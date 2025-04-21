from pathlib import Path
from app.core.question_gen import generate_qa_from_email
from app.database.email_repository import insert_email, insert_qa
from app.database.db_connection import SessionLocal
from app.config.config_loader import load_config

config = load_config()
EMAIL_FOLDER = Path(config["email"].get("seed_path", "app/data/seed_mails"))

def process_all_emails():
    db = SessionLocal()
    try:
        for email_file in EMAIL_FOLDER.glob("*.txt"):
            with open(email_file, "r", encoding="utf-8") as f:
                content = f.read().strip()

            if not content:
                print(f"⚠️ Boş içerik atlandı: {email_file.name}")
                continue

            email_id = insert_email(db, content)
            result = generate_qa_from_email(content)

            if "result" in result:
                lines = result["result"].split("\n")
                question = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("question:")), "")
                answer = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("answer:")), "")
                insert_qa(db, email_id, question, answer)
                print(f"✅ İşlendi: {email_file.name}")
            else:
                print(f"❌ Hata ({email_file.name}): {result.get('error')}")
    finally:
        db.close()

if __name__ == "__main__":
    process_all_emails()