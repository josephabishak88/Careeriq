from app.services.embedding_service import generate_embedding


text = """
Python machine learning FastAPI XGBoost
data science and artificial intelligence
"""

embedding = generate_embedding(text)

print("Embedding generated successfully.")

print("Vector dimensions:", len(embedding))

print("\nFirst 10 values:")
print(embedding[:10])`  `