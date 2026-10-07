from app.services.rag_service import generate_rag_answer


TEST_CASES = [
    {
        "name": "Supported Career Question",
        "candidate": """
Final-year CSE student with skills in Python,
Machine Learning, SQL, Generative AI and RAG.
""",
        "query": "Which retrieved jobs are most relevant to my technical skills?"
    },
    {
        "name": "Supported Skill Question",
        "candidate": """
Final-year CSE student with Python, Machine Learning,
SQL, Generative AI and RAG skills.
""",
        "query": "What skills are mentioned in the retrieved jobs?"
    },
    {
        "name": "Unsupported Information Question",
        "candidate": """
Final-year CSE student with Python, Machine Learning,
SQL, Generative AI and RAG skills.
""",
        "query": "Which retrieved company offers the highest salary?"
    }
]


def run_rag_evaluation():

    print("\n======================================")
    print("          CAREERIQ RAG EVALUATION")
    print("======================================\n")

    for case in TEST_CASES:

        print("--------------------------------------")
        print(f"TEST: {case['name']}")
        print("--------------------------------------")

        print(f"QUESTION:\n{case['query']}\n")

        answer = generate_rag_answer(
            candidate_text=case["candidate"],
            query=case["query"],
            top_k=3
        )

        print("ANSWER:")
        print(answer)

        print("\n")


if __name__ == "__main__":
    run_rag_evaluation()