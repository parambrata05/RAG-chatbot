# 💬 Local RAG Chatbot (Ollama + LangChain + FAISS)

A fully local Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Ollama (Mistral), FAISS vector database, and Streamlit.

This project demonstrates end-to-end LLM application development including embeddings, vector search, conversational memory, and local model inference — all running without paid APIs.

---

## 🚀 Features

- 🔹 Local LLM using Ollama (Mistral)
- 🔹 Retrieval-Augmented Generation (RAG)
- 🔹 FAISS vector database
- 🔹 HuggingFace sentence-transformer embeddings
- 🔹 Conversational memory
- 🔹 Streamlit chat interface
- 🔹 Fully offline (no OpenAI API required)

---

## 🏗️ Tech Stack

- Python 3.10
- LangChain (v0.1.20)
- Ollama (Mistral model)
- FAISS
- HuggingFace Embeddings
- Streamlit
- PyTorch (CPU)

---

## 📂 Project Structure

chatbot/
│
├── app.py # Streamlit frontend
├── chain.py # RAG pipeline
├── ingest.py # Creates FAISS index
├── data.txt # Knowledge base
├── faiss_index/ # Generated vector store
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd chatbot
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install langchain==0.1.20
pip install langchain-community==0.0.38
pip install langchain-huggingface==0.0.3
pip install langsmith==0.1.147
pip install faiss-cpu
pip install sentence-transformers
pip install streamlit
pip install python-dotenv
pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu
pip install numpy==1.26.4
4️⃣ Install Ollama & Pull Model
Download Ollama from:

https://ollama.com

Then:

ollama pull mistral
5️⃣ Create Vector Index
python ingest.py
6️⃣ Run Application
python -m streamlit run app.py
Open:

http://localhost:8501
🧠 How It Works
data.txt is split into chunks.

Chunks are converted into embeddings.

FAISS stores embeddings locally.

On user query:

Relevant chunks are retrieved.

Sent to Mistral via Ollama.

Response generated with conversational memory.

📸 Example Use Cases
Resume chatbot

Personal knowledge assistant

Documentation search

Offline AI assistant

Learning RAG architecture

🎯 Key Learning Outcomes
Built full RAG pipeline from scratch

Integrated local LLM (no external APIs)

Handled dependency & version conflicts

Implemented vector search with FAISS

Designed conversational memory system

📌 Future Improvements
Add streaming responses

Add source citation display

Dockerize application

Deploy via FastAPI backend

Add authentication
