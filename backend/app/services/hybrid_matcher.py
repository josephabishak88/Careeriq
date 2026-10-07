def calculate_hybrid_score(
    skill_match_percentage: float,
    semantic_similarity: float,
    experience_score: float,
    seniority_score: float
) -> dict:

    skill_score = max(
        0.0,
        min(100.0, skill_match_percentage)
    )

    semantic_score = (
        max(
            0.0,
            min(1.0, semantic_similarity)
        ) * 100
    )

    experience_score = max(
        0.0,
        min(100.0, experience_score)
    )

    seniority_score = max(
        0.0,
        min(100.0, seniority_score)
    )

    # Initial CareerIQ ranking weights
    skill_weight = 0.50
    semantic_weight = 0.25
    experience_weight = 0.15
    seniority_weight = 0.10

    final_score = (
        skill_weight * skill_score
        + semantic_weight * semantic_score
        + experience_weight * experience_score
        + seniority_weight * seniority_score
    )

    return {
        "skill_score": round(skill_score, 2),
        "semantic_score": round(semantic_score, 2),
        "experience_score": round(experience_score, 2),
        "seniority_score": round(seniority_score, 2),
        "final_score": round(final_score, 2)
    }