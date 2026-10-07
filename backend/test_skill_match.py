from app.services.skill_matcher import calculate_skill_match


candidate_skills = [
    "Python",
    "Machine Learning",
    "FastAPI",
    "XGBoost",
    "Data Science"
]

required_skills = [
    "Python",
    "Machine Learning",
    "SQL",
    "FastAPI",
    "Docker"
]


result = calculate_skill_match(
    candidate_skills,
    required_skills
)


print("\n===== SKILL MATCH =====")

print("Matched Skills:")
for skill in result["matched_skills"]:
    print("-", skill)

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("-", skill)

print(
    "\nSkill Match:",
    result["match_percentage"],
    "%"
)