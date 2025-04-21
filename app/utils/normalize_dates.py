# NOTE:
# The current seed data does not include explicit timestamps or date metadata,
# so date normalization (e.g., converting "tomorrow" to an exact date) has been temporarily skipped.
# However, applying proper date normalization is essential for ensuring high-quality training data,
# and it should be implemented in production scenarios or with real datasets.

from datetime import datetime, timedelta
import re

def normalize_relative_dates(text: str, reference_date: datetime = None) -> str:
    if reference_date is None:
        reference_date = datetime.today()

    def replace(pattern: str, replacement: str) -> str:
        return re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    text = replace(r"\btomorrow\b", (reference_date + timedelta(days=1)).strftime("%Y-%m-%d"))
    text = replace(r"\btoday\b", reference_date.strftime("%Y-%m-%d"))

    # this Friday → haftanın 4. günü (0=Mon)
    days_to_friday = (4 - reference_date.weekday()) % 7
    friday_date = (reference_date + timedelta(days=days_to_friday)).strftime("%Y-%m-%d")
    text = replace(r"\bthis\s+Friday\b", friday_date)

    # next Monday → haftanın 0. günü, bir sonraki
    days_to_next_monday = ((0 - reference_date.weekday() + 7) % 7) + 7
    monday_date = (reference_date + timedelta(days=days_to_next_monday)).strftime("%Y-%m-%d")
    text = replace(r"\bnext\s+Monday\b", monday_date)

    return text
