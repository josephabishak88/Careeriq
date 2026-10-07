from app.services.resume_optimizer import optimize_resume_for_job
from app.services.job_storage import load_jobs


print("\n===== CAREERIQ RESUME OPTIMIZATION TEST =====")

jobs = load_jobs()

if not jobs:
    print("No jobs found in jobs.json")
    exit()

job = jobs[0]

print("\nSelected Job:")
print("Title:", job.title)
print("Company:", job.company)
print("Description Length:", len(job.description or ""))

if not job.description:
    print("\nERROR: Job description is empty.")
    exit()

sample_resume = """
Arun Kumar

B.Tech Computer Science Engineering

Skills:
Python, SQL, Machine Learning, Deep Learning,
Scikit-learn, XGBoost, CatBoost, LLM, RAG,
Generative AI, Pandas, NumPy, FastAPI

Experience:
Data Science Intern

Projects:
Medical Insurance Risk Prediction
Career Recommendation AI Agent
"""

result = optimize_resume_for_job(
    resume_text=sample_resume,
    job_title=job.title or "",
    company=job.company or "",
    job_description=job.description or "",
    required_skills=job.required_skills,
    missing_skills=[]
)

print("\n===== OPTIMIZATION RESULT =====")
print(result)