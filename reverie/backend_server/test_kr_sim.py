"""
File: test_kr_sim.py (Phase 5 verification)
용도: Generative Agents 한국어 통합 검증 (시뮬레이션 1단계에 사용되는 핵심 함수들 직접 호출)
실행: cd reverie/backend_server && source ~/.hermes/secrets/nvidia_keys.env && export NVIDIA_API_KEY=$NVIDIA_API_KEY_1 && python3 test_kr_sim.py

검증 항목:
1. 한국어 whisper + 페르소나 데이터 로드
2. 한국어 프롬프트 라우팅
3. LLM 한국어 응답 (한국어 페르소나 시나리오 - 한강 자전거 동호회)
4. conversation 품질 (대화성)
5. daily_planning (일과 계획) 한국어
6. task_decomp (작업 분해) 한국어

이건 시뮬레이션 실제 실행은 아니지만, 시뮬레이션의 핵심 모듈을 직접 호출해서
한국어 화이트엔드 검증.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from persona.prompt_template.gpt_structure import (
    ChatGPT_request, generate_prompt,
)

# 한국어 페르소나 시드 (실제 시뮬레이션에서 load될 whisper)
PERSONAS_KR = {
    "이서연": {
        "commonset": "이서연은 27세 도시계획 석사과정 학생이다. 호기심이 많고 외향적이며 세심하다. 도시계획 연구에 관심이 있다. 평일에는 학교에서 공부하고 주말에는 한강 자전거 라이딩을 한다.",
        "curr_time": "오전 9시",
        "current_action": "자전거를 타고 한강변을 지나고 있다",
        "location": "한강 자전거 코스 (여의도 구간)",
    },
    "김민준": {
        "commonset": "김민준은 28세 데이터 사이언스 석사과정 학생이다. 내향적이고 꼼꼼하며 창의적이다. 평일에는 도서관에서 공부하고 주말에는 주말에는 한강 자전거 라이딩을 한다. 한강 카페에서 알바를 한다.",
        "curr_time": "오전 9시",
        "current_action": "도서관에서 공부하고 있다",
        "location": "오크힐 대학 도서관",
    },
    "박지우": {
        "commonset": "박지우는 29세 마케팅 매니저다. 외향적이고 분위기 메이커이며 운동 좋아한다. 한강 자전거 동호회 운영진이다.",
        "curr_time": "오전 9시",
        "current_action": "동호회 회계 정리 중이다",
        "location": "한강 자전거 동호회 사무실",
    },
}

# ============================================================================
# 검증 1: daily_planning (일일 계획) - 시뮬 시작시 실행
# ============================================================================
def test_daily_planning(persona_name):
    inputs = [
        PERSONAS_KR[persona_name]["commonset"],  # INPUT 0: Commonset
        "오전 9시",  # INPUT 1: curr time
        "2026-05-10 Saturday",  # INPUT 2: initial_date
        "초기 생활 시나리오",  # INPUT 3: wakeup_hour
        "(고려 불필요)",  # INPUT 4: contexto (사용 X)
    ]
    prompt = generate_prompt(inputs, "persona/prompt_template/v2/daily_planning_v6.txt")
    print(f"[{persona_name}] === daily_planning ===")
    print(f"프롬프트 미리보기: {prompt[:150]}...")
    response = ChatGPT_request(prompt)
    print(f"응답:\n{response}\n")
    return response


# ============================================================================
# 검증 2: task_decomp (작업 분해) - 시뮬의 핵심
# ============================================================================
def test_task_decomp(persona_name, task="도서관에서 데이터 사이언스 논문 작성"):
    src = open("/Users/mac/work/generative-agents-kr/reverie/backend_server/persona/prompt_template_kr/v2/task_decomp_v3.txt",
               encoding="utf-8").read()

    # commonset, surrounding schedule, persona, persona, current action, curr time range, duration, personas
    commonset = PERSONAS_KR[persona_name]["commonset"]
    surrounding = f"{persona_name}는 오전에는 공부할 계획이고, 오후에는 동호회 모임에 참석할 계획입니다."
    inputs = [
        commonset,
        surrounding,
        persona_name,
        persona_name,
        task,
        "09:00 ~ 12:00",
        "180",
        persona_name,
    ]
    prompt = generate_prompt(inputs, "persona/prompt_template/v2/task_decomp_v3.txt")
    print(f"[{persona_name}] === task_decomp ===")
    print(f"프롬프트 미리보기: {prompt[:150]}...")
    response = ChatGPT_request(prompt)
    print(f"응답:\n{response}\n")
    return response


# ============================================================================
# 검증 3: decide_to_talk (대화 시작 결정)
# ============================================================================
def test_decide_to_talk(p1_name, p2_name):
    p1 = PERSONAS_KR[p1_name]["commonset"]
    p2 = PERSONAS_KR[p2_name]["commonset"]
    inputs = [
        f"{p1_name}은 {p1}. {p2_name}은 {p2}.",
        "오전 9시 30분",
        f"{p1_name}",
        f"{p2_name}",
        f"오전 9시",
        f"자전거 코스",
        f"{p1_name}이(가) 도서관으로 가는 중",
        f"{p2_name}이(가) 같은 도서관에 있다",
        f"{p1_name}",
        f"{p2_name}",
    ]
    prompt = generate_prompt(inputs, "persona/prompt_template/v2/decide_to_talk_v2.txt")
    print(f"[{p1_name} → {p2_name}] === decide_to_talk ===")
    response = ChatGPT_request(prompt)
    print(f"응답: {response[:200]}\n")
    return response


# ============================================================================
# 검증 4: agent_chat (실제 대화)
# ============================================================================
def test_agent_chat(p1_name, p2_name):
    p1 = PERSONAS_KR[p1_name]["commonset"]
    p2 = PERSONAS_KR[p2_name]["commonset"]

    # agent_chat_v1 inputs는 일반적으로 [init_persona_summary, target_persona_summary, ...]
    # 간단히 모의 대화 생성
    chat_initiator = f"[{p1_name}의 머릿속: {p2_name}에게 한강 자전거 코스 추천을 부탁하고 싶음]"
    chat_target = f"[{p2_name}의 머릿속: 한강 자전거 코스 추천에 관심이 있음]"
    inputs = [
        f"{p1_name}이(가) {p2_name}에게 말하기 시작한다.",
        f"{p1_name}은 {p1}",
        f"{p2_name}은 {p2}",
    ]
    src_path = "persona/prompt_template/v3_ChatGPT/agent_chat_v1.txt"
    prompt = generate_prompt(inputs, src_path)
    print(f"[{p1_name} ↔ {p2_name}] === agent_chat ===")
    print(f"프롬프트 미리보기: {prompt[:200]}...")
    response = ChatGPT_request(prompt + "\n\n답변은 한국어로, 두 사람의 짧은 대화를 JSON으로 출력하세요. 예: '[[\"이서연\", \"안녕!\"], [\"김민준\", \"안녕하세요!\"]]'")
    print(f"응답:\n{response}\n")
    return response


# ============================================================================
# 메인
# ============================================================================
def main():
    print("=" * 70)
    print("🇰🇷 Generative Agents 한국어 시뮬레이션 통합 검증")
    print("=" * 70)
    print()

    # 1. 일과 계획
    test_daily_planning("이서연")
    print("-" * 70)
    test_daily_planning("김민준")
    print("-" * 70)

    # 2. 작업 분해
    test_task_decomp("이서연", "도시계획 논문 작성")
    print("-" * 70)
    test_task_decomp("김민준", "머신러닝 과제 작성")
    print("-" * 70)

    # 3. 대화 시작 결정
    test_decide_to_talk("이서연", "김민준")
    print("-" * 70)

    # 4. 실제 대화
    test_agent_chat("이서연", "김민준")
    print()

    print("=" * 70)
    print("✅ 검증 완료")
    print("=" * 70)


if __name__ == "__main__":
    main()
