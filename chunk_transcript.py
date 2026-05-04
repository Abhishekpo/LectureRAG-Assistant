from pathlib import Path

INPUT_FILE = "transcripts/audio1.txt"
OUTPUT_FILE = "chunks.txt"

def chunk_text(text, chunk_size=400, overlap=80):
    words = text.split()
    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(words), step):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks

# encoding = "utf-8" is important to handle any special characters in the transcript like emojis, accented characters, etc. 
# It ensures that the text is read correctly without any encoding issues.
# Supports all characters (English, symbols, Nepali, etc.)
text = Path(INPUT_FILE).read_text(encoding="utf-8")

# light cleaning
text = text.replace("\n", " ")
# breaks text into words and rejoins to ensure consistent spacing
#Splits on any whitespace (space, tab, newline) and rejoins with a single space,
# effectively normalizing the spacing in the text.
text = " ".join(text.split())

chunks = chunk_text(text)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks, start=1):
        f.write(f"\n\n--- CHUNK {i} ---\n")
        f.write(chunk)

print(f"Created {len(chunks)} chunks in {OUTPUT_FILE}")