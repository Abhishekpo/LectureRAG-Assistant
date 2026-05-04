# we are going to use ollama to embed the chuks to vector and store them in a vector database.

import requests
from pathlib import Path
import json

CHUNKS_FILE = "chunks.txt"
OUTPUT_FILE = "embeddings.json"
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

# returns a list of floats representing the embedding vector for the input text
text = Path(CHUNKS_FILE).read_text(encoding="utf-8")

# returns a list after splitting the text into chunks based on the delimiter "--- CHUNK "
raw_chunks = text.split("--- CHUNK ")
chunks = []

for part in raw_chunks:
    #Removes extra whitespace from the start and end of the string.
    part = part.strip()
    if not part:
        continue

    lines = part.split("\n", 1)
    chunk_id = lines[0].replace("---", "").strip()
    chunk_text = lines[1].strip()

    chunks.append({
        "chunk_id": chunk_id,
        "text": chunk_text,
        "embedding": get_embedding(chunk_text)
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2)

print(f"Created embeddings for {len(chunks)} chunks")
