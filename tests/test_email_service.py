# tests/test_email_service.py

import pytest
from app.services.email_service import EmailAnalysisService

service = EmailAnalysisService()

def test_valid_email_analysis():
    email_text = "Hi team, the meeting is tomorrow at 10AM."
    result = service.analyze_email(email_text)

    assert result["success"] is True
    assert "Question:" in result["data"]
    assert "Answer:" in result["data"]

def test_empty_email_analysis():
    email_text = "  "
    result = service.analyze_email(email_text)

    assert result["success"] is False
    assert result["error"] == "Email text is empty."

def test_normalization_applied():
    email_text = "Let’s sync tomorrow and this Friday."
    result = service.analyze_email(email_text)

    assert result["success"] is True
    assert "tomorrow" not in result["normalized_email"].lower()
    assert "friday" not in result["normalized_email"].lower()
