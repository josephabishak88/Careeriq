import re


SENIORITY_LEVELS = {
    "intern": 0,
    "entry": 1,
    "junior": 1,
    "associate": 1,
    "mid": 2,
    "senior": 3,
    "lead": 4,
    "principal": 5,
    "staff": 5,
    "manager": 4,
    "director": 6,
    "head": 6
}


def detect_seniority(job_title: str) -> str:
    """
    Detect the seniority level explicitly indicated
    by the job title.
    """

    if not job_title:
        return "unknown"

    title = job_title.lower()

    # Senior abbreviation: Sr / Sr.
    if re.search(r"\bsr\.?\b", title):
        return "senior"

    # Check more specific levels first
    levels = [
        "principal",
        "director",
        "manager",
        "staff",
        "senior",
        "lead",
        "associate",
        "junior",
        "intern"
    ]

    for level in levels:
        if re.search(
            rf"\b{re.escape(level)}\b",
            title
        ):
            return level

    # Common entry-level indicators
    if re.search(
        r"\bgraduate\b|\bentry[- ]level\b",
        title
    ):
        return "entry"

    # Mid-level indicators
    if re.search(
        r"\bmid[- ]level\b",
        title
    ):
        return "mid"

    return "unknown"


def calculate_seniority_fit(
    candidate_seniority: str,
    job_seniority: str
) -> dict:

    candidate_level = SENIORITY_LEVELS.get(
        candidate_seniority.lower(),
        1
    )

    job_level = SENIORITY_LEVELS.get(
        job_seniority.lower(),
        None
    )

    # Unknown seniority = neutral score
    if job_level is None:

        return {
            "candidate_seniority": candidate_seniority,
            "job_seniority": job_seniority,
            "seniority_score": 50.0,
            "seniority_status": "Not specified"
        }

    if candidate_level >= job_level:

        score = 100.0
        status = "Seniority level is suitable"

    else:

        difference = job_level - candidate_level

        # Penalize larger seniority gaps
        score = max(
            0.0,
            100.0 - (difference * 25.0)
        )

        status = "Below target seniority"

    return {
        "candidate_seniority": candidate_seniority,
        "job_seniority": job_seniority,
        "seniority_score": round(score, 2),
        "seniority_status": status
    }