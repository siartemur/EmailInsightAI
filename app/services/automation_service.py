from app.services.email_service import EmailAnalysisService
from app.database.email_repository import insert_email, insert_qa

class EmailAutomationService:
    def __init__(self, db):
        self.db = db
        self.analyzer = EmailAnalysisService()

    def process_email(self, raw_email_text: str):
        result = self.analyzer.analyze_email(raw_email_text)
        if not result["success"]:
            return {"error": result["error"]}

        email_id = insert_email(self.db, result["normalized_email"])
        lines = result["data"].split("\n")
        question = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("question:")), "")
        answer = next((l.split(":", 1)[1].strip() for l in lines if l.lower().startswith("answer:")), "")
        insert_qa(self.db, email_id, question, answer)

        return {"email_id": email_id, "question": question, "answer": answer}
