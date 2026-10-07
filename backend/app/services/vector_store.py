import chromadb
import json

from app.services.embedding_service import generate_embedding


client = chromadb.PersistentClient(
    path="data/chroma_db"
)

collection = client.get_or_create_collection(
    name="careeriq_jobs"
)


def add_job(job):

    text = f"""
    Job Title: {job.title}
    Company: {job.company}
    Location: {job.location}
    Work Mode: {job.work_mode}
    Experience: {job.experience_level}
    Required Skills: {", ".join(job.required_skills)}
    Preferred Skills: {", ".join(job.preferred_skills)}
    Description: {job.description}
    """

    embedding = generate_embedding(text)

    collection.upsert(
        ids=[job.job_id],
        embeddings=[embedding],
        documents=[text],
        metadatas=[{
    "title": job.title or "",
    "company": job.company or "",
    "location": job.location or "",
    "source_url": job.source_url or "",
    "experience_level": job.experience_level or "",
    "required_skills": json.dumps(
        job.required_skills
    )
}]
    )


def search_jobs(query: str, top_k: int = 5):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "metadatas",
            "documents",
            "distances"
        ]
    )

    return results