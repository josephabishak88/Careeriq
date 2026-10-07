from app.services.job_search_ranker import search_and_rank_jobs
from app.services.career_intelligence import generate_career_intelligence
from app.services.career_strategy import generate_career_strategy
from app.services.resume_optimizer import optimize_resume_for_job
from app.services.interview_service import generate_interview_prep
from app.services.candidate_experience import (
    calculate_candidate_years,
    determine_candidate_seniority
)
from app.services.market_intelligence import (
    analyze_job_market,
    compare_candidate_to_market
)


def run_careeriq_pipeline(
    candidate_profile,
    candidate_text: str,
    target_role: str,
    query: str,
    top_k: int = 5
):

    # -----------------------------------------
    # 1. Candidate experience
    # -----------------------------------------

    candidate_years = calculate_candidate_years(
        candidate_profile.experience
    )

    candidate_seniority = determine_candidate_seniority(
        candidate_years
    )

    # -----------------------------------------
    # 2. Search and rank jobs
    # -----------------------------------------

    ranked_jobs = search_and_rank_jobs(
        candidate_skills=candidate_profile.skills,
        candidate_text=candidate_text,
        query=query,
        candidate_years=candidate_years,
        candidate_seniority=candidate_seniority,
        top_k=top_k
    )

    # -----------------------------------------
    # 3. No jobs found
    # -----------------------------------------

    if not ranked_jobs:
        return {
            "target_role": target_role,
            "candidate_years": candidate_years,
            "candidate_seniority": candidate_seniority,
            "jobs": [],
            "top_job": None,
            "career_intelligence": None,
            "career_strategy": None,
            "resume_optimization": None,
            "interview_preparation": None,
            "market_intelligence": None,
            "candidate_market_comparison": None
        }

    # -----------------------------------------
    # 4. Select top-ranked job
    # -----------------------------------------

    top_job = ranked_jobs[0]

    # -----------------------------------------
    # 5. Market Intelligence
    # -----------------------------------------

    market_intelligence = analyze_job_market(
        ranked_jobs
    )

    candidate_market_comparison = compare_candidate_to_market(
        candidate_skills=candidate_profile.skills,
        jobs=ranked_jobs
    )

    # -----------------------------------------
    # 6. Career Intelligence
    # -----------------------------------------

    career_intelligence = generate_career_intelligence(
        candidate_text=candidate_text,
        job_title=top_job["title"],
        company=top_job["company"],
        required_skills=top_job["required_skills"],
        matched_skills=top_job["matched_skills"],
        missing_skills=top_job["missing_skills"],
        skill_score=top_job["skill_score"],
        semantic_score=top_job["semantic_score"],
        final_score=top_job["final_score"]
    )

    # -----------------------------------------
    # 7. Career Strategy
    # -----------------------------------------

    career_strategy = generate_career_strategy(
        candidate_skills=candidate_profile.skills,
        target_role=target_role,
        missing_skills=top_job["missing_skills"],
        career_intelligence=career_intelligence
    )

    # -----------------------------------------
    # 8. Resume Optimization
    # -----------------------------------------

    resume_optimization = optimize_resume_for_job(
        resume_text=candidate_text,
        job_title=top_job["title"],
        company=top_job["company"],
        job_description=top_job.get("description", ""),
        required_skills=top_job["required_skills"],
        missing_skills=top_job["missing_skills"]
    )

    # -----------------------------------------
    # 9. Interview Preparation
    # -----------------------------------------

    interview_preparation = generate_interview_prep(
        candidate_text=candidate_text,
        job_title=top_job["title"],
        company=top_job["company"],
        job_description=top_job.get("description", ""),
        required_skills=top_job["required_skills"],
        missing_skills=top_job["missing_skills"]
    )

    # -----------------------------------------
    # 10. Final CareerIQ result
    # -----------------------------------------

    return {
        "target_role": target_role,

        "candidate_years": candidate_years,

        "candidate_seniority": candidate_seniority,

        "jobs": ranked_jobs,

        "top_job": top_job,

        "career_intelligence": career_intelligence,

        "career_strategy": career_strategy,

        "resume_optimization": resume_optimization,

        "interview_preparation": interview_preparation,

        "market_intelligence": market_intelligence,

        "candidate_market_comparison": candidate_market_comparison
    }