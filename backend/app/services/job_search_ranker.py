import json

from sklearn.metrics.pairwise import cosine_similarity

from app.services.vector_store import search_jobs
from app.services.embedding_service import generate_embedding
from app.services.job_ranker import rank_job


def search_and_rank_jobs(
    candidate_skills: list[str],
    candidate_text: str,
    query: str,
    candidate_years: float = 0,
    candidate_seniority: str = "entry",
    top_k: int = 5
):

    # -----------------------------------------
    # 1. Semantic job retrieval
    # -----------------------------------------

    results = search_jobs(
        query=query,
        top_k=top_k
    )

    candidate_embedding = generate_embedding(
        candidate_text
    )

    ranked_jobs = []

    # -----------------------------------------
    # 2. Rank retrieved jobs
    # -----------------------------------------

    for i in range(
        len(results["ids"][0])
    ):

        job_id = results["ids"][0][i]

        metadata = results["metadatas"][0][i]

        document = results["documents"][0][i]

        distance = results["distances"][0][i]

        # -----------------------------------------
        # Required skills
        # -----------------------------------------

        raw_skills = metadata.get(
            "required_skills",
            "[]"
        )

        try:

            required_skills = json.loads(
                raw_skills
            )

            if not isinstance(
                required_skills,
                list
            ):
                required_skills = []

        except (
            json.JSONDecodeError,
            TypeError
        ):

            required_skills = []

        # -----------------------------------------
        # Semantic similarity
        # -----------------------------------------

        job_embedding = generate_embedding(
            document
        )

        semantic_similarity = cosine_similarity(
            [candidate_embedding],
            [job_embedding]
        )[0][0]

        # -----------------------------------------
        # Job information
        # -----------------------------------------

        job_title = metadata.get(
            "title",
            ""
        )

        job_experience_level = metadata.get(
            "experience_level",
            ""
        )

        job_work_mode = metadata.get(
            "work_mode",
            ""
        )

        job_company = metadata.get(
            "company",
            ""
        )

        job_location = metadata.get(
            "location",
            ""
        )

        job_source_url = metadata.get(
            "source_url",
            ""
        )

        # -----------------------------------------
        # Hybrid ranking
        # -----------------------------------------

        ranking = rank_job(
            candidate_skills=candidate_skills,
            job_required_skills=required_skills,
            semantic_similarity=semantic_similarity,
            candidate_years=candidate_years,
            candidate_seniority=candidate_seniority,
            job_experience_level=job_experience_level,
            job_title=job_title
        )

        # -----------------------------------------
        # Store ranked result
        # -----------------------------------------

        ranked_jobs.append({

            "job_id":
                job_id,

            "title":
                job_title,

            "company":
                job_company,

            "location":
                job_location,

            "work_mode":
                job_work_mode,

            "experience_level":
                job_experience_level,

            "source_url":
                job_source_url,

            # -----------------------------------------
            # Full job description
            # Used by Career Intelligence,
            # Resume Optimizer and Interview Prep
            # -----------------------------------------

            "description":
                document,

            "required_skills":
                required_skills,

            "matched_skills":
                ranking["matched_skills"],

            "missing_skills":
                ranking["missing_skills"],

            "skill_score":
                ranking["skill_score"],

            "semantic_score":
                ranking["semantic_score"],

            "experience_score":
                ranking["experience_score"],

            "experience_status":
                ranking["experience_status"],

            "seniority_score":
                ranking["seniority_score"],

            "seniority_status":
                ranking["seniority_status"],

            "job_seniority":
                ranking["job_seniority"],

            "candidate_seniority":
                ranking["candidate_seniority"],

            "final_score":
                ranking["final_score"],

            # -----------------------------------------
            # Explainable Match
            # -----------------------------------------

            "match_explanation":
                ranking["match_explanation"],

            # -----------------------------------------
            # Vector database distance
            # -----------------------------------------

            "chroma_distance":
                distance
        })

    # -----------------------------------------
    # 3. Sort by final score
    # -----------------------------------------

    ranked_jobs.sort(
        key=lambda job: job["final_score"],
        reverse=True
    )

    return ranked_jobs