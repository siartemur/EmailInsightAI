import csv
import json
import os
from app.core.question_gen import generate_qa_from_email
from app.utils.normalize_dates import normalize_relative_dates
from app.config.config_loader import load_config

config = load_config()
OUTPUT_JSON = os.path.join(config["email"]["output_path"], "qa_results.json")
OUTPUT_CSV = os.path.join(config["email"]["output_path"], "qa_results.csv")

def append_to_outputs(email_text: str, question: str, answer: str) -> None:
    os.makedirs(config["email"]["output_path"], exist_ok=True)

    # JSON
    data = []
    if os.path.exists(OUTPUT_JSON):
        with open(OUTPUT_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    data.append({"email": email_text, "question": question, "answer": answer})

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # CSV
    file_exists = os.path.exists(OUTPUT_CSV)
    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "question", "answer"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"email": email_text, "question": question, "answer": answer})

def process_emails(email_list: list[str]) -> None:
    for email_text in email_list:
        normalized_text = normalize_relative_dates(email_text)
        result = generate_qa_from_email(normalized_text)
        if "result" in result:
            lines = result["result"].split("\n")
            question = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("question:")), "")
            answer = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("answer:")), "")
            append_to_outputs(normalized_text, question, answer)
            print("✅ Soru-Cevap eklendi.")
        else:
            print(f"❌ OpenAI hatası: {result.get('error')}")