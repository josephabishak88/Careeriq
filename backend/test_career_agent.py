from app.services.career_agent import run_career_agent


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]


candidate_text = """
Final-year B.Tech Computer Science and Engineering student
with skills in Python, Machine Learning, FastAPI, XGBoost
and Data Science. Interested in AI and Data Science roles.
"""


user_request = """
Find the most relevant jobs for me based on my technical
skills and interest in AI and Data Science.
"""


print("\n===== CAREERIQ AGENT TEST =====")


result = run_career_agent(
    candidate_skills=candidate_skills,
    candidate_text=candidate_text,
    user_request=user_request
)


print("\n===== QUERY CHOSEN BY AGENT =====")
print(result["query_used"])


print("\n===== RETRIEVED JOBS =====")

for index, job in enumerate(result["jobs"], start=1):

    print(f"\n--- Job {index} ---")

    print("Title:", job["title"])
    print("Company:", job["company"])
    print("Location:", job["location"])
    print("Skill Score:", job["skill_score"])
    print("Semantic Score:", job["semantic_score"])
    print("Final Score:", job["final_score"])


print("\n===== AGENT FINAL ANSWER =====")
print(result["answer"])