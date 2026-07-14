"""
File: refresh_persona_csv.py
용도: persona_seed_kr.py에서 CSV whisper 자동 생성 → CSV 갱신
실행: cd reverie/backend_server/persona && python3 refresh_persona_csv.py
"""
import csv
import os
from persona_seed_kr import PERSONAS_KR_N3, to_whisper_csv, SCENARIO_KO

OUT_CSV = os.path.join(
    os.path.dirname(__file__), "..", "..", "..",
    "environment", "frontend_server", "static_dirs", "assets", "the_ville",
    "agent_history_init_kr_n3.csv",
)
OUT_CSV = os.path.abspath(OUT_CSV)


def write_csv():
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Whisper"])
        for p in PERSONAS_KR_N3:
            writer.writerow([p["name"], to_whisper_csv(p)])
    print(f"✅ CSV 갱신 완료: {OUT_CSV}")
    print(f"   시나리오: {SCENARIO_KO['world_name']}")
    print(f"   페르소나: {len(PERSONAS_KR_N3)}명")
    for p in PERSONAS_KR_N3:
        print(f"   - {p['name']} ({p['occupation']})")


if __name__ == "__main__":
    write_csv()
