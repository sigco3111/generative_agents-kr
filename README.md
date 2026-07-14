# 🏘️ Generative Agents 한국어판 (NIM 백엔드)

> **원본**: [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) · **라이선스**: Apache 2.0
>
> **본 fork의 변경점**: LLM 백엔드를 OpenAI → **NVIDIA NIM** 으로 교체, 한국어 환경 최적화

<p align="center">
  <img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>

이 저장소는 Stanford의 ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442) 논문을 한국어 환경에서 재현하기 위한 fork입니다.

**주요 차이점 (원본 대비)**:
- 🤖 **LLM**: OpenAI GPT-3.5/4 → **NVIDIA NIM `openai/gpt-oss-120b`** (120B reasoning)
- 🧠 **임베딩**: OpenAI ada-002 → **NIM `nvidia/llama-nemotron-embed-1b-v2`** (2048d asymmetric)
- 🇰🇷 **한국어**: 페르소나 시드 + 프롬프트 + UI 한글화 (진행 중)
- 🛡️ **부정 가드**: 한국어 "~않다" 검색 오류 보정

> ⚠️ **현재 상태**: Phase 1 (LLM 백엔드 교체) 완료. 한국어 페르소나/프롬프트는 점진 진행.

---

## 📋 사전 요구사항

- Python 3.9+
- NVIDIA NIM API 키 ([build.nvidia.com](https://build.nvidia.com)에서 무료 발급)
- (선택) 메모리 4GB+ — 임베딩 차원이 2048이고 에이전트 25명 × 메모리 1000개 시 약 200MB

## 🚀 설치

```bash
# 1. 클론
git clone https://github.com/sigco3111/generative_agents-kr.git
cd generative_agents-kr

# 2. 의존성 설치
pip install -r requirements.txt
# python-dotenv 사용 시 (선택):
pip install python-dotenv

# 3. NIM API 키 설정
export NVIDIA_API_KEY="nvapi-..."

# 4. utils.py 확인 (자동 환경변수 로드)
python3 reverie/backend_server/utils.py  # config_check
```

## ✅ LLM 백엔드 self-test

```bash
cd reverie/backend_server/persona/prompt_template
python3 gpt_structure.py
```

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

## 🎮 시뮬레이션 실행

```bash
# 1. 환경 서버 (Django)
cd environment/frontend_server
python manage.py runserver
# → http://localhost:8000 접속

# 2. 시뮬레이션 서버 (별도 터미널)
cd reverie/backend_server
python reverie.py
# → "Enter name of forked simulation:" 입력
# → "Enter option:" → run 100
```

자세한 원본 실행 가이드는 [원본 README](https://github.com/joonspk-research/generative_agents#readme) 참고.

## 🛠️ 주요 API

### 비대칭 임베딩

```python
from gpt_structure import get_passage_embedding, get_query_embedding

# 메모리 저장 시
p_emb = get_passage_embedding("이서연은 카페에서 커피를 마신다")

# 메모리 검색 시
q_emb = get_query_embedding("이서연이 마신 음료는?")
```

### Retrieval 점수 (부정 가드 포함)

```python
from gpt_structure import score_memory

score = score_memory(
    query_text="이서연이 마신 음료는?",
    memory_text="이서연은 카페에서 커피를 마시지 않았다"
)
# 부정 가드 자동 적용 → 0.057 (낮음, 정확한 retrieval)
```

## 📜 라이선스 및 원본 표시

- **Apache License 2.0** ([LICENSE](LICENSE) 참고)
- **원본 저작자 표시**: © 2023 Stanford University. Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative Agents: Interactive Simulacra of Human Behavior.
- **변경 사항**: [MODIFIED.md](MODIFIED.md) 참고

## 🚧 로드맵

- [x] Phase 1: LLM 백엔드 (NIM) 교체
- [x] Phase 1.5: 비대칭 임베딩 + 부정 가드
- [ ] Phase 2: 페르소나 시드 한글화 (3명 → 25명)
- [ ] Phase 3: 프롬프트 한국어 번역 (50+ 파일)
- [ ] Phase 4: Django UI 한글화
- [ ] Phase 5: 한국 시나리오 시뮬레이션 검증

---

**Built with ❤️ by sigco3111 · Powered by NVIDIA NIM**
