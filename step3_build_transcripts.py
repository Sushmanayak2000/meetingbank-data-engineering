import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEETINGBANK_JSON_PATH = os.path.join(BASE_DIR, "Data", "MeetingBank.json")

TARGET_CITIES = ["BostonCC", "SeattleCityCouncil"]

def build_transcript_features():
    with open(MEETINGBANK_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    processed_meetings = []

    for meeting_id, meeting_data in data.items():

        city = meeting_id.split("_")[0]

        # Step 2 filter (reuse)
        if city not in TARGET_CITIES:
            continue

        item_info = meeting_data.get("itemInfo", {})

        full_text = []
        speakers = set()

        for item in item_info.values():
            transcripts = item.get("transcripts", [])

            for segment in transcripts:
                text = segment.get("text", "").strip()
                speaker = segment.get("speaker")

                if text:
                    full_text.append(text)

                if speaker is not None:
                    speakers.add(speaker)

        full_transcript_text = " ".join(full_text)
        transcript_word_count = len(full_transcript_text.split())
        speaker_count = len(speakers)

        processed_meetings.append({
            "meeting_id": meeting_id,
            "city": city,
            "transcript_word_count": transcript_word_count,
            "speaker_count": speaker_count,
            "full_transcript_text": full_transcript_text
        })

    return processed_meetings


if __name__ == "__main__":
    meetings = build_transcript_features()

    print("Total processed meetings:", len(meetings))
    print("\nFirst 5 Records:")
    for m in meetings[:5]:
        print("Meeting ID:", m["meeting_id"])
        print("City:", m["city"])
        print("Word count:", m["transcript_word_count"])
        print("Speaker count:", m["speaker_count"])
        print("Transcript preview:", m["full_transcript_text"][:200], "...\n")

        print("\nLast 5 Records:")
    for m in meetings[-5:]:
        print("Meeting ID:", m["meeting_id"])
        print("City:", m["city"])
        print("Word count:", m["transcript_word_count"])
        print("Speaker count:", m["speaker_count"])
        print("Transcript preview:", m["full_transcript_text"][:200], "...\n")





