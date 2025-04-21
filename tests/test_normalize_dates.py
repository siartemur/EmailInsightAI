from app.utils.normalize_dates import normalize_relative_dates
from datetime import datetime

def test_normalize_relative_dates():
    text = "Meeting is tomorrow and this Friday, then next Monday."
    ref_date = datetime(2025, 4, 21)

    result = normalize_relative_dates(text, ref_date)
    expected = "Meeting is 2025-04-22 and 2025-04-25, then 2025-04-28."

    assert result == expected