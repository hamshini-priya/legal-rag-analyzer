# Legal RAG Analyzer

A Python-based legal document question-answering system using Retrieval-Augmented Generation (RAG).

## Features
- Loads and preprocesses HTML and TXT documents.
- Splits documents into overlapping text chunks.
- Generates embeddings using Hugging Face Sentence Transformers.
- Stores and retrieves relevant text using FAISS.
- Generates answers using the Google Gemini API.

## Tech Stack
- Python
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- Google Gemini API
- Beautiful Soup

## Project Structure
- `ask_legal_question.py` — retrieves relevant context and generates answers.
- `build_vectorstore.py` — builds and saves the FAISS vector store.
- `document_loader.py` — loads and chunks HTML and TXT documents.
- `data/` — input documents (not included in this repository).
- `vectorstore/` — generated vector index (build locally).

## Setup

1. Clone this repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your Gemini API key as an environment variable in PowerShell:

   ```powershell
   $env:GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY"
   ```

5. Place permitted `.txt` or `.html` documents in the `data/` directory.
6. Build the vector store:

   ```bash
   python build_vectorstore.py
   ```

7. Start asking questions:

   ```bash
   python ask_legal_question.py
   ```

## Disclaimer
This project is for educational and informational purposes only. It does not replace advice from a qualified legal professional.
