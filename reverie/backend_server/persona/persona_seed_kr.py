"""
File: persona_seed_kr.py
용도: 한국어 페르소나 시드 (CSV whisper + LLM이 bootstrap_memory 생성에 사용)

시나리오: '한강 자전거 동호회와 한강뷰 카페'
원본 english: agent_history_init_n3.csv (Isabella/Maria/Klaus)
"""

PERSONAS_KR_N3 = [
    {
        "name": "이서연",
        "first_name": "서연",
        "last_name": "이",
        "age": 27,
        "occupation": "도시계획 석사과정",
        "personality_traits": ["호기심 많음", "외향적", "세심함"],
        "speech_style": "친근한 반말, 가끔 의문사 사용",
        "interests": ["한강 자전거", "도시계획", "카페 탐방"],
        "habits": ["주 3회 자전거 출퇴근", "거의 매일 도서관", "한강뷰 카페 단골"],
        "background": (
            "서울 출신. 한강변 자전거 동호회에서 활동 중이며, "
            "도시계획 석사 논문 '한강변 공공공간 활성화 방안'을 작성 중."
        ),
        "relationships": [
            ("김민준", "짝사랑 (본인만 모름)", 2, "years"),
            ("김민준", "같은 대학 도서관 친구", 2, "years"),
            ("박지우", "한강 자전거 동호회 친구", 3, "years"),
            ("박지우", "가장 친한 친구", None, None),
        ],
        "secret": "김민준에게 짝사랑함 (아직 고백 안 함)",
    },
    {
        "name": "김민준",
        "first_name": "민준",
        "last_name": "김",
        "age": 26,
        "occupation": "데이터 사이언스 석사 / 카페 아르바이트",
        "personality_traits": ["내향적", "꼼꼼함", "창의적"],
        "speech_style": "정중한 존댓말, 데이터/수사 표현 선호",
        "interests": ["데이터 분석", "자전거", "커피 메뉴 개발"],
        "habits": ["거의 매일 도서관", "주말 카페 알바", "한강 자전거 주 2회"],
        "background": (
            "부산 출신. 데이터 사이언스 석사과정 중이며, "
            "한강뷰 카페에서 신메뉴 개발 아르바이트 중. "
            "자전거 동호회 회원으로 활동."
        ),
        "relationships": [
            ("이서연", "짝사랑", 2, "years"),
            ("이서연", "도서관 같은 자리 단골", 2, "years"),
            ("박지우", "자전거 동호회 친구", 2, "years"),
            ("박지우", "자전거 코스 동반자", None, None),
        ],
        "secret": "이서연에게 고백하고 싶지만 타이밍을 못 잡음",
    },
    {
        "name": "박지우",
        "first_name": "지우",
        "last_name": "박",
        "age": 28,
        "occupation": "마케팅 매니저 / 자전거 동호회 운영진",
        "personality_traits": ["외향적", "분위기 메이커", "운동 좋아함"],
        "speech_style": "활발한 반말, 유머러스, 이모티콘 자주 사용",
        "interests": ["자전거", "마케팅", "건강한 요리"],
        "habits": ["아침 조깅", "도시락 싸서 자전거", "동호회 운영"],
        "background": (
            "대구 출신. 마케팅 매니저로 직장 다니면서 "
            "한강 자전거 동호회 운영진으로 활동. "
            "주 3회 한강 자전거 코스 함께 탐."
        ),
        "relationships": [
            ("이서연", "가장 친한 친구", 3, "years"),
            ("이서연", "자전거 동호회 공동 운영", 2, "years"),
            ("김민준", "자전거 동호회 친구", 2, "years"),
            ("김민준", "자전거 동반자", None, None),
        ],
        "secret": "이서연과 김민준이 서로 좋아한다는 걸 본인만 알고 있음",
    },
]


def to_whisper_csv(persona):
    """페르소나 dict → CSV whisper 문자열.

    구조: 비밀 (1개) + 관계 (각 1개) + 일상 루틴
    각 관계에서 비밀과 중복되는 항목은 스킵.
    한국어 조사 자동 처리: 받침 있으면 은/이, 없으면 는/가.
    """
    def josa_with(particle_eul, particle_neun, name):
        """한국어 조사 자동 선택. 받침 유무에 따라 은/는, 이/가 등 결정."""
        last_char = name[-1]
        if not (ord("가") <= ord(last_char) <= ord("힣")):
            return f"{name}{particle_eul}"  # 한글이 아니면 그대로
        has_jongseong = (ord(last_char) - ord("가")) % 28 != 0

        if has_jongseong:
            if particle_neun == "는": return f"{name}은"
            if particle_neun == "가": return f"{name}이"
            if particle_neun == "와": return f"{name}과"
            if particle_neun == "를": return f"{name}을"
            if particle_neun == "나": return f"{name}이나"
        else:
            if particle_neun == "는": return f"{name}는"
            if particle_neun == "가": return f"{name}가"
            if particle_neun == "와": return f"{name}와"
            if particle_neun == "를": return f"{name}를"
            if particle_neun == "나": return f"{name}나"
        return f"{name}{particle_neun}"

    parts = []
    # 비밀 (이미 자연스러운 한국어 문장으로 작성되어 있음)
    parts.append(f"이것은 매우 중요합니다 -- {persona['secret']}")

    # 관계 — 비밀에 표현된 type은 스킵하고, 그 외 type 중복 없이
    seen_types = set()
    import re as _re
    secret_text = persona.get("secret", "")

    for rel_name, rel_type, years, unit in persona["relationships"]:
        if rel_type in seen_types:
            continue
        # 관계 type 핵심 단어가 비밀 텍스트에 들어있으면 스킵 (substring)
        # "짝사랑"이 secret "짝사랑함"에 포함 → 중복으로 판단 → 스킵
        # "고백"이 secret "고백하고"에 포함 → 스킵
        skip = False
        for word in _re.findall(r'[가-힣]+', rel_type):
            if len(word) >= 2 and word in secret_text:
                skip = True
                break
        if skip:
            continue
        seen_types.add(rel_type)

        name_p = josa_with("은", "는", rel_name)
        if years:
            parts.append(f"당신과 {name_p} {years}년 넘게 {rel_type}입니다")
        else:
            parts.append(f"당신과 {name_p} {rel_type}입니다")

    # 일상 루틴
    parts.append(
        f"당신의 일상: {'; '.join(persona['habits'])}"
    )
    return "; ".join(parts)


# 시뮬레이션 환경 시드 (영문 맵이지만 한국어 에이전트 이름 매핑)
SCENARIO_KO = {
    "world_name": "한강 자전거 동호회와 한강뷰 카페",
    "places": {
        "Hobbs Cafe": "한강뷰 카페",
        "Library": "도서관",
        "Park": "한강 자전거 코스",
        "Dorm": "기숙사",
        "School": "오크힐 대학",
    },
    "agent_history_csv": "agent_history_init_kr_n3.csv",
}


if __name__ == "__main__":
    import json
    for p in PERSONAS_KR_N3:
        print(f"=== {p['name']} ===")
        print(f"  직업: {p['occupation']}")
        print(f"  외모: {p['personality_traits']}")
        print(f"  비밀: {p['secret']}")
        print(f"  whisper: {to_whisper_csv(p)[:100]}...")
        print()
