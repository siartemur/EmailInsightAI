import os
import csv
import json
from app.config.config_loader import load_config
from app.database.db_connection import SessionLocal
from app.database.email_models import Email

config = load_config()
OUTPUT_DIR = config["email"]["output_path"]
JSON_PATH = os.path.join(OUTPUT_DIR, "qa_results.json")
CSV_PATH = os.path.join(OUTPUT_DIR, "qa_results.csv")

def export_to_json_and_csv():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    db = SessionLocal()

    try:
        all_data = []
        emails = db.query(Email).all()
        for email in emails:
            for qa in email.qa_pairs:
                all_data.append({
                    "email": email.content,
                    "question": qa.question,
                    "answer": qa.answer
                })

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)

        with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["email", "question", "answer"])
            writer.writeheader()
            writer.writerows(all_data)

        print(f"✅ JSON ve CSV dışa aktarıldı: {JSON_PATH}, {CSV_PATH}")
    finally:
        db.close()

if __name__ == "__main__":
    export_to_json_and_csv()