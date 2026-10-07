from app.services.adaptive_interview import run_interview_turn


candidate_text = """
Final-year B.Tech Computer Science and Engineering student.

Skills:
Python, Machine Learning, FastAPI, XGBoost, Data Science.

Experience:
Data Science Intern.

Project:
Built a prediabetes detection system using XGBoost,
LightGBM, CatBoost and Random Forest.
"""


job_title = "Data Scientist"

job_description = """
The role involves data analysis, machine learning,
predictive modeling and experimentation.
Candidates should have strong Python and analytical skills.
"""


required_skills = [
    "Python",
    "Machine Learning",
    "Data Analysis",
    "SQL",
    "Experimentation"
]


question = """
Can you explain how you handled class imbalance
in your prediabetes detection project?
"""


answer = """
I compared different machine learning models including
XGBoost, LightGBM, CatBoost and Random Forest. I also
optimized the models and compared their performance
using evaluation metrics.
"""


result = run_interview_turn(
    candidate_text=candidate_text,
    job_title=job_title,
    job_description=job_description,
    required_skills=required_skills,
    question=question,
    answer=answer
)


print("\n===== CURRENT QUESTION =====")
print(result["current_question"])

print("\n===== ANSWER =====")
print(result["answer"])

print("\n===== EVALUATION =====")

evaluation = result["evaluation"]

print("Relevance:", evaluation["relevance"])
print("Technical Accuracy:", evaluation["technical_accuracy"])
print("Clarity:", evaluation["clarity"])
print("Depth:", evaluation["depth"])
print("Overall Score:", evaluation["overall_score"])

print("\nStrengths:")
for item in evaluation["strengths"]:
    print("-", item)

print("\nWeaknesses:")
for item in evaluation["weaknesses"]:
    print("-", item)

print("\nMissing Points:")
for item in evaluation["missing_points"]:
    print("-", item)

print("\nImprovement Advice:")
print(evaluation["improvement_advice"])

print("\n===== NEXT QUESTION =====")
print(result["next_question"])