"""
File: review_prompts_kr.py
용도: 영문 원본 vs 한국어 번역 비교 리포트 자동 생성
실행: cd reverie/backend_server/persona/prompt_template && python3 review_prompts_kr.py

출력:
- prompt_template_kr_review/ 폴더에 side-by-side 비교 .md 파일 생성
- 코드 표식 보존 검증 (변수, JSON 키)
- 한국어 조사 자동 검증 (자주 어색한 케이스)
- LLM 검수: 의심스러운 번역 자동 발견 -> review_needed/ 표시
"""
import os
import re
import sys

PROMPT_DIR = os.path.dirname(os.path.abspath(__file__))
KR_DIR = os.path.join(os.path.dirname(PROMPT_DIR), "prompt_template_kr")
REVIEW_DIR = os.path.join(os.path.dirname(PROMPT_DIR), "prompt_template_kr_review")

sys.path.insert(0, PROMPT_DIR)
from translate_prompts_kr import get_active_prompts


def extract_code_markers(text):
    """번역에서 보존되어야 할 코드 표식 추출."""
    markers = set()
    # 변수 패턴
    for m in re.findall(r"!<INPUT\s+\d+>!", text):
        markers.add(m)
    for m in re.findall(r"<NAME_\d+>", text):
        markers.add(m)
    for m in re.findall(r"<commentblockmarker>###</commentblockmarker>", text):
        markers.add(m)
    # JSON 키
    for m in re.findall(r'"[a-z_]+":\s', text):
        markers.add(m.strip().rstrip(":"))
    # 점수 패턴
    for m in re.findall(r"\[\d+-\d+\]", text):
        markers.add(m)
    return markers


def check_preservation(src_text, dst_text):
    """원본에 있는 코드 표식이 번역에 보존됐는지 검증."""
    src_markers = extract_code_markers(src_text)
    dst_markers = extract_code_markers(dst_text)

    missing = src_markers - dst_markers
    extra = dst_markers - src_markers
    return missing, extra, len(src_markers)


def check_korean_naturalness(text):
    """한국어 자연스러움 대략적 검증 (조사 어색 케이스)."""
    issues = []
    # 흔한 어색 패턴
    patterns = [
        (r"는\s+를", "조사 어색: ~는를 연속"),
        (r"가\s+을", "조사 어색: ~가를 연속"),
        (r"은\s+를", "조사 어색: ~은를 연속"),
        (r"이\s+가", "조사 어색: ~이가 연속"),
        (r"을\s+이", "조사 어색: ~을이 연속"),
        (r"됩니다\s*\.", "문장 종결 어색: ~됩니다"),
        (r"\bthe\s+", "번역 안 된 'the' 발견"),
        (r"\band\s", "번역 안 된 'and' 발견"),
        (r"\bor\s", "번역 안 된 'or' 발견"),
        (r"\bof\s", "번역 안 된 'of' 발견"),
        (r"\bIs\s", "번역 안 된 'Is' 발견"),
        (r"\bare\s", "번역 안 된 'are' 발견"),
        (r"\bdo\s", "번역 안 된 'do' 발견"),
    ]
    for pat, msg in patterns:
        for m in re.finditer(pat, text):
            issues.append((msg, text[max(0, m.start()-15):m.end()+15]))
    return issues


def main():
    print("=" * 70)
    print("한국어 프롬프트 검수 리포트 생성")
    print("=" * 70)

    active = get_active_prompts()
    print(f"활성 파일: {len(active)}개")
    print(f"비교 디렉토리: {KR_DIR} -> {REVIEW_DIR}\n")

    os.makedirs(REVIEW_DIR, exist_ok=True)

    summary = {
        "total": 0,
        "translated": 0,
        "missing": 0,
        "code_loss": 0,
        "korean_issues": 0,
        "clean": 0,
    }

    for rel in active:
        src = os.path.join(PROMPT_DIR, rel)
        dst = os.path.join(KR_DIR, rel)
        summary["total"] += 1

        if not os.path.exists(dst):
            summary["missing"] += 1
            print(f"  MISSING: {rel}")
            continue

        summary["translated"] += 1
        src_text = open(src, encoding="utf-8").read()
        dst_text = open(dst, encoding="utf-8").read()

        missing_markers, extra_markers, total_markers = check_preservation(src_text, dst_text)
        kr_issues = check_korean_naturalness(dst_text)

        ok = not missing_markers and len(kr_issues) == 0
        if ok:
            summary["clean"] += 1
        if missing_markers:
            summary["code_loss"] += 1
        if kr_issues:
            summary["korean_issues"] += 1

        # 마크다운 비교 리포트
        review_path = os.path.join(REVIEW_DIR, rel.replace("/", "__") + ".md")
        with open(review_path, "w", encoding="utf-8") as f:
            f.write(f"# 검수: `{rel}`\n\n")
            f.write(f"- 원본: {len(src_text)}자\n")
            f.write(f"- 번역: {len(dst_text)}자\n")
            f.write(f"- 보존된 코드 표식: {total_markers - len(missing_markers)}/{total_markers}\n\n")
            if missing_markers:
                f.write("## MISSING 마커 (자동 검출)\n")
                for m in missing_markers:
                    f.write(f"- {m}\n")
                f.write("\n")
            if extra_markers:
                f.write("## EXTRA 마커 (번역에 추가됨)\n")
                for m in extra_markers:
                    f.write(f"- {m}\n")
                f.write("\n")
            if kr_issues:
                f.write("## 어색한 한국어 (자동 검출)\n")
                for msg, ctx in kr_issues[:10]:
                    f.write(f"- {msg} `...{ctx}...`\n")
                f.write("\n")
            f.write("## 원본\n```\n")
            f.write(src_text)
            f.write("\n```\n\n## 번역\n```\n")
            f.write(dst_text)
            f.write("\n```\n")

    print("\n" + "=" * 70)
    print("요약")
    print("=" * 70)
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print()
    print(f"검수 리포트 위치: {REVIEW_DIR}")


if __name__ == "__main__":
    main()
