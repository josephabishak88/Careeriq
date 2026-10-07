from app.services.interview_service import generate_interview_prep


candidate_text = """
Final-year B.Tech Computer Science and Engineering student.

Skills:
Python, Machine Learning, FastAPI, XGBoost, Data Science.

Experience:
Data Science Intern.

Projects:
Built a prediabetes detection system using machine learning
models including XGBoost, LightGBM, CatBoost and Random Forest.

Interested in AI and Data Science roles.
"""


job_title = "Data Scientist"

company = "CRED"


job_description = """
The role involves analyzing data, building predictive models,
performing experimentation and generating insights to support
business decisions.

Candidates should have strong programming and analytical skills
and experience with machine learning and data analysis.
"""


required_skills = [
    "Python",
    "Machine Learning",
    "Data Analysis",
    "SQL",
    "Experimentation"
]


missing_skills = [
    "SQL",
    "Experimentation"
]


result = generate_interview_prep(
    candidate_text=candidate_text,
    job_title=job_title,
    company=company,
    job_description=job_description,
    required_skills=required_skills,
    missing_skills=missing_skills
)


print("\n===== CAREERIQ INTERVIEW PREPARATION =====\n")
print(result)