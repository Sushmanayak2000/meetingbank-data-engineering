import json
from pymongo import MongoClient

MEETINGBANK_JSON_PATH = "/Users/sushma/Documents/SRH Class Notes/Data Engneering/DE_Project/MeetingBank_Dataset/Metadata/MeetingBank.json"
TARGET_CITIES = ["BostonCC", "SeattleCityCouncil"]

print("Connecting to MongoDB...")

client = MongoClient("mongodb://localhost:27017/")
db = client["meetingbank"]
collection = db["raw_meetings"]

print("MongoDB connected.")

def load_mongodb():
    print("Opening JSON file...")
    with open(MEETINGBANK_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("JSON loaded. Total meetings in file:", len(data))

    count = 0

    for meeting_id, meeting_data in data.items():
        city = meeting_id.split("_")[0]

        if city not in TARGET_CITIES:
            continue

        full_text = []
        item_info = meeting_data.get("itemInfo", {})

        for item in item_info.values():
            for seg in item.get("transcripts", []):
                if seg.get("text"):
                    full_text.append(seg["text"])

        document = {
            "_id": meeting_id,
            "city": city,
            "full_transcript_text": " ".join(full_text)
        }

        collection.update_one(
            {"_id": meeting_id},
            {"$set": document},
            upsert=True
        )

        count += 1

    print(f"MongoDB: {count} meetings stored")

if __name__ == "__main__":
    load_mongodb()

