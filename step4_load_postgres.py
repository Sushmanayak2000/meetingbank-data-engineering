import json
import psycopg2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEETINGBANK_JSON_PATH = os.path.join(BASE_DIR, "Data", "MeetingBank.json")

TARGET_CITIES = ["BostonCC", "SeattleCityCouncil"]

conn = psycopg2.connect(dbname="meetingbank")
cur = conn.cursor()

def load_postgres():
    with open(MEETINGBANK_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    for meeting_id, meeting_data in data.items():
        city = meeting_id.split("_")[0]

        if city not in TARGET_CITIES:
            continue

        # insert city
        cur.execute(
            "INSERT INTO dim_city (city_name) VALUES (%s) ON CONFLICT DO NOTHING",
            (city,)
        )

        cur.execute(
            "SELECT city_id FROM dim_city WHERE city_name = %s",
            (city,)
        )
        city_id = cur.fetchone()[0]

        item_info = meeting_data.get("itemInfo", {})
        full_text = []
        speakers = set()

        for item in item_info.values():
            for seg in item.get("transcripts", []):
                if seg.get("text"):
                    full_text.append(seg["text"])
                if seg.get("speaker") is not None:
                    speakers.add(seg["speaker"])

        transcript_word_count = len(" ".join(full_text).split())
        speaker_count = len(speakers)

        cur.execute("""
            INSERT INTO fact_meetings
            (meeting_id, city_id, transcript_word_count, speaker_count)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (meeting_id) DO NOTHING
        """, (meeting_id, city_id, transcript_word_count, speaker_count))

    conn.commit()
    print("PostgreSQL: metrics stored")

if __name__ == "__main__":
    load_postgres()




    
