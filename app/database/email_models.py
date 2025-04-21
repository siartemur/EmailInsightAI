from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)

    qa_pairs = relationship("QAPair", back_populates="email")


class QAPair(Base):
    __tablename__ = "qa_pairs"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, ForeignKey("emails.id"))
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    email = relationship("Email", back_populates="qa_pairs")