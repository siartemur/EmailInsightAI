import os
import openai
from dotenv import load_dotenv
from app.config.config_loader import load_config

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

config = load_config()


def generate_qa_from_email(email_text: str, model: str = None) -> dict:
    if not email_text.strip():
        return {"error": "Email text is empty."}

    selected_model = model or config["openai"].get("model", "gpt-4")
    temperature = config["openai"].get("temperature", 0.5)
    max_tokens = config["openai"].get("max_tokens", 300)

    prompt = [
        {"role": "system", "content": "You are an AI assistant that generates a meaningful question and its answer from an email."},
        {"role": "user", "content": f"Email:\n{email_text.strip()}\n\nExtract one clear and relevant question with its answer.\nFormat:\nQuestion: ...\nAnswer: ..."}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=selected_model,
            messages=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        content = response['choices'][0]['message']['content']
        return {"result": content}
    except Exception as e:
        return {"error": str(e)}