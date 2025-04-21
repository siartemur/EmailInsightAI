from app.core.question_gen import generate_qa_from_email

if __name__ == "__main__":
    email_text = """
    Hey team, quick update: The client demo has been moved to Wednesday at 2PM.
    Please make sure all UI bugs are resolved before that. Thanks!
    """

    result = generate_qa_from_email(email_text)

    if "error" in result:
        print("❌ Hata:", result["error"])
    else:
        print("✅ Soru-Cevap Çıktısı:\n")
        print(result["result"])
