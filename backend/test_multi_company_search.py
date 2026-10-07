from app.services.vector_store import search_jobs


queries = [
    "Python machine learning artificial intelligence",
    "backend software engineering",
    "AI agents healthcare",
    "data analytics data science"
]


print("\n===== CAREERIQ MULTI-COMPANY SEARCH =====")


for query in queries:

    print("\n===================================")
    print("QUERY:", query)
    print("===================================")

    results = search_jobs(
        query=query,
        top_k=5
    )

    for i in range(len(results["ids"][0])):

        metadata = results["metadatas"][0][i]
        distance = results["distances"][0][i]

        print(
            f"\n{i + 1}. "
            f"{metadata.get('title', '')}"
        )

        print(
            "Company:",
            metadata.get("company", "")
        )

        print(
            "Location:",
            metadata.get("location", "")
        )

        print(
            "Chroma Distance:",
            round(distance, 4)
        )