from app.services.job_service import fetch_company_jobs
from app.services.job_parser import parse_lever_job, enrich_job_profile
from app.services.job_analyzer import analyze_job_description
from app.services.vector_store import add_job, search_jobs


# 1. Fetch a real job
jobs = fetch_company_jobs("cred")

raw_job = jobs[0]

# 2. Convert it into our JobProfile
job = parse_lever_job(raw_job, company="CRED")

# 3. Analyze the description
if job.description:
    analysis = analyze_job_description(job.description)
    job = enrich_job_profile(job, analysis)

# 4. Store the job in ChromaDB
add_job(job)

print("\n===== JOB STORED =====")
print("Title:", job.title)
print("Company:", job.company)
print("Job ID:", job.job_id)


# 5. Search the Vector DB
query = "Python machine learning data science job"

results = search_jobs(query, top_k=3)

print("\n===== VECTOR SEARCH =====")
print("Query:", query)

for i, job_id in enumerate(results["ids"][0]):
    print("\nResult", i + 1)
    print("Job ID:", job_id)
    print("Title:", results["metadatas"][0][i]["title"])
    print("Company:", results["metadatas"][0][i]["company"])
    print("Location:", results["metadatas"][0][i]["location"])
    print("Distance:", results["distances"][0][i])