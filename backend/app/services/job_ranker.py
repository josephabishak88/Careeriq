from app.services.skill_matcher import calculate_skill_match
from app.services.hybrid_matcher import calculate_hybrid_score
from app.services.experience_matcher import calculate_experience_fit
from app.services.seniority_matcher import (
    detect_seniority,
    calculate_seniority_fit
)


def build_match_explanation(
    skill_result: dict,
    experience_result: dict,
    seniority_result: dict,
    hybrid_result: dict
) -> dict:

    return {
        "overall_match": hybrid_result["final_score"],

        "score_breakdown": {
            "skill_match": hybrid_result["skill_score"],
            "semantic_match": hybrid_result["semantic_score"],
            "experience_match": hybrid_result["experience_score"],
            "seniority_match": hybrid_result["seniority_score"]
        },

        "strengths": [
            f"Matched {len(skill_result['matched_skills'])} required skill(s)."
        ] if skill_result["matched_skills"] else [],

        "matched_skills": skill_result["matched_skills"],

        "skill_gaps": skill_result["missing_skills"],

        "experience_assessment": {
            "status": experience_result["experience_status"],
            "candidate_years": experience_result["candidate_years"],
            "required_years": experience_result["required_years"]
        },

        "seniority_assessment": {
            "status": seniority_result["seniority_status"],
            "candidate_seniority": seniority_result["candidate_seniority"],
            "job_seniority": seniority_result["job_seniority"]
        }
    }


def rank_job(
    candidate_skills: list[str],
    job_required_skills: list[str],
    semantic_similarity: float,
    candidate_years: float,
    candidate_seniority: str,
    job_experience_level: str | None,
    job_title: str
) -> dict:

    # -----------------------------------------
    # 1. Skill matching
    # -----------------------------------------

    skill_result = calculate_skill_match(
        candidate_skills,
        job_required_skills
    )

    # -----------------------------------------
    # 2. Experience matching
    # -----------------------------------------

    experience_result = calculate_experience_fit(
        candidate_years=candidate_years,
        job_experience_level=job_experience_level
    )

    # -----------------------------------------
    # 3. Seniority matching
    # -----------------------------------------

    job_seniority = detect_seniority(
        job_title
    )

    seniority_result = calculate_seniority_fit(
        candidate_seniority=candidate_seniority,
        job_seniority=job_seniority
    )

    # -----------------------------------------
    # 4. Hybrid scoring
    # -----------------------------------------

    hybrid_result = calculate_hybrid_score(
        skill_match_percentage=skill_result["match_percentage"],
        semantic_similarity=semantic_similarity,
        experience_score=experience_result["experience_score"],
        seniority_score=seniority_result["seniority_score"]
    )

    # -----------------------------------------
    # 5. Explainable match result
    # -----------------------------------------

    match_explanation = build_match_explanation(
        skill_result=skill_result,
        experience_result=experience_result,
        seniority_result=seniority_result,
        hybrid_result=hybrid_result
    )

    # -----------------------------------------
    # 6. Final result
    # -----------------------------------------

    return {
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"],

        "skill_score": hybrid_result["skill_score"],
        "semantic_score": hybrid_result["semantic_score"],

        "experience_score": hybrid_result["experience_score"],
        "experience_status": experience_result["experience_status"],

        "seniority_score": hybrid_result["seniority_score"],
        "seniority_status": seniority_result["seniority_status"],

        "job_seniority": job_seniority,
        "candidate_seniority": candidate_seniority,

        "final_score": hybrid_result["final_score"],

        "match_explanation": match_explanation
    }