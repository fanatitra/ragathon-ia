import chromadb

client = chromadb.Client()
print("ChromaDB: OK")

try:
    from groq import Groq

    print("Groq SDK: OK")
except ImportError:
    print("Groq SDK: MISSING")

try:
    from google import genai

    print("Gemini SDK: OK")
except ImportError:
    print("Gemini SDK: MISSING")

try:
    from sentence_transformers import SentenceTransformer

    print("sentence-transformers: OK")
except ImportError:
    print("sentence-transformers: MISSING")

print("\nEnvironment ready. See you on challenge day.")
