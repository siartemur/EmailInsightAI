from app.core.question_gen import generate_qa_from_email

def test_generate_qa_from_email():
    email = "Reminder: Team meeting is Monday 10AM at Room A-202"
    result = generate_qa_from_email(email)

    assert result.get("result") is not None
    assert "Question:" in result["result"]
    assert "Answer:" in result["result"]