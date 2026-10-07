from app.services.vector_store import search_jobs


# --------------------------------------------------
# Human-labelled retrieval benchmark
# --------------------------------------------------
# The expected jobs are based on the actual job titles
# currently present in the CareerIQ job collection.
#
# We use broad title keywords instead of exact job IDs
# so the benchmark remains readable and easy to maintain.
# --------------------------------------------------

BENCHMARKS = [
    {
        "query": "machine learning artificial intelligence data science",
        "relevant_keywords": [
            "machine learning",
            "ai analyst",
            "machine learning engineer"
        ]
    },
    {
        "query": "Python backend developer FastAPI",
        "relevant_keywords": [
            "backend engineer",
            "backend",
            "software engineer"
        ]
    },
    {
        "query": "data analyst SQL analytics",
        "relevant_keywords": [
            "analytics",
            "data analyst"
        ]
    },
    {
        "query": "generative AI LLM RAG",
        "relevant_keywords": [
            "ai engineer",
            "ai solution engineer",
            "machine learning engineer",
            "ai agents"
        ]
    },
    {
        "query": "software engineer",
        "relevant_keywords": [
            "software engineer",
            "backend engineer"
        ]
    }
]


def is_relevant(job_title: str, relevant_keywords: list[str]) -> bool:

    title = job_title.lower()

    return any(
        keyword.lower() in title
        for keyword in relevant_keywords
    )


def calculate_precision_at_k(
    retrieved_titles: list[str],
    relevant_keywords: list[str]
) -> float:

    if not retrieved_titles:
        return 0.0

    relevant_count = sum(
        is_relevant(title, relevant_keywords)
        for title in retrieved_titles
    )

    return relevant_count / len(retrieved_titles)


def run_benchmark(top_k: int = 5):

    print("\n======================================")
    print("       CAREERIQ RETRIEVAL BENCHMARK")
    print("======================================\n")

    precision_scores = []

    for benchmark in BENCHMARKS:

        query = benchmark["query"]
        relevant_keywords = benchmark["relevant_keywords"]

        print("--------------------------------------")
        print(f"QUERY: {query}")
        print("--------------------------------------")

        results = search_jobs(
            query=query,
            top_k=top_k
        )

        documents = results.get(
            "documents",
            [[]]
        )[0]

        if not documents:
            print("No jobs retrieved.")
            print("Precision@5: 0.00\n")

            precision_scores.append(0.0)
            continue

        retrieved_titles = []

        for rank, document in enumerate(
            documents,
            start=1
        ):

            title = "Unknown"

            for line in document.splitlines():

                line = line.strip()

                if line.lower().startswith("job title:"):
                    title = line.split(
                        ":",
                        1
                    )[1].strip()

                    break

            retrieved_titles.append(title)

            relevance = is_relevant(
                title,
                relevant_keywords
            )

            status = "RELEVANT" if relevance else "NOT RELEVANT"

            print(
                f"{rank}. {title} → {status}"
            )

        precision = calculate_precision_at_k(
            retrieved_titles,
            relevant_keywords
        )

        precision_scores.append(precision)

        print(
            f"\nPrecision@{top_k}: "
            f"{precision:.2f}"
        )

        print()

    if precision_scores:

        average_precision = (
            sum(precision_scores)
            / len(precision_scores)
        )

    else:
        average_precision = 0.0

    print("======================================")
    print("           FINAL RESULT")
    print("======================================")

    print(
        f"Average Precision@{top_k}: "
        f"{average_precision:.2f}"
    )

    print(
        f"Percentage: "
        f"{average_precision * 100:.2f}%"
    )

    print("======================================\n")


if __name__ == "__main__":
    run_benchmark()