# 🏘️ Generative Agents 한국어판 (NVIDIA NIM)

> **원본**: [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) · **라이선스**: Apache 2.0
>
> **본 fork의 변경점**: LLM 백엔드를 OpenAI → **NVIDIA NIM** 으로 교체, **한국어 환경 완전 최적화** (페르소나 + 프롬프트 + UI)

<p align="center">
  <img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

이 저장소는 Stanford의 ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442) 논문을 **한국어 환경에서 완전 재현**하기 위한 fork입니다. NIM API 키 하나로 한국어 시뮬레이션을 띄울 수 있습니다.

**원본 대비 주요 차이점**:

| 영역 | 원본 | 본 fork |
|------|------|---------|
| **LLM** | OpenAI GPT-3.5/4 | NVIDIA NIM `openai/gpt-oss-120b` (120B reasoning) |
| **임베딩** | OpenAI `text-embedding-ada-002` (1536d symmetric) | NIM `nvidia/llama-nemotron-embed-1b-v2` (2048d **asymmetric**) |
| **페르소나** | 영어 (Isabella/Maria/Klaus) | **한국어 (이서연/김민준/박지우)** — 한강 자전거 동호회 |
| **프롬프트** | 영어 35+개 | **한국어 35개** 자동번역 + 라우팅 |
| **UI** | 영어 | **한국어** (Django 6 템플릿) |
| **부정 가드** | 없음 | 한국어 "않/말/없/아니" 보정 내장 |

> 🎉 **현재 상태**: Phase 1-5 모두 완료. 한국어 시뮬레이션 기능 검증됨.

---

## 📋 사전 요구사항

- Python 3.9+
- NVIDIA NIM API 키 ([build.nvidia.com](https://build.nvidia.com)에서 무료 발급)
- 메모리 4GB+ — 임베딩 차원 2048 × 에이전트 3명 × 메모리 1000개 시 약 50MB

## 🚀 설치

```bash
# 1. 클론
git clone https://github.com/sigco3111/generative_agents-kr.git
cd generative-agents-kr

# 2. venv 생성 (PEP 668 회피 — macOS Sonoma+ 권장)
python3 -m venv .venv
source .venv/bin/activate

# 3. 의존성 설치 (requirements.txt는 이미 Python 3.11+ 호환 버전으로 갱신됨)
pip install -r requirements.txt
pip install python-dotenv  # 선택

# 4. NIM API 키 설정 (https://build.nvidia.com 에서 무료 발급)
#    키 형식: nvapi-XXXXXXXXXXXXXXXXXXXXXXXXXXXX (보통 60자+)
export NVIDIA_API_KEY="nvapi-..."

# 5. 백엔드 self-test (선택이지만 강력 권장)
cd reverie/backend_server/persona/prompt_template
python3 gpt_structure.py
```

> ⚠️ **API 키 에러 디버깅**: `HTTP Error 500: Internal Server Error` 또는
> `Missing request extension: headers::common::authorization` 에러가 나면
> NIM API 키가 잘못된 것입니다. 키 발급 사이트 ([build.nvidia.com](https://build.nvidia.com))
> 에서 새 키를 받아 다시 export 하세요. 500/401/403 모두 키 문제일 가능성이 높습니다.
>
> 여러 키를 가지고 있다면 `~/.hermes/secrets/nvidia_keys.env` 파일에 저장 후:
> ```bash
> source ~/.hermes/secrets/nvidia_keys.env
> export NVIDIA_API_KEY="$NVIDIA_API_KEY_1"
> ```

> ⚠️ **macOS Sonoma+ / 시스템 Python 사용자**: `pip install -r requirements.txt` 시
> "command not found: pip" 또는 "externally-managed-environment" 에러가 날 수 있습니다.
> 위 예시처럼 `.venv`를 만들고 활성화해서 사용하세요.
>
> 이미 다른 venv를 쓰고 있다면 그것을 활성화해도 됩니다.
> (예: Hermes 환경이 있다면 `source ~/.hermes/hermes-agent/venv/bin/activate`)

**기대 출력**:
```
=== NIM gpt_structure self-test ===
[1] ChatGPT_single_request('ping 한 단어만')
    응답: ping
[2] 비대칭 임베딩 (passage vs query)
    차원: 2048
    '이서연 카페 커피' ↔ '이서연 음료' = 0.474
    부정 케이스 (가드 전): 0.457, (가드 후): 0.057
```

## ⚠️ Python 호환성 노트

원본 `requirements.txt`는 **2022년 Python 3.7~3.9 환경에서 작성**되었습니다.

본 fork는 Python 3.11+ 호환성 문제를 해결하기 위해 `requirements.txt`에 다음 변경을 미리 적용했습니다:
- `Pillow>=10.0` (8.4.0은 wheel 부재로 libjpeg 빌드 실패)
- `Django>=4.2,<5` (2.2는 Python 3.11 syntax 미지원)
- `gensim>=4.3` (3.8.0은 cython 빌드 실패)
- `asgiref>=3.6`, `numpy>=1.26`, `pandas>=2.0`, `scikit-learn>=1.4`, `scipy>=1.11`, `six>=1.16` (의존성 충돌 방지)

원본 strict 버전은 `requirements-original-2022.txt`에 백업. **사용자는 그냥 `pip install -r requirements.txt`만 하면 됩니다.**

### 검증된 의존성 조합 (2026-07)

본 fork는 다음 버전으로 self-test 통과 검증됨:

| 패키지 | 검증 버전 |
|--------|----------|
| Django | 4.2.30 |
| numpy | 1.26.4 |
| pandas | 3.0.3 |
| scikit-learn | 1.9.0 |
| gensim | 4.4.0 |
| scipy | 1.17.1 |
| matplotlib | 3.11.0 |
| openai | 2.24.0 |
| Pillow | 12.2.0 |
| seaborn | 0.13.2 |

> ⚠️ **원본 시뮬레이션 코드와의 호환성**: 위 업그레이드 조합은 self-test (`gpt_structure.py`) 통과 확인됨.
> 실제 `reverie.py` 실행 시 Django 4.x 변경사항 (예: `path()` 사용) 으로 마이그레이션 필요할 수 있음.

---

## 🎮 시뮬레이션 실행

> **⚠️ 시뮬레이션은 두 개의 별도 터미널에서 실행됩니다:**
> - **터미널 1**: Django 시각화 서버 (`manage.py runserver`)
> - **터미널 2**: 시뮬레이션 백엔드 (`reverie.py`)
>
> 두 서버가 **동시에 실행 중**이어야 브라우저에서 시뮬레이션을 볼 수 있습니다.

**각 터미널을 열 때마다 venv를 먼저 활성화해야 합니다** (새 shell에서는 venv가 자동 비활성화됨).

### 터미널 1: Django 시각화 서버

```bash
cd /path/to/generative-agents-kr
source .venv/bin/activate
export NVIDIA_API_KEY="***"
unset PYTHONPATH  # ← Hermes 데스크탑 사용 시 필수

cd environment/frontend_server
python manage.py runserver
# → http://localhost:8000 접속 (브라우저에서 열어두세요)
```

### 터미널 2: 시뮬레이션 백엔드

```bash
cd /path/to/generative-agents-kr
source .venv/bin/activate
export NVIDIA_API_KEY="***"
unset PYTHONPATH  # ← Hermes 데스크탑 사용 시 필수

cd reverie/backend_server
python3 reverie.py
# → "Enter name of forked simulation:" 에 시나리오 이름 입력 (예: July1_the_ville_n3_kr_test)
# → "Enter option:" 에 run 100
```

브라우저를 새로고침하면 메인 시뮬레이션 화면이 한국어로 표시됩니다.

### 시뮬레이션 백엔드에서 쓸 수 있는 명령어 (reverie.py 입력)

| 명령 | 설명 |
|------|------|
| `run 100` | 100 step 시뮬레이션 진행 |
| `save` | 현재 상태 저장 |
| `fin` / `finish` | 저장 후 종료 |
| `print persona schedule 이서연` | 페르소나의 일과 출력 |
| `print all persona schedule` | 모든 페르소나의 일과 출력 |
| `exit` | 저장하지 않고 종료 (데이터 삭제) |

> 💡 **시나리오 시작 방법**:
> 1. **storage/ 디렉토리가 비어 있으면** 원본 시나리오를 fork해야 합니다.
>    `storage/base_the_ville_isabella_maria_klaus` (원본 Isabella/Maria/Klaus 시나리오) 다운로드:
>    ```bash
>    # sparse-checkout으로 storage/만 가져오기 (1GB)
>    git clone --depth 1 --filter=blob:none --sparse https://github.com/joonspk-research/generative_agents.git /tmp/ga-orig
>    cd /tmp/ga-orig && git sparse-checkout set environment/frontend_server/storage
>    cp -r environment/frontend_server/storage/base_the_ville_isabella_maria_klaus /Users/mac/work/generative-agents-kr/environment/frontend_server/storage/
>    rm -rf /tmp/ga-orig
>    ```
>
> 2. **reverie.py 실행** (새 시나리오 생성):
>    ```
>    Enter the name of the forked simulation: base_the_ville_isabella_maria_klaus
>    Enter the name of the new simulation: ICBM_kr_test
>    ```
>    새 시나리오 `ICBM_kr_test`가 만들어지고 메인 프롬프트 진입.
>
> 3. **시뮬레이션 시작** (메인 프롬프트):
>    ```
>    Enter option: run 100
>    ```
>    100 step 시뮬레이션이 진행됨 (1 step당 ~10초 = 약 17분 소요).
>    NIM LLM 호출이므로 NIM API 키와 인터넷 연결 필수.
>
> 4. **브라우저에서 실시간 확인**:
>    - **터미널 1**의 Django 서버가 띄워져 있어야 함 (위 "터미널 1" 가이드)
>    - 브라우저로 `http://localhost:8000/replay/ICBM_kr_test/0/` 접속
>    - 또는 `http://localhost:8000/` 에서 시뮬레이션 목록 확인 후 진입
>    - 한국어 UI로 페르소나들의 현재 행동/대화가 실시간 표시됨
>    - step이 진행될 때마다 페르소나 행동 업데이트
>
> 5. **시뮬레이션 일시정지/재개** (브라우저에서):
>    - 화면 상단 ▶ 재생 / ⏸ 일시정지 버튼
>    - 또는 URL의 step 번호 변경 (예: `/replay/ICBM_kr_test/50/`)
>
> 6. **시뮬레이션 저장 + 종료** (터미널 2의 reverie.py 프롬프트에서):
>    ```
>    Enter option: fin
>    ```
>    다음에 같은 시나리오로 돌아오려면 `Enter the name of the forked simulation: ICBM_kr_test` 입력.

### ⚠️ 새 shell + venv + PYTHONPATH 주의

- 새 shell을 열 때마다 venv가 풀리므로 `source .venv/bin/activate` 잊지 마세요
- `.zshrc`에 NVIDIA_API_KEY 등록하면 편리:
  ```bash
  echo 'export NVIDIA_API_KEY="***"' >> ~/.zshrc
  ```
- **Hermes 데스크탑 사용자**: `PYTHONPATH=/Users/mac/.hermes/hermes-agent/...`가
  자동으로 export 되어 .venv 패키지가 아닌 Hermes 패키지가 import 됩니다.
  venv 활성화 후 `unset PYTHONPATH` 필수. 또는 alias 등록:
  ```bash
  cat >> ~/.zshrc << 'EOF'
  alias ungate-hermes='unset PYTHONPATH'
  EOF
  ```

### 🐍 Django 4.x 마이그레이션 (완료됨)

`reverie.py`와 Django 시각화 코드는 원본 (Django 2.2) 기반으로 작성됐지만, 본 fork는 **Django 4.2 LTS**로 실행됩니다.

본 fork가 적용한 Django 2 → 4 마이그레이션 패치:

| 파일 | 변경 |
|------|------|
| `requirements.txt` | `django-cors-headers>=3.5` (2.5.3은 `django.utils.six` 사용으로 4.0에서 깨짐) |
| `frontend_server/urls.py` | `django.conf.urls.url` → `re_path` (url은 4.0에서 제거) |
| `translator/views.py` | `django.contrib.staticfiles.templatetags.staticfiles` → `django.templatetags.static` |
| 11개 템플릿 | `{% load staticfiles %}` → `{% load static %}` |

검증: `python manage.py check` → `System check identified no issues`, `python manage.py runserver` → HTTP 200 OK.

---

## 🇰🇷 한국어 시뮬레이션 작동 검증

### 페르소나 시나리오: 한강 자전거 동호회

| 이름 | 직업 | 주요 특성 |
|------|------|----------|
| **이서연** (27) | 도시계획 석사 | 자전거 동호회 회원, 김민준에게 짝사랑 |
| **김민준** (28) | 데이터 사이언스 석사 | 도서관 단골, 한강 카페 알바, 이서연 짝사랑 |
| **박지우** (29) | 마케팅 매니저 | 자전거 동호회 운영진, 둘 서로 좋아하는 사실 알고 있음 |

### 실제 LLM 출력 (Phase 5 검증)

```bash
cd reverie/backend_server
python3 test_kr_sim.py
# "이서연은 무엇을 마실까?" → "부드러운 바닐라 라떼 한 잔을 마시면 카페 분위기와 잘 어울릴 거예요."
```

**한국어 agent_chat 검증 (이서연 ↔ 김민준)**:
```
이서연: "민준아, 요즘 데이터 분석 프로젝트는 어때?"
김민준: "음... 아직 모델링 단계라 좀 복잡하지만 재밌어."
이서연: "우리 이번 주말에 한강 자전거 타면서 얘기 좀 할까?"
김민준: "좋아! 타면서 도시계획 아이디어도 공유하고 말이야."
```

---

## 🛠️ 주요 API 가이드

### 한국어 페르소나 사용

```python
from persona.persona_seed_kr import PERSONAS_KR_N3, to_whisper_csv

# 3명 페르소나 dict
for name, persona in PERSONAS_KR_N3.items():
    print(f"{name}: {persona['secret']}")
    print(to_whisper_csv(persona))
```

### 비대칭 임베딩 (저장/검색 분리)

```python
from persona.prompt_template.gpt_structure import (
    get_passage_embedding,
    get_query_embedding,
    score_memory,
)

# 메모리 저장 시 (passage 형태)
p_emb = get_passage_embedding("이서연은 카페에서 커피를 마신다")

# 메모리 검색 시 (query 형태)
q_emb = get_query_embedding("이서연이 마신 음료는?")

# 검색 (부정 가드 내장)
score = score_memory(
    query_text="이서연이 마신 음료는?",
    memory_text="이서연은 카페에서 커피를 마시지 않았다",
)
# 0.057 (낮음 — "마시지 않았다"로 정확히 분리)
```

### 한국어 프롬프트 자동 라우팅

`generate_prompt()`가 `persona/prompt_template/...` 경로 호출 시 동일 상대경로의 `prompt_template_kr/` 파일이 있으면 자동 사용. **코드 변경 없이 영어/한국어 전환**.

```python
from persona.prompt_template.gpt_structure import generate_prompt

# 자동으로 한국어 버전이 로드됨
prompt = generate_prompt(inputs, "persona/prompt_template/v2/whisper_inner_thought_v1.txt")
# "이서연에 대한 진술로 다음 생각을 번역하세요..."
```

---

## 🔧 한국어 자동화 도구

Phase 3에서 개발한 자동화 도구 (재실행 가능):

| 도구 | 용도 | 실행 |
|------|------|------|
| `translate_prompts_kr.py` | 35개 영문 프롬프트 → 한국어 자동번역 | `cd .../prompt_template && python3 translate_prompts_kr.py` |
| `review_prompts_kr.py` | 번역 결과 자동 검수 (코드 손실/어색 패턴 검출) | `cd .../prompt_template && python3 review_prompts_kr.py` |

---

## 📊 Phase별 진행 상황

| Phase | 내용 | 결과 |
|-------|------|------|
| **1** | LLM 백엔드 (NIM) 교체 | ✅ 완료 (`b6456da`) |
| **1.5** | 비대칭 임베딩 + 부정 가드 | ✅ 완료 (`b6456da`) |
| **2** | 한국어 페르소나 3명 시드 | ✅ 완료 (`51f13d7`) |
| **3** | 프롬프트 35개 자동번역 + 검수 + 라우팅 | ✅ 완료 (`d3b0210`) |
| **4** | Django UI 6 템플릿 한글화 | ✅ 완료 (`7fb0460`) |
| **5** | 한국어 시뮬레이션 통합 검증 | ✅ 완료 (`67afc84`) |
| **Bug Fix** | `gpt-oss-120b` reasoning 모델 content 처리 | ✅ 완료 (`66ee15d`) |

자세한 단계별 진행 사항은 `MODIFIED.md` 참고.

---

## 📜 라이선스 및 원본 표시

- **Apache License 2.0** ([LICENSE](LICENSE) 참고)
- **원본 저작자 표시**: © 2023 Stanford University. Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). ["Generative Agents: Interactive Simulacra of Human Behavior."](https://arxiv.org/abs/2304.03442) In Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology.
- **변경 사항**: [MODIFIED.md](MODIFIED.md) 참고

---

## 🔗 레포지토리 구조

```
generative-agents-kr/
├── reverie/backend_server/         # 시뮬레이션 서버 (Phase 1-3)
│   ├── persona/
│   │   ├── prompt_template/
│   │   │   ├── v1/, v2/, v3_ChatGPT/, safety/    # 원본 영문
│   │   │   └── prompt_template_kr/...             # 한국어 (자동 생성)
│   │   ├── persona_seed_kr.py                    # 한국어 3명 페르소나
│   │   └── refresh_persona_csv.py                # CSV 자동 갱신
│   ├── gpt_structure.py                          # NIM 백엔드 (한국어 라우팅)
│   ├── reverie.py                                # 시뮬레이션 메인
│   └── test_kr_sim.py                            # Phase 5 검증 도구
│
├── environment/frontend_server/    # Django 시각화 (Phase 4 한글화)
│   └── templates/
│       ├── base.html                            # 한글 헤더/푸터
│       ├── landing/landing.html                 # 환경 안내
│       ├── home/home.html                       # 시뮬 메인
│       ├── demo/demo.html                       # 데모 뷰
│       ├── home/error_start_backend.html        # 백엔드 미연결 안내
│       └── persona_state/persona_state.html     # 페르소나 상세 (28+ 라벨)
│
├── README.md                                       # 이 파일
├── MODIFIED.md                                     # Apache 2.0 §4(a) 준수
└── LICENSE                                         # 원본 라이선스
```

---

## 🚧 향후 확장 (옵션)

- [ ] 페르소나 3명 → 25명 확장 (원본 `March20_the_ville_n25` 시나리오 한국화)
- [ ] 음성 (TTS) — 한국어 음성 합성 통합
- [ ] 공간 자산 (맵/스프라이트) 한국어 라벨링
- [ ] 비동기 + 멀티시뮬레이션 안정화

---

**Built with ❤️ by sigco3111 · Powered by NVIDIA NIM (gpt-oss-120b)**
