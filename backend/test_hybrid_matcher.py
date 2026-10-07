from app.services.hybrid_matcher import calculate_hybrid_score


skill_match = 60.0
semantic_similarity = 0.55466866

result = calculate_hybrid_score(
    skill_match_percentage=skill_match,
    semantic_similarity=semantic_similarity
)

print("\n===== HYBRID MATCHING =====")

print("Skill Score:", result["skill_score"], "%")
print("Semantic Score:", result["semantic_score"], "%")
print("Final Match Score:", result["final_score"], "%")