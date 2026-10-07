from typing import List


# Common aliases → one canonical skill name
SKILL_ALIASES = {
    # Programming
    "python 3": "python",
    "python3": "python",

    "javascript": "javascript",
    "js": "javascript",

    "typescript": "typescript",
    "ts": "typescript",

    "c plus plus": "c++",
    "cpp": "c++",

    # AI / ML
    "ml": "machine learning",
    "machine-learning": "machine learning",

    "ai": "artificial intelligence",

    "genai": "generative ai",
    "gen ai": "generative ai",

    "natural language processing": "nlp",

    "large language models": "llm",
    "large language model": "llm",
    "llms": "llm",

    "retrieval augmented generation": "rag",
    "retrieval-augmented generation": "rag",
    "retrieval augmented": "rag",

    # Frameworks
    "fast api": "fastapi",

    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",

    # ML libraries
    "pytorch": "pytorch",
    "tensorflow": "tensorflow",
    "keras": "keras",

    # Data
    "data analytics": "data analysis",
    "data analysis": "data analysis",

    # Cloud
    "amazon web services": "aws",
    "aws": "aws",

    "google cloud platform": "gcp",
    "google cloud": "gcp",
    "gcp": "gcp",

    "microsoft azure": "azure",
    "azure": "azure",
}


# Technical skills receive higher importance
TECHNICAL_SKILLS = {
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",
    "sql",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "generative ai",
    "llm",
    "rag",
    "nlp",
    "computer vision",
    "data science",
    "data analysis",
    "fastapi",
    "django",
    "flask",
    "pytorch",
    "tensorflow",
    "keras",
    "scikit-learn",
    "xgboost",
    "lightgbm",
    "catboost",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "gcp",
}


def normalize_skill(skill: str) -> str:

    cleaned = skill.strip().lower()

    return SKILL_ALIASES.get(
        cleaned,
        cleaned
    )


def normalize_skills(
    skills: List[str]
) -> List[str]:

    normalized = []

    for skill in skills:

        if not skill or not skill.strip():
            continue

        canonical = normalize_skill(skill)

        if canonical not in normalized:
            normalized.append(canonical)

    return normalized


def calculate_skill_match(
    candidate_skills: List[str],
    required_skills: List[str]
) -> dict:

    candidate_set = set(
        normalize_skills(candidate_skills)
    )

    required_set = set(
        normalize_skills(required_skills)
    )

    if not required_set:

        return {
            "matched_skills": [],
            "missing_skills": [],
            "match_percentage": 0.0
        }

    matched_skills = sorted(
        candidate_set.intersection(
            required_set
        )
    )

    missing_skills = sorted(
        required_set - candidate_set
    )

    technical_required = {
        skill
        for skill in required_set
        if skill in TECHNICAL_SKILLS
    }

    general_required = (
        required_set - technical_required
    )

    technical_matched = (
        candidate_set.intersection(
            technical_required
        )
    )

    general_matched = (
        candidate_set.intersection(
            general_required
        )
    )

    if technical_required and general_required:

        technical_score = (
            len(technical_matched)
            / len(technical_required)
        ) * 100

        general_score = (
            len(general_matched)
            / len(general_required)
        ) * 100

        match_percentage = (
            0.70 * technical_score
            + 0.30 * general_score
        )

    elif technical_required:

        match_percentage = (
            len(technical_matched)
            / len(technical_required)
        ) * 100

    else:

        match_percentage = (
            len(general_matched)
            / len(general_required)
        ) * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(
            match_percentage,
            2
        )
    }