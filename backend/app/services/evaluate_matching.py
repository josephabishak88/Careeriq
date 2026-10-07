from app.services.job_ranker import rank_job


TEST_CASES = [
    {
        "name": "Strong Technical Match",
        "candidate_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Generative AI",
            "RAG"
        ],
        "job_required_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Generative AI",
            "RAG"
        ],
        "semantic_similarity": 0.90,
        "candidate_years": 2,
        "candidate_seniority": "mid",
        "job_experience_level": "2+ years",
        "job_title": "Machine Learning Engineer"
    },
    {
        "name": "Partial Technical Match",
        "candidate_skills": [
            "Python",
            "Machine Learning",
            "SQL"
        ],
        "job_required_skills": [
            "Python",
            "Machine Learning",
            "SQL",
            "Docker",
            "AWS"
        ],
        "semantic_similarity": 0.70,
        "candidate_years": 1,
        "candidate_seniority": "junior",
        "job_experience_level": "2+ years",
        "job_title": "ML Engineer"
    },
    {
        "name": "Poor Match",
        "candidate_skills": [
            "Python",
            "Machine Learning"
        ],
        "job_required_skills": [
            "B2B Sales",
            "Negotiation",
            "CRM",
            "Lead Generation"
        ],
        "semantic_similarity": 0.20,
        "candidate_years": 0.5,
        "candidate_seniority": "entry",
        "job_experience_level": "3+ years",
        "job_title": "Account Executive"
    }
]


def run_matching_evaluation():

    print("\n======================================")
    print("       CAREERIQ MATCHING EVALUATION")
    print("======================================\n")

    scores = []

    for case in TEST_CASES:

        print("--------------------------------------")
        print(f"TEST: {case['name']}")
        print("--------------------------------------")

        result = rank_job(
            candidate_skills=case["candidate_skills"],
            job_required_skills=case["job_required_skills"],
            semantic_similarity=case["semantic_similarity"],
            candidate_years=case["candidate_years"],
            candidate_seniority=case["candidate_seniority"],
            job_experience_level=case["job_experience_level"],
            job_title=case["job_title"]
        )

        scores.append(result["final_score"])

        print(f"Job: {case['job_title']}")
        print(
            f"Skill Score: "
            f"{result['skill_score']:.2f}"
        )

        print(
            f"Semantic Score: "
            f"{result['semantic_score']:.2f}"
        )

        print(
            f"Experience Score: "
            f"{result['experience_score']:.2f}"
        )

        print(
            f"Seniority Score: "
            f"{result['seniority_score']:.2f}"
        )

        print(
            f"Final Score: "
            f"{result['final_score']:.2f}"
        )

        print(
            f"Matched Skills: "
            f"{result['matched_skills']}"
        )

        print(
            f"Missing Skills: "
            f"{result['missing_skills']}"
        )

        print(
            f"Experience Status: "
            f"{result['experience_status']}"
        )

        print(
            f"Seniority Status: "
            f"{result['seniority_status']}"
        )

        print()

    print("======================================")
    print("           FINAL RESULT")
    print("======================================")

    for index, score in enumerate(scores, start=1):
        print(
            f"Test {index} Final Score: "
            f"{score:.2f}"
        )

    print("======================================\n")


if __name__ == "__main__":
    run_matching_evaluation()