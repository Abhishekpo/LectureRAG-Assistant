import json
import requests
import math

EMBEDDINGS_FILE = "embeddings.json"
MODEL = "bge-m3"

def get_embedding(text):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": MODEL,
            "prompt": text
        }
    )
    response.raise_for_status()
    return response.json()["embedding"]

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(b * b for b in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)

with open(EMBEDDINGS_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

question = input("Ask a question: ")

question_embedding = get_embedding(question)

results = []

for chunk in chunks:
    score = cosine_similarity(question_embedding, chunk["embedding"])
    results.append({
        "chunk_id": chunk["chunk_id"],
        "score": score,
        "text": chunk["text"]
    })

results = sorted(results, key=lambda x: x["score"], reverse=True)

top_results = results[:3]

print("\nTop matching chunks:\n")

for result in top_results:
    print(f"--- CHUNK {result['chunk_id']} | SCORE: {result['score']:.4f} ---")
    print(result["text"][:1000])
    print()