from app.services.vector_store import search_jobs


TEST_QUERIES = [
    "machine learning artificial intelligence data science",
    "Python backend developer FastAPI",
    "data analyst SQL analytics",
    "generative AI LLM RAG",
    "software engineer",
]


def evaluate_retrieval(top_k: int = 5):

    print("\n======================================")
    print("      CAREERIQ RETRIEVAL EVALUATION")
    print("======================================\n")

    for query in TEST_QUERIES:

        print("--------------------------------------")
        print(f"QUERY: {query}")
        print("--------------------------------------")

        results = search_jobs(
            query=query,
            top_k=top_k
        )

        ids = results.get("ids", [[]])[0]
        documents = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]

        if not ids:
            print("No jobs retrieved.\n")
            continue

        for rank, (job_id, document, distance) in enumerate(
            zip(ids, documents, distances),
            start=1
        ):

            first_lines = document.strip().splitlines()

            job_title = "Unknown"
            company = "Unknown"

            for line in first_lines:

                line = line.strip()

                if line.lower().startswith("job title:"):
                    job_title = line.split(":", 1)[1].strip()

                elif line.lower().startswith("company:"):
                    company = line.split(":", 1)[1].strip()

            print(
                f"{rank}. {job_title} | "
                f"{company} | "
                f"distance={distance:.4f}"
            )

        print()


if __name__ == "__main__":
    evaluate_retrieval()