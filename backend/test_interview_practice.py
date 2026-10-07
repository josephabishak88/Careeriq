from app.services.interview_practice import (
    start_interview,
    evaluate_answer
)


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
The candidate should be comfortable working with
Python and data-driven problem solving.
"""


required_skills = [
    "Python",
    "Machine Learning",
    "Data Analysis",
    "SQL",
    "Experimentation"
]


# Start interview
question_result = start_interview(
    candidate_text=candidate_text,
    job_title=job_title,
    job_description=job_description,
    required_skills=required_skills
)

question = question_result["question"]

print("\n===== CAREERIQ PRACTICE INTERVIEW =====")
print("\nQuestion:")
print(question)

print("\nCategory:")
print(question_result["category"])


# Simulated candidate answer
answer = """
I used XGBoost in my prediabetes detection project because
it is a powerful tree-based machine learning algorithm.
I compared it with models such as LightGBM, CatBoost and
Random Forest and evaluated their performance to identify
a suitable model for the prediction task.
"""


# Evaluate answer
evaluation = evaluate_answer(
    candidate_text=candidate_text,
    job_title=job_title,
    question=question,
    answer=answer
)


print("\n===== ANSWER EVALUATION =====")

print("\nRelevance:")
print(evaluation["relevance"])

print("\nTechnical Accuracy:")
print(evaluation["technical_accuracy"])

print("\nClarity:")
print(evaluation["clarity"])

print("\nDepth:")
print(evaluation["depth"])

print("\nOverall Score:")
print(evaluation["overall_score"])

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