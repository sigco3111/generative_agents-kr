"""
File: translate_prompts_kr.py
용도: 영문 프롬프트 (.txt) → 한국어 자동 번역
실행: cd reverie/backend_server/persona/prompt_template && python3 translate_prompts_kr.py

설계:
- 원본 파일 구조 보존: prompt_template_kr/{v1,v2,v3_ChatGPT,safety}/...
- NIM gpt-oss-120b 사용 (gpt_structure.py)
- 번역 가이드:
  * 코드 변수 (<NAME_0>, [brackets], {! !}) 절대 보존
  * JSON 스키마/예시는 한국 시나리오로 자연스럽게 변환
  * 짧은 단어 (I, you)는 한국 호응 ("나는", "당신은")으로 명시
  * 조사 자동 처리 (은/는, 이/가 등)는 LLM에게 위임
  * 영어 예시 이름 (Isabella, Maria, Klaus) → 한국 이름 유지 (한국어 페르소나 시드와 일관성)
- 검수 단계: 사람이 diff 보고 수정 가능 (해시 비교)

=== 사용법 ===
1. NIM 키 설정: export NVIDIA_API_KEY=...
2. python3 translate_prompts_kr.py
3. 결과: persona/prompt_template_kr/ 디렉토리에 *_kr.txt 파일 생성
"""
import os
import re
import sys
import time
import json
import hashlib

# 같은 디렉토리의 gpt_structure 사용
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gpt_structure import ChatGPT_request

PROMPT_DIR = os.path.dirname(os.path.abspath(__file__))
KR_DIR = os.path.join(PROMPT_DIR, "prompt_template_kr")
SRC_DIR = PROMPT_DIR

TRANSLATION_GUIDE = """당신은 영문 프롬프트를 한국어로 번역하는 전문가입니다.

=== 번역 규칙 ===
1. **코드 변수 보존 (절대 변경 금지)**:
   - `<NAME_0>`, `[ ... ]`, `{ ... }`, `!<INPUT N>!`, `###`
   - `\n` (이스케이프 시퀀스), 함수 호출 형식
   - JSON 키/값, 정규식 패턴

2. **콘텐츠 (영어 본문)**:
   - 자연스러운 한국어 (~습니다체 기본, 명령문은 ~하세요)
   - 어려운 영문 어구는 풀어서 설명
   - 예시 이름을 한국 이름 (이서연, 김민준, 박지우)으로 변경 가능
   - 시나리오 (카페, 도서관, 자전거 동호회)에 맞게 자연스럽게

3. **한국어 조사 처리**:
   - 받침 있으면 "은/이", 없으면 "는/가" 자동
   - "와/과", "을/를" 정확히

4. **번역 스타일**:
   - 기계번역 말투 X
   - 자연스러운 한국어 LLM 프롬프트 OK
   - LLM이 읽고 JSON/구조화된 응답을 생성할 수 있도록 명확하게

5. **출력 형식**:
   - 오직 번역된 텍스트만 출력 (설명 금지)
   - 원본 포맷 (들여쓰기, 줄바꿈) 보존

=== 예시 ===
원문: "Is Maria Lopez working on her physics degree?"
번역: "이서연은 물리학 학위를 따기 위해 공부 중인가?"

원문: "Output the response in json."
번역: "응답을 json으로 출력하세요."

번역: "Score [0-3]"
번역: "점수 [0-3]"  # 코드 보존

"""

# ---------------------------------------------------------------------------
# 활성 프롬프트 식별
# ---------------------------------------------------------------------------

def get_active_prompts():
    """run_gpt_prompt.py에서 active (주석 아님) 프롬프트 파일 목록."""
    runner = os.path.join(PROMPT_DIR, "run_gpt_prompt.py")
    with open(runner) as f:
        content = f.read()

    active = set()
    for line in content.split("\n"):
        if "prompt_template =" in line:
            if not line.lstrip().startswith("#"):
                cleaned = line.split("########")[0]
                if '"' in cleaned:
                    parts = cleaned.split('"', 2)
                    if len(parts) >= 2:
                        val = parts[1]
                        if val.startswith("persona/prompt_template/"):
                            val = val[len("persona/prompt_template/"):]
                        active.add(val)

    result = []
    for rel in sorted(active):
        p = os.path.join(PROMPT_DIR, rel)
        if os.path.exists(p):
            result.append(rel)
    return result


# ---------------------------------------------------------------------------
# 단일 파일 번역
# ---------------------------------------------------------------------------

def translate_file(src_path, dst_path):
    """하나의 프롬프트 파일을 영문 -> 한국어로 번역."""
    if os.path.exists(dst_path):
        return False  # 이미 번역됨

    with open(src_path, encoding="utf-8") as f:
        src_text = f.read()

    if not src_text.strip():
        return False

    prompt = TRANSLATION_GUIDE + "\n=== 번역할 텍스트 ===\n" + src_text + "\n=== 끝 ===\n\n위 텍스트를 한국어로 번역하세요. 코드 표식은 그대로 유지하고 본문만 자연스러운 한국어로 번역하세요. 번역 결과만 출력:"

    for attempt in range(2):
        response = ChatGPT_request(prompt)
        if response and response != "ChatGPT ERROR" and len(response) > 50:
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            with open(dst_path, "w", encoding="utf-8") as f:
                f.write(response.strip() + "\n")
            return True
        time.sleep(2)

    return False


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Generative Agents 한국어 프롬프트 자동번역")
    print("=" * 70)

    active = get_active_prompts()
    print(f"\n활성 프롬프트 파일: {len(active)}개\n")

    os.makedirs(KR_DIR, exist_ok=True)

    success = 0
    skip = 0
    fail = 0
    total_chars = 0
    start = time.time()

    for i, rel in enumerate(active, 1):
        src = os.path.join(PROMPT_DIR, rel)
        dst = os.path.join(KR_DIR, rel)

        if os.path.exists(dst):
            print(f"  [{i:2d}/{len(active)}] SKIP {rel} (이미 번역됨)")
            skip += 1
            continue

        src_size = os.path.getsize(src)
        print(f"  [{i:2d}/{len(active)}] ... {rel} ({src_size}자) -> 번역 중...", end=" ", flush=True)

        t0 = time.time()
        ok = translate_file(src, dst)
        elapsed = time.time() - t0

        if ok:
            kr_size = os.path.getsize(dst)
            total_chars += kr_size
            print(f"OK ({kr_size}자, {elapsed:.1f}초)")
            success += 1
        else:
            fail += 1
            print("FAIL")

        time.sleep(0.5)

    elapsed = time.time() - start
    print()
    print("=" * 70)
    print("결과")
    print("=" * 70)
    print(f"  성공: {success}개")
    print(f"  스킵: {skip}개")
    print(f"  실패: {fail}개")
    print(f"  총 번역 글자: {total_chars:,}자")
    print(f"  소요 시간: {elapsed/60:.1f}분")
    print(f"  결과 위치: {KR_DIR}")


if __name__ == "__main__":
    main()
