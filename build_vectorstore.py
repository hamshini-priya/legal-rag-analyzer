from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from document_loader import load_and_chunk_documents

# Load chunks from your documents
chunks = load_and_chunk_documents()

# Use a Hugging Face model to generate embeddings (Gemini-safe)
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector store
vectorstore = FAISS.from_texts(chunks, embedding)

# Save the store
vectorstore.save_local("vectorstore/")

print("✅ FAISS Vector Store built successfully using HuggingFace embeddings!")
