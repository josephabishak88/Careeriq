import re


def extract_years(text: str) -> float | None:

    if not text:
        return None

    text = text.lower()

    patterns = [
        r"(\d+(?:\.\d+)?)\s*\+\s*years",
        r"(\d+(?:\.\d+)?)\s*or more\s*years",
        r"minimum\s*(?:of\s*)?(\d+(?:\.\d+)?)\s*years",
        r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*years"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:
            return float(match.group(1))

    return None


def calculate_experience_fit(
    candidate_years: float,
    job_experience_level: str | None
) -> dict:

    if not job_experience_level:

        return {
            "candidate_years": candidate_years,
            "required_years": None,
            "experience_score": 50.0,
            "experience_status": "Not specified"
        }

    required_years = extract_years(
        job_experience_level
    )

    if required_years is None:

        return {
            "candidate_years": candidate_years,
            "required_years": None,
            "experience_score": 50.0,
            "experience_status": "Not specified"
        }

    if candidate_years >= required_years:

        score = 100.0
        status = "Meets experience requirement"

    else:

        score = (
            candidate_years
            / required_years
        ) * 100

        score = max(
            0.0,
            min(100.0, score)
        )

        status = "Below experience requirement"

    return {
        "candidate_years": candidate_years,
        "required_years": required_years,
        "experience_score": round(score, 2),
        "experience_status": status
    }