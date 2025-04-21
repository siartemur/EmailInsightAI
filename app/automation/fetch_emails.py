from pathlib import Path
from app.config.config_loader import load_config

def fetch_unread_emails() -> list[str]:
    config = load_config()
    seed_path = Path(config["email"]["seed_path"])

    emails = []
    for file in seed_path.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                emails.append(content)
    return emails