from app.services.interview_report import generate_interview_report


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


interview_history = [
    {
        "question": "Why did you choose XGBoost for your project?",
        "answer": """
        I used XGBoost because it is a powerful machine
        learning algorithm. I compared it with LightGBM,
        CatBoost and Random Forest.
        """,
        "evaluation": {
            "relevance": 8,
            "technical_accuracy": 7,
            "clarity": 7,
            "depth": 5,
            "overall_score": 7,
            "strengths": [
                "Relevant model comparison",
                "Correct basic understanding"
            ],
            "weaknesses": [
                "Limited explanation of model selection"
            ],
            "missing_points": [
                "Specific evaluation metrics",
                "Why XGBoost performed better"
            ]
        }
    },
    {
        "question": "How did you handle class imbalance?",
        "answer": """
        I used class weighting and SMOTE to address the
        imbalance in the dataset and evaluated the models
        again after optimization.
        """,
        "evaluation": {
            "relevance": 9,
            "technical_accuracy": 8,
            "clarity": 8,
            "depth": 7,
            "overall_score": 8,
            "strengths": [
                "Explained class imbalance techniques"
            ],
            "weaknesses": [
                "Could explain why the techniques were selected"
            ],
            "missing_points": [
                "Impact on evaluation metrics"
            ]
        }
    }
]


result = generate_interview_report(
    candidate_text=candidate_text,
    job_title=job_title,
    interview_history=interview_history
)


print("\n===== CAREERIQ FINAL INTERVIEW REPORT =====")

print("\nOverall Score:")
print(result["overall_score"])

print("\nTechnical Performance:")
print(result["technical_performance"])

print("\nCommunication Score:")
print(result["communication_score"])

print("\nStrengths:")
for item in result["strengths"]:
    print("-", item)

print("\nWeaknesses:")
for item in result["weaknesses"]:
    print("-", item)

print("\nTopics To Revise:")
for item in result["topics_to_revise"]:
    print("-", item)

print("\nReadiness:")
print(result["readiness"])

print("\nFinal Feedback:")
print(result["final_feedback"])