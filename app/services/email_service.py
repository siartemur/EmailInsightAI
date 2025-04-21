from app.core.question_gen import generate_qa_from_email
from app.utils.normalize_dates import normalize_relative_dates

class EmailAnalysisService:
    def analyze_email(self, email_text: str) -> dict:
        if not email_text.strip():
            return {"success": False, "error": "Email text is empty."}

        normalized_text = normalize_relative_dates(email_text)
        result = generate_qa_from_email(normalized_text)

        if "error" in result:
            return {"success": False, "error": result["error"]}

        return {"success": True, "data": result["result"], "normalized_email": normalized_text}
