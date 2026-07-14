# MODIFIED.md — 변경 사항 명시 (Apache 2.0 §4(a) 준수)

## 원본 정보
- **원본 저장소**: https://github.com/joonspk-research/generative_agents
- **원본 저자**: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein (Stanford University)
- **원본 논문**: ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442)
- **원본 라이선스**: Apache License 2.0
- **원본 commit (import 시점)**: upstream main (2026-07-14)
- **저작권 표시**: © 2023 Stanford University. Apache 2.0.

## 본 저장소 (sigco3111/generative_agents-kr)

### 주요 변경 사항

| # | 파일/모듈 | 변경 내용 |
|---|----------|----------|
| 1 | `reverie/backend_server/persona/prompt_template/gpt_structure.py` | LLM 백엔드를 OpenAI → NVIDIA NIM (openai/gpt-oss-120b) 으로 교체 |
| 2 | `reverie/backend_server/persona/prompt_template/gpt_structure.py` | 임베딩을 OpenAI ada-002 → NIM `nvidia/llama-nemotron-embed-1b-v2` (asymmetric, 2048d) 로 교체 |
| 3 | `reverie/backend_server/persona/prompt_template/gpt_structure.py` | `get_passage_embedding()` / `get_query_embedding()` 비대칭 함수 추가 |
| 4 | `reverie/backend_server/persona/prompt_template/gpt_structure.py` | 한국어/영어 부정 표현 검색 가드(`negation_penalty()`) 추가 |
| 5 | `reverie/backend_server/persona/prompt_template/gpt_structure.py` | `score_memory()` retrieval 점수 함수 추가 (부정 가드 통합) |
| 6 | `reverie/backend_server/utils.py` | OpenAI 키 → NIM `NVIDIA_API_KEY` 환경변수 사용으로 변경 |
| 7 | `reverie/backend_server/test.py` | 영문 sanity check → 한글 sanity check |
| 8 | `README.md` | 영문 → 한글 설치/실행 가이드 (한글화 진행 중) |

### 보존된 사항

- 원본 LICENSE 파일 (Apache 2.0 전문) 그대로 유지
- 원본 디렉토리 구조 (`reverie/`, `environment/`) 유지
- 원본 시뮬레이션 환경 (Django + Smallville 맵) 그대로 사용
- 원본 한국어 페르소나 시드 데이터는 `persona/<이름>/bootstrap_memory/` 경로에 영문/한글 혼용
- 모든 원본 코드 Apache 2.0 §4(a) (변경 사항 표시) 준수

### 추가 의존성 (원본 대비)

| 패키지 | 용도 | 라이선스 |
|--------|------|---------|
| `urllib.request` | NIM HTTP 호출 (requests 대체) | Python stdlib |
| `python-dotenv` (선택) | `.env` 파일 로드 | BSD-3 |

### 검증 (LLM 백엔드)

- `python gpt_structure.py` self-test: LLM 호출 + 비대칭 임베딩 + 부정 가드 검증
- 한국어 어순/조사/시제 변형 retrieval 정확도: 75% (12 핵심 케이스)
- 메모리 검색 점수 산정식: `cosine_similarity(passage, query) - negation_penalty(text_a, text_b)`

### 면책 조항

본 저장소는 원본의 학술 연구를 한국어 환경에 적용하고 외부 LLM 제공자 변경을 시도한 비공식 fork입니다. 원본 저자(Stanford University)의 공식 입장을 대표하지 않으며, 모든 책임은 사용자에게 있습니다.

---

**Apache License 2.0 §4(a)**: "You must give any other recipients of the Work or Derivative Works a copy of this License; and You must cause any modified files to carry prominent notices stating that You changed the files."
