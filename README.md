# 🚀 Semantic Lecture Assistant (RAG-Based QA System)

A context-aware AI assistant that answers questions from lecture transcripts using a Retrieval-Augmented Generation (RAG) pipeline.

This project demonstrates a full end-to-end RAG system running **entirely locally**, combining semantic search with LLM-based reasoning.

### 🔑 Key Highlights
- Built a complete RAG pipeline from scratch
- Uses **BGE-M3 embeddings** for semantic retrieval
- Uses **Llama 3.2** for answer generation
- Implements **cosine similarity** for context ranking
- Fully local inference (no external APIs)

> ⚡ Designed as a foundation for integrating AI assistants into real-world web applications

## 💡 Why I Built This

I built this project to understand how modern AI assistants work under the hood—especially how retrieval and generation can be combined to produce accurate, context-aware responses.

As someone interested in full-stack development, I wanted to explore how LLMs can be integrated into web applications to build intelligent features like chat assistants and semantic search.

This project is my first step toward building production-ready AI-powered applications.

## 🔄 System Flow

```
[User Question]
        ↓
[Convert to Embedding]
        ↓
[Compare with Stored Chunk Embeddings]
        ↓
[Retrieve Top-K Relevant Chunks]
        ↓
[Construct Context]
        ↓
[Send to LLM]
        ↓
[Generate Final Answer]
```

This pipeline ensures responses are grounded in the provided data instead of relying on general knowledge.

## 📋 Overview

This project implements a RAG pipeline that:
- Chunks lecture transcripts into manageable segments
- Generates vector embeddings for each chunk using the **BGE-M3** model
- Retrieves the most relevant chunks using semantic similarity (cosine distance)
- Uses the **Llama 3.2** model to generate context-aware answers based on retrieved chunks

All processing is done **locally** on your machine without any external API calls.

## 🔧 Requirements

### System Requirements
- **Ollama**: A local LLM runtime environment
- **Python 3.7+**
- **pip** (Python package manager)

### Required Models
This project requires two models to be installed and running in Ollama:

1. **bge-m3** - For generating text embeddings
   ```bash
   ollama pull bge-m3
   ```

2. **llama3.2** - For generating context-aware answers
   ```bash
   ollama pull llama3.2
   ```

## 🚀 Installation

### Step 1: Install Ollama

Download and install Ollama from [ollama.ai](https://ollama.ai)

### Step 2: Pull Required Models

Open a terminal and run:
```bash
ollama pull bge-m3
ollama pull llama3.2
```

### Step 3: Clone the Repository

```bash
git clone https://github.com/Abhishekpo/LectureRAG-Assistant.git
cd LectureRAG-Assistant
```

### Step 4: Install Python Dependencies

```bash
pip install requests
```

## 📁 Project Structure

```
LectureRAG-Assistant/
├── README.md                  # This file
├── chunk_transcript.py         # Script to chunk raw transcripts
├── embed_chunks.py             # Script to generate embeddings for chunks
├── search_chunks.py            # Script to search and retrieve relevant chunks
├── rag_answer.py               # Main script to ask questions and get answers
├── chunks.txt                  # Processed transcript chunks
├── embeddings.json             # Pre-computed embeddings for all chunks
└── transcripts/                # Directory for storing lecture transcripts
```

## 🔄 Workflow

### 1. Prepare Transcripts

Place your lecture transcript files in the `transcripts/` directory. The system expects raw text transcripts.

### 2. Generate Chunks

Run the chunking script to split transcripts into manageable pieces:
```bash
python chunk_transcript.py
```

This creates `chunks.txt` with formatted chunks.

### 3. Generate Embeddings

Embed all chunks using the BGE-M3 model:
```bash
python embed_chunks.py
```

**Note**: Ollama must be running in the background for this to work.

This creates `embeddings.json` with all chunk embeddings.

### 4. Ask Questions

Run the main RAG script to ask questions:
```bash
python rag_answer.py
```

The script will:
- Prompt you to enter a question
- Embed your question
- Find the top 3 most relevant chunks using cosine similarity
- Send the retrieved chunks and question to Llama 3.2
- Return a context-aware answer based on the lecture transcript

## 💻 Running the Program

### Prerequisites Check
Before running, ensure:
1. **Ollama is running** in the background
   - On macOS/Linux: Ollama runs automatically after installation
   - On Windows: Launch the Ollama application
2. **Models are downloaded**: Run `ollama list` to verify both models are installed

### Running the RAG Assistant

```bash
# Make sure you're in the project directory
cd LectureRAG-Assistant

# Start asking questions
python rag_answer.py
```

### Example Interaction

```
Ask a question: What is the main topic of the lecture?
<Processing...>

Answer:
Based on the lecture transcript, the main topic is...
```

## 🔍 Advanced Usage

### Search Only (Without LLM Answer)

If you just want to search for relevant chunks without generating an answer:
```bash
python search_chunks.py
```

This will:
- Prompt you for a question
- Return the top 3 most relevant chunks with similarity scores
- Useful for previewing what context will be used

### Customization

You can modify the following parameters in the scripts:

**In `rag_answer.py` and `embed_chunks.py`:**
- `EMBED_MODEL`: Change the embedding model (default: "bge-m3")
- `CHAT_MODEL`: Change the LLM model (default: "llama3.2")

**In `rag_answer.py`:**
- `top_chunks = results[:3]`: Change the number of retrieved chunks (currently top 3)

## ⚙️ Technical Details

### Embedding Model: BGE-M3
- **Purpose**: Converts text into high-dimensional vector embeddings
- **Dimensions**: 1024-dimensional vectors
- **Use**: Semantic similarity matching between questions and transcript chunks

### Chat Model: Llama 3.2
- **Purpose**: Generates natural language answers
- **Context**: Operates only on the retrieved chunks and user question
- **Safety**: Configured to only use information from the lecture transcript

### Similarity Metric
- **Cosine Similarity**: Measures the angular distance between embedding vectors
- **Range**: -1 to 1 (higher values = more similar)
- **Why**: Works well for semantic similarity in high-dimensional spaces

## 📝 Notes

- ✅ All processing happens locally - no data is sent to external servers
- ✅ Embeddings are pre-computed and cached in `embeddings.json` for fast retrieval
- ✅ The system uses only the retrieved chunks as context (no hallucination from general knowledge)
- ⚠️ Requires Ollama to be running on `http://localhost:11434` (default port)
- ⚠️ First run may take time as models are loaded into memory

## 🐛 Troubleshooting

### Issue: "Connection refused" error
**Solution**: Make sure Ollama is running. Start Ollama and ensure it's accessible at `http://localhost:11434`.

### Issue: Model not found error
**Solution**: Pull the required models:
```bash
ollama pull bge-m3
ollama pull llama3.2
```

### Issue: Slow responses
**Solution**: 
- Ensure your system has sufficient RAM (minimum 8GB recommended)
- Close other applications to free up resources
- Consider using a smaller model variant

### Issue: Out of memory error
**Solution**:
- Your system may not have enough RAM for both models
- Consider using smaller model variants from Ollama's registry
- Reduce the number of chunks used for context

## 🚧 Future Improvements

- Integrate with a web UI (React + Node.js)
- Add streaming responses for better UX
- Optimize retrieval using a vector database (FAISS / Pinecone)
- Improve ranking with re-ranking models
- Reduce latency with optimized inference

## 📚 Resources

- [Ollama Documentation](https://github.com/ollama/ollama)
- [Retrieval-Augmented Generation (RAG) Overview](https://arxiv.org/abs/2005.11401)
- [BGE Model Documentation](https://github.com/FlagOpen/FlagEmbedding)

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Abhishekpo** - Created and maintained this RAG system

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Happy Questioning! 🚀**
