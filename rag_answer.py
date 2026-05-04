import json
import requests
import math

EMBED_MODEL = "bge-m3"
CHAT_MODEL = "llama3.2"
EMBEDDINGS_FILE = "embeddings.json"

def get_embedding(text):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text}
    )
    response.raise_for_status()
    return response.json()["embedding"]

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0

def ask_llm(question, context):
    prompt = f"""
    You are a helpful assistant answering questions from a lecture transcript.

    Use ONLY the context below.
    If the answer is not in the context, say: "I don't know based on the lecture transcript."

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": CHAT_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    return response.json()["response"]

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

top_chunks = results[:3]

context = "\n\n".join(
    [f"Chunk {c['chunk_id']}:\n{c['text']}" for c in top_chunks]
)

answer = ask_llm(question, context)

print("\nAnswer:\n")
print(answer)

