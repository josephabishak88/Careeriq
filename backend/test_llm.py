from app.services.llm_service import analyze_resume_with_llm


resume_text = """
Joseph D Abishak

Final-year B.Tech Computer Science and Engineering
student specializing in Artificial Intelligence and Data Science.

Skills:
Python
Machine Learning
Data Science
FastAPI
Streamlit
XGBoost

Projects:
MarketPulse - Marketing Intelligence Platform
Anime Recommendation System
Job Recommendation AI Agent

Experience:
Data Science Intern

Certifications:
IBM SkillsBuild Applied Artificial Intelligence
"""


profile = analyze_resume_with_llm(resume_text)

print("\n===== CANDIDATE PROFILE =====\n")

print(profile.model_dump_json(indent=2))