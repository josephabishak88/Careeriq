import re
from datetime import datetime


MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def calculate_candidate_years(experience: list) -> float:
    """
    Calculate approximate total professional experience.

    Supports:
    - "2 years"
    - "6 months"
    - "June 2026 – July 2026"
    - "June 2025 - January 2026"
    """

    total_months = 0.0

    for item in experience:

        duration = getattr(item, "duration", None)

        if not duration:
            continue

        text = str(duration).strip().lower()

        # Normalize different dash characters
        text = text.replace("–", "-")
        text = text.replace("—", "-")

        print(f"[EXPERIENCE DEBUG] Duration detected: {text}")

        # --------------------------------------------------
        # 1. Explicit years
        # Example: "2 years"
        # --------------------------------------------------

        years_match = re.search(
            r"(\d+(?:\.\d+)?)\s*years?",
            text
        )

        if years_match:
            total_months += float(years_match.group(1)) * 12

        # --------------------------------------------------
        # 2. Explicit months
        # Example: "6 months"
        # --------------------------------------------------

        months_match = re.search(
            r"(\d+(?:\.\d+)?)\s*months?",
            text
        )

        if months_match:
            total_months += float(months_match.group(1))

        # --------------------------------------------------
        # 3. Month YYYY - Month YYYY
        # Example:
        # June 2026 - July 2026
        # --------------------------------------------------

        date_range_pattern = (
            r"(january|february|march|april|may|june|july|"
            r"august|september|october|november|december)"
            r"\s+(\d{4})"
            r"\s*-\s*"
            r"(january|february|march|april|may|june|july|"
            r"august|september|october|november|december)"
            r"\s+(\d{4})"
        )

        date_match = re.search(
            date_range_pattern,
            text
        )

        if date_match:

            start_month_name = date_match.group(1)
            start_year = int(date_match.group(2))

            end_month_name = date_match.group(3)
            end_year = int(date_match.group(4))

            start_month = MONTHS[start_month_name]
            end_month = MONTHS[end_month_name]

            start_date = datetime(
                start_year,
                start_month,
                1
            )

            end_date = datetime(
                end_year,
                end_month,
                1
            )

            month_difference = (
                (end_date.year - start_date.year) * 12
                + (end_date.month - start_date.month)
            )

            # Same month should still count as one month
            if month_difference <= 0:
                month_difference = 1

            print(
                "[EXPERIENCE DEBUG] "
                f"Date range = {month_difference} month(s)"
            )

            total_months += month_difference

    years = total_months / 12

    return round(years, 1)


def determine_candidate_seniority(years: float) -> str:

    if years < 1:
        return "entry"

    if years < 2:
        return "junior"

    if years < 4:
        return "mid"

    if years < 7:
        return "senior"

    return "lead"