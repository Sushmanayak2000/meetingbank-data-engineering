import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "Data", "Processed_Data")
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_JSON_PATH = os.path.join(OUTPUT_DIR, "meeting_summary.json")
MEETINGBANK_JSON_PATH = os.path.join(BASE_DIR, "Data", "MeetingBank.json")

TARGET_CITIES = ["BostonCC", "SeattleCityCouncil"]

def read_and_filter_meetingbank():
    with open(MEETINGBANK_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    meetings = []

    for meeting_id, meeting_data in data.items():

        city = meeting_id.split("_")[0]

        # FILTER: keep only Boston & Seattle
        if city not in TARGET_CITIES:
            continue

        video_duration = meeting_data.get("VideoDuration")

        item_info = meeting_data.get("itemInfo", {})
        item_count = len(item_info)

        total_segments = 0
        for item in item_info.values():
            total_segments += len(item.get("transcripts", []))

        meetings.append({
            "meeting_id": meeting_id,
            "city": city,
            "video_duration_sec": video_duration,
            "item_count": item_count,
            "segment_count": total_segments
        })

    return meetings


if __name__ == "__main__":
    meetings = read_and_filter_meetingbank()

    print("Total Boston & Seattle meetings:", len(meetings))
    print("\nSample records:")
    for m in meetings[:5]:
        print(m)

    # Save filtered data to JSON

    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(meetings, f, indent=2, ensure_ascii=False)

    print(f"\nFile saved at: {OUTPUT_JSON_PATH}")
