from sqlalchemy.orm import Session
from app.database.email_models import Email, QAPair

def insert_email(db: Session, content: str) -> int:
    new_email = Email(content=content)
    db.add(new_email)
    db.commit()
    db.refresh(new_email)
    return new_email.id

def insert_qa(db: Session, email_id: int, question: str, answer: str):
    qa = QAPair(email_id=email_id, question=question, answer=answer)
    db.add(qa)
    db.commit()
