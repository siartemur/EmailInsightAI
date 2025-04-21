import time
from app.automation.fetch_emails import fetch_unread_emails
from app.automation.process_and_export import process_emails
from app.config.config_loader import load_config

def run_loop():
    config = load_config()
    interval = config["automation"].get("check_interval_seconds", 3600)

    while True:
        print("\n🔄 Yeni e-postalar kontrol ediliyor...")
        emails = fetch_unread_emails()
        if emails:
            print(f"📥 {len(emails)} yeni e-posta bulundu.")
            process_emails(emails)
        else:
            print("📭 Yeni e-posta yok.")

        print(f"⏳ {interval} saniye bekleniyor...\n")
        time.sleep(interval)

if __name__ == "__main__":
    run_loop()
