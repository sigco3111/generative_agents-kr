"""
File: gpt_structure.py (NIM 백엔드판)
원본: joonspk-research/generative_agents/persona/prompt_template/gpt_structure.py
라이선스: Apache 2.0 (원본) — sigco3111 한글화/수정본
변경 사항:
  - OpenAI ChatCompletion/Completion/Embedding → NVIDIA NIM (openai 호환)
  - LLM: openai/gpt-oss-120b (gpt-3.5-turbo / gpt-4 대체, 통합)
  - 임베딩: nvidia/llama-nemotron-embed-1b-v2 (asymmetric, 2048d)
  - 비동기 호출 → 동기 (원본 인터페이스 유지)
  - 추가: get_passage_embedding() / get_query_embedding() (asymmetric 분리)
  - 추가: NEGATION_GUARD (한국어 부정 표현 검색 가드)
"""
import os
import json
import re
import time
import random
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# NIM (NVIDIA) 설정 — utils.py에서 주입됨
# ---------------------------------------------------------------------------

# 다음 값들은 utils.py에서 import됨
try:
    from utils import (
        openai_api_key as nim_api_key,
        key_owner,
        maze_assets_loc,
        env_matrix,
        env_visuals,
        fs_storage,
        fs_temp_storage,
        collision_block_id,
        debug,
    )
except ImportError:
    # standalone 테스트 시 fallback
    nim_api_key = os.environ.get("NVIDIA_API_KEY", "")
    key_owner = "test"
    debug = False

NIM_BASE_URL = "https://integrate.api.nvidia.com/v1"
CHAT_MODEL = "openai/gpt-oss-120b"          # 120B reasoning model
EMBED_MODEL = "nvidia/llama-nemotron-embed-1b-v2"  # 2048d asymmetric

# ---------------------------------------------------------------------------
# NIM API 클라이언트 (OpenAI 호환)
# ---------------------------------------------------------------------------

def _nim_post(endpoint, body, timeout=60):
    """NIM API에 POST 요청. 응답은 JSON dict.

    NIM gpt-oss-120b 마이그레이션: urllib.request.urlopen이 keep-alive
    연결에서 hang. requests + connect_timeout 분리.
    timeout은 더 짧은 60초로 (시뮬 100 step에 ~1000 LLM 호출).
    """
    import requests as _requests
    url = f"{NIM_BASE_URL}{endpoint}"
    headers = {
        "Authorization": f"Bearer {nim_api_key}",
        "Content-Type": "application/json",
    }
    try:
        r = _requests.post(
            url,
            json=body,
            headers=headers,
            timeout=(5, timeout),  # (connect, read) — 빠른 fail
        )
        r.raise_for_status()
        return r.json()
    except _requests.exceptions.Timeout:
        raise urllib.error.URLError(f"NIM request timeout ({timeout}s)")
    except _requests.exceptions.RequestException as e:
        if hasattr(e, "response") and e.response is not None:
            raise urllib.error.HTTPError(
                url, e.response.status_code, str(e), {}, None
            )
        raise urllib.error.URLError(str(e))


def temp_sleep(seconds=0.1):
    time.sleep(seconds)


# ---------------------------------------------------------------------------
# 부정(negation) 가드
# ---------------------------------------------------------------------------
# 한국어/영어 부정 표현이 passage/query 양쪽에 있는 경우 retrieval 점수를
# 강제로 낮춥니다. (임베딩 모델은 "~않다"를 무시하는 경향 — 검증된 한계)
# ---------------------------------------------------------------------------
NEGATION_KO = ["않", "안 ", "못 ", "없", "아니", "말고", "싫어하", "거부하", "반대하"]
NEGATION_EN = ["not ", "n't ", " no ", "never", "none", "cannot", "won't", "hate", "refuse"]


def negation_penalty(text_a: str, text_b: str) -> float:
    """passage/query 양쪽의 부정 표현 비대칭 시 페널티 반환 (0.0 ~ 0.4)."""
    a_lower = text_a.lower()
    b_lower = text_b.lower()
    a_neg = any(neg in a_lower for neg in NEGATION_KO + NEGATION_EN)
    b_neg = any(neg in b_lower for neg in NEGATION_KO + NEGATION_EN)
    # 한쪽만 부정: 강한 페널티
    if a_neg != b_neg:
        return 0.4
    # 양쪽 다 부정: 약한 페널티 (둘 다 부정일 가능성 높음)
    if a_neg and b_neg:
        return 0.1
    return 0.0


# ---------------------------------------------------------------------------
# 채팅 (LLM) 호출
# ---------------------------------------------------------------------------

def _nim_chat(messages, model=CHAT_MODEL, temperature=0.7, max_tokens=2048, top_p=1.0):
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
    }
    resp = _nim_post("/chat/completions", body)
    msg = resp["choices"][0]["message"]

    # gpt-oss-120b (reasoning model) 처리:
    # reasoning_content에 사고를 출력하고, content는 None이거나 짧음.
    # 비어있으면 reasoning에서 추출 시도 (간단한 후처리).
    content = msg.get("content") or ""
    if not content.strip():
        reasoning = msg.get("reasoning_content") or ""
        if reasoning.strip():
            # reasoning 끝부분에서 실제 응답을 추출 (간단 휴리스틱)
            # gpt-oss-120b reasoning은 일반적으로 "<final>...</final>" 포함
            import re as _re
            # 1) "<final>...</final>" 패턴 시도
            m = _re.search(r"<final>(.*?)</final>", reasoning, _re.DOTALL)
            if m:
                content = m.group(1).strip()
            else:
                # 2) reasoning 마지막 줄 시도
                lines = [l for l in reasoning.strip().split("\n") if l.strip()]
                # 마크다운 코드 펜스 제거
                last = lines[-1].strip().strip("`")
                # 너무 길면 마지막 문장 추출
                if len(last) > max_tokens * 4:  # 명백히 너무 김
                    content = (lines[-2].strip() if len(lines) > 1 else last)[:max_tokens * 3]
                else:
                    content = last

    return content


def ChatGPT_single_request(prompt):
    """gpt-3.5-turbo 단건 호출 대체."""
    temp_sleep()
    return _nim_chat([{"role": "user", "content": prompt}], temperature=0.7)


def ChatGPT_request(prompt):
    """gpt-3.5-turbo 호출 (여러 번 시도)."""
    temp_sleep()
    try:
        return _nim_chat([{"role": "user", "content": prompt}])
    except Exception as e:
        if debug:
            print(f"[ChatGPT_request ERROR] {e}")
        return "ChatGPT ERROR"


def GPT4_request(prompt):
    """gpt-4 호출 (gpt-oss-120b로 통일, 높은 temperature로 다양한 응답)."""
    temp_sleep()
    try:
        return _nim_chat(
            [{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=4096,
        )
    except Exception as e:
        if debug:
            print(f"[GPT4_request ERROR] {e}")
        return "ChatGPT ERROR"


# ---------------------------------------------------------------------------
# Safe response (재시도 + JSON 파싱)
# ---------------------------------------------------------------------------

def _safe_generate(model_name, prompt, example_output, special_instruction,
                    repeat=3, fail_safe_response="error",
                    func_validate=None, func_clean_up=None, verbose=False):
    """원본 ChatGPT_safe_generate_response / GPT4_safe_generate_response 통합."""
    full_prompt = '"""\n' + prompt + '\n"""\n'
    full_prompt += f"Output the response to the prompt above in json. {special_instruction}\n"
    full_prompt += "Example output json:\n"
    full_prompt += '{"output": "' + str(example_output) + '"}'

    if verbose:
        print("[PROMPT]", full_prompt)

    for i in range(repeat):
        try:
            if model_name == "GPT4":
                response = GPT4_request(full_prompt).strip()
            else:
                response = ChatGPT_request(full_prompt).strip()

            end_index = response.rfind("}") + 1
            response = response[:end_index]
            parsed = json.loads(response)["output"]

            if func_validate and func_validate(parsed, prompt=full_prompt):
                return func_clean_up(parsed, prompt=full_prompt) if func_clean_up else parsed

            if verbose:
                print(f"---- repeat {i}:", response)
        except Exception:
            if verbose:
                print(f"---- repeat {i} failed")
            continue

    if debug:
        print("[WARN] safe_generate_response returning fail_safe")
    return fail_safe_response


def ChatGPT_safe_generate_response(prompt, example_output, special_instruction,
                                    repeat=3, fail_safe_response="error",
                                    func_validate=None, func_clean_up=None, verbose=False):
    return _safe_generate("ChatGPT", prompt, example_output, special_instruction,
                          repeat, fail_safe_response, func_validate, func_clean_up, verbose)


def GPT4_safe_generate_response(prompt, example_output, special_instruction,
                                 repeat=3, fail_safe_response="error",
                                 func_validate=None, func_clean_up=None, verbose=False):
    return _safe_generate("GPT4", prompt, example_output, special_instruction,
                          repeat, fail_safe_response, func_validate, func_clean_up, verbose)


# 하위 호환
def ChatGPT_safe_generate_response_OLD(prompt, repeat=3, fail_safe_response="error",
                                        func_validate=None, func_clean_up=None, verbose=False):
    """validate 없이 단순 반복 호출 (원본 OLD API)."""
    if verbose:
        print(prompt)
    for i in range(repeat):
        try:
            resp = ChatGPT_request(prompt).strip()
            if func_validate and func_validate(resp, prompt=prompt):
                return func_clean_up(resp, prompt=prompt) if func_clean_up else resp
        except Exception:
            pass
    return fail_safe_response


# ---------------------------------------------------------------------------
# 원본 GPT-3 (Completion) API — 테스트/구 호환용
# ---------------------------------------------------------------------------

def GPT_request(prompt, gpt_parameter):
    """원본 Completion.create() 호환. gpt-3.5-turbo로 우회.

    NIM gpt-oss-120b 마이그레이션: max_tokens 기본값 100 → 1000으로 상향.
    (reasoning 모델이 응답 잘림 방지)
    """
    temp_sleep()
    try:
        return _nim_chat(
            [{"role": "user", "content": prompt}],
            model=CHAT_MODEL,
            temperature=gpt_parameter.get("temperature", 0.7),
            max_tokens=gpt_parameter.get("max_tokens", 1000),
        )
    except Exception:
        return "TOKEN LIMIT EXCEEDED"


def safe_generate_response(prompt, gpt_parameter, repeat=5, fail_safe_response="error",
                            func_validate=None, func_clean_up=None, verbose=False):
    if verbose:
        print(prompt)
    for i in range(repeat):
        resp = GPT_request(prompt, gpt_parameter)
        # NIM gpt-oss-120b 마이그레이션: 깨진 응답 감지
        # TOKEN LIMIT / 빈 응답 / 너무 짧은 응답은 즉시 fail_safe
        if not resp or "TOKEN LIMIT" in resp or len(resp.strip()) < 20:
            if debug:
                print(f"[WARN] bad response (attempt {i+1}): retry")
            continue
        if func_validate and func_validate(resp, prompt=prompt):
            return func_clean_up(resp, prompt=prompt) if func_clean_up else resp
    return fail_safe_response


def generate_prompt(curr_input, prompt_lib_file):
    """원본 generate_prompt() 호환 + 한국어 자동 라우팅.

    prompt_lib_file이 "persona/prompt_template/..." 형태일 때,
    prompt_template_kr/ 아래에 동일 상대경로 파일이 있으면 그것을 우선 사용.
    없으면 영문 원본 사용 (fallback).
    """
    # 한국어 자동 라우팅: prompt_template_kr/ 우선
    if prompt_lib_file.startswith("persona/prompt_template/"):
        ko_rel = prompt_lib_file[len("persona/prompt_template/"):]
        # 절대 경로 우선 시도 -> cwd 기준으로 fallback
        candidates = [
            os.path.join("persona", "prompt_template_kr", ko_rel),
            os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "prompt_template_kr", ko_rel,
            ),
        ]
        # 또는 cwd가 reverie/backend_server/persona 라면 prompt_template_kr 직접
        candidates.append(os.path.join("prompt_template_kr", ko_rel))
        for c in candidates:
            if os.path.exists(c):
                prompt_lib_file = c
                break
    if isinstance(curr_input, str):
        curr_input = [curr_input]
    curr_input = [str(i) for i in curr_input]
    with open(prompt_lib_file, "r", encoding="utf-8") as f:
        prompt = f.read()
    for count, i in enumerate(curr_input):
        prompt = prompt.replace(f"!<INPUT {count}>!", i)
    if "<commentblockmarker>###</commentblockmarker>" in prompt:
        prompt = prompt.split("<commentblockmarker>###</commentblockmarker>")[1]
    return prompt.strip()


# ---------------------------------------------------------------------------
# 임베딩 (비대칭)
# ---------------------------------------------------------------------------

def _nim_embed(text, input_type):
    # NIM gpt-oss-120b (reasoning model) 마이그레이션: 빈/특수 입력에 500 가능.
    # 빈 텍스트/공백만 있는 경우 0 벡터 반환 (NIM 호출 안 함).
    safe_text = (text or "").strip()
    if not safe_text:
        # 2048d 0 벡터 반환 (모델 출력 차원과 동일)
        return [0.0] * 2048
    body = {
        "model": EMBED_MODEL,
        "input": [safe_text],
        "input_type": input_type,
    }
    try:
        resp = _nim_post("/embeddings", body)
        return resp["data"][0]["embedding"]
    except urllib.error.HTTPError as e:
        # 500/400 일 때 한 번만 재시도, 그래도 안되면 0 벡터
        if e.code in (500, 502, 503, 504):
            try:
                resp = _nim_post("/embeddings", body)
                return resp["data"][0]["embedding"]
            except Exception:
                return [0.0] * 2048
        return [0.0] * 2048
    except Exception:
        return [0.0] * 2048


def get_embedding(text, model=None):
    """원본 호환: input_type=passage 기본값."""
    text = (text or "this is blank").replace("\n", " ")
    return _nim_embed(text, "passage")


def get_passage_embedding(text):
    """메모리 저장 시 사용 (input_type=passage)."""
    text = (text or "this is blank").replace("\n", " ")
    return _nim_embed(text, "passage")


def get_query_embedding(text):
    """메모리 검색 시 사용 (input_type=query)."""
    text = (text or "this is blank").replace("\n", " ")
    return _nim_embed(text, "query")


def cosine_similarity(a, b):
    """두 임베딩 벡터의 코사인 유사도 (0.0 ~ 1.0)."""
    if not a or not b:
        return 0.0
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return sum(x * y for x, y in zip(a, b)) / (na * nb)


def score_memory(query_text, memory_text,
                 query_emb=None, memory_emb=None,
                 use_negation_guard=True):
    """
    메모리 retrieval 점수 계산.
    - query_text / memory_text (raw)
    - query_emb / memory_emb (optional, precomputed)
    - 부정 가드 자동 적용
    """
    if query_emb is None:
        query_emb = get_query_embedding(query_text)
    if memory_emb is None:
        memory_emb = get_passage_embedding(memory_text)
    sim = cosine_similarity(query_emb, memory_emb)
    if use_negation_guard:
        sim -= negation_penalty(query_text, memory_text)
    return max(0.0, sim)


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== NIM gpt_structure self-test ===\n")

    # 1. 채팅
    print("[1] ChatGPT_single_request('ping 한 단어만')")
    try:
        r = ChatGPT_single_request("ping 한 단어만")
        print(f"    응답: {r.strip()}\n")
    except Exception as e:
        print(f"    ❌ {e}\n")

    # 2. 임베딩 (asymmetric)
    print("[2] 비대칭 임베딩 (passage vs query)")
    try:
        p = get_passage_embedding("이서연은 카페에서 커피를 마신다")
        q = get_query_embedding("이서연이 마신 음료는?")
        sim_pq = cosine_similarity(p, q)
        print(f"    차원: {len(p)}")
        print(f"    '이서연 카페 커피' ↔ '이서연 음료' = {sim_pq:.3f}")

        p2 = get_passage_embedding("이서연은 카페에서 커피를 마신다")
        q2 = get_query_embedding("이서연이 마신 음료는?")
        sim_pq2 = cosine_similarity(p2, q2)
        print(f"    재호출 안정성: {sim_pq2:.3f}")

        # 부정 가드
        pn = get_passage_embedding("이서연은 카페에서 커피를 마시지 않았다")
        qn = get_query_embedding("이서연이 마신 음료는?")
        sim_neg = cosine_similarity(pn, qn)
        guarded = sim_neg - negation_penalty("이서연은 카페에서 커피를 마시지 않았다",
                                             "이서연이 마신 음료는?")
        print(f"    부정 케이스 (가드 전): {sim_neg:.3f}, (가드 후): {guarded:.3f}")
    except Exception as e:
        print(f"    ❌ {e}\n")
