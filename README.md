# 🧠 Second Brain — AI Personal Knowledge OS

A RAG-powered (Retrieval-Augmented Generation) personal knowledge management system. Upload documents, index them semantically, search with natural language, and have AI-powered conversations grounded in your personal knowledge base.

![Tech Stack](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F61?style=for-the-badge&logoColor=white)

## ✨ Features

- **📄 Document Ingestion** — Upload PDF, DOCX, Markdown, and text files
- **🔍 Semantic Search** — Find relevant information using natural language queries
- **💬 RAG Chat** — AI-powered conversations grounded in your documents with source citations
- **📊 Dashboard** — Overview of your knowledge base with stats and recent activity
- **⚡ Real-time Indexing** — Documents become searchable immediately after upload
- **🔒 Local-first** — All data stays on your machine

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                  Frontend (React)                │
│   Dashboard │ Search │ Chat │ Documents          │
└──────────────────┬──────────────────────────────┘
                   │ REST API
┌──────────────────▼──────────────────────────────┐
│                Backend (FastAPI)                  │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────┐ │
│  │ Document │ │  Search  │ │   RAG Chat       │ │
│  │ Service  │ │ Service  │ │   Service        │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────────────┘ │
│       │             │            │               │
│  ┌────▼─────────────▼────────────▼─────────────┐ │
│  │           Core RAG Pipeline                  │ │
│  │  Chunker → Embeddings → VectorStore → LLM   │ │
│  └──────────────────────────────────────────────┘ │
│                                                   │
│  ┌─────────────┐  ┌──────────────────────────┐   │
│  │  ChromaDB   │  │  OpenAI API              │   │
│  │ (Vectors)   │  │  (Embeddings + LLM)      │   │
│  └─────────────┘  └──────────────────────────┘   │
└───────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API Key

### 1. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Start the server
uvicorn app.main:app --reload --port 8000
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
```

### 3. Open the App

Visit **http://localhost:5173** in your browser.

## 📁 Project Structure

```
Second_Brain/
├── backend/
│   ├── app/
│   │   ├── api/routes/        # REST API endpoints
│   │   ├── core/              # RAG pipeline components
│   │   ├── models/            # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── config.py          # Configuration
│   │   └── main.py            # FastAPI entry point
│   ├── data/
│   │   ├── uploads/           # Uploaded documents
│   │   └── chroma_db/         # Vector database storage
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/             # Page views
│   │   ├── services/          # API client
│   │   ├── App.jsx
│   │   └── index.css          # Design system
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 19 + Vite |
| Styling | Vanilla CSS (Glassmorphism Dark Theme) |
| Backend | FastAPI + Uvicorn |
| Vector DB | ChromaDB (local) |
| Embeddings | OpenAI text-embedding-3-small |
| LLM | OpenAI gpt-4o-mini |
| Doc Parsing | PyPDF2, python-docx, markdown |

## 📝 Supported File Types

| Format | Extension |
|--------|-----------|
| Plain Text | `.txt` |
| Markdown | `.md` |
| PDF | `.pdf` |
| Word Document | `.docx` |

## ⚙️ Configuration

All configuration is managed via environment variables in `backend/.env`:

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | (required) | Your OpenAI API key |
| `EMBEDDING_MODEL` | `text-embedding-3-small` | Embedding model |
| `LLM_MODEL` | `gpt-4o-mini` | Chat completion model |
| `CHUNK_SIZE` | `1000` | Document chunk size (chars) |
| `CHUNK_OVERLAP` | `200` | Chunk overlap (chars) |
| `CHROMA_PERSIST_DIR` | `./data/chroma_db` | ChromaDB storage path |
| `UPLOAD_DIR` | `./data/uploads` | Document upload path |

## 📜 License

MIT
