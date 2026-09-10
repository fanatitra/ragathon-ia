from sentence_transformers import SentenceTransformer

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

print(f"Downloading and caching '{MODEL_NAME}'...")
SentenceTransformer(MODEL_NAME)
print("Done. This model is now cached locally and will not require network access.")
