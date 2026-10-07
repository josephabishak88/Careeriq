from app.services.resume_optimizer import optimize_resume_for_job


resume_text = """
Final-year B.Tech Computer Science and Engineering student.

Skills:
Python, Machine Learning, FastAPI, XGBoost, Data Science.

Projects:
Built a prediabetes detection system using machine learning
models including XGBoost, LightGBM, CatBoost and Random Forest.

Experience:
Data Science Intern.

Interested in AI and Data Science roles.
"""


job_title = "Credit Card Bill Payments Growth"

company = "CRED"


job_description = """
The role focuses on improving credit card bill payment growth
through data analysis, experimentation and product analytics.
The candidate should work with data to identify opportunities
and improve business outcomes.
"""


required_skills = [
    "Product Analytics",
    "Experimentation",
    "Data Analysis",
    "Machine Learning"
]


missing_skills = [
    "Product Analytics",
    "Experimentation"
]


result = optimize_resume_for_job(
    resume_text=resume_text,
    job_title=job_title,
    company=company,
    job_description=job_description,
    required_skills=required_skills,
    missing_skills=missing_skills
)


print("\n===== CAREERIQ RESUME OPTIMIZATION =====\n")
print(result)