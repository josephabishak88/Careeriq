from app.models.profile import CandidateProfile


# Common skill aliases
SKILL_ALIASES = {
    "ml": "Machine Learning",
    "machine learning": "Machine Learning",
    "machine-learning": "Machine Learning",

    "ai": "Artificial Intelligence",
    "artificial intelligence": "Artificial Intelligence",

    "genai": "Generative AI",
    "gen ai": "Generative AI",
    "generative ai": "Generative AI",

    "fast api": "FastAPI",
    "fastapi": "FastAPI",

    "streamlit": "Streamlit",

    "python 3": "Python",
    "python3": "Python",
    "python": "Python",

    "scikit learn": "Scikit-learn",
    "scikit-learn": "Scikit-learn",
    "sklearn": "Scikit-learn",

    "xgboost": "XGBoost",

    "natural language processing": "NLP",
    "nlp": "NLP",

    "computer vision": "Computer Vision",
    "cv": "Computer Vision",
}


def normalize_skill(skill: str) -> str:
    """
    Convert a skill into its canonical name.
    """

    cleaned = skill.strip().lower()

    if cleaned in SKILL_ALIASES:
        return SKILL_ALIASES[cleaned]

    # Basic formatting for unknown skills
    return skill.strip()


def normalize_skills(skills: list[str]) -> list[str]:
    """
    Normalize skills and remove duplicates.
    """

    normalized = []

    for skill in skills:
        if not skill or not skill.strip():
            continue

        canonical = normalize_skill(skill)

        if canonical not in normalized:
            normalized.append(canonical)

    return normalized


def normalize_candidate_profile(
    profile: CandidateProfile
) -> CandidateProfile:
    """
    Normalize the candidate's skills while
    keeping the rest of the profile unchanged.
    """

    profile.skills = normalize_skills(profile.skills)

    return profile