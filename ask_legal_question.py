import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

import os
import google.generativeai as genai

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY is not set. Set it in PowerShell before running the program."
    )

genai.configure(api_key=api_key)

# Step 2: Load the vectorstore
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vectorstore/", embedding, allow_dangerous_deserialization=True)


# Step 3: Ask the user a legal question
query = input("❓ Ask your legal question: ")

# Step 4: Search top relevant chunks
docs = vectorstore.similarity_search(query, k=3)
context = "\n\n".join([doc.page_content for doc in docs])

# Step 5: Send to Gemini for answer generation
model = genai.GenerativeModel("models/gemini-3.8-flash")
response = model.generate_content(f"""
You are a legal assistant. Based on the context below, answer the legal question clearly.

Context:
{context}

Question:
{query}
""")

# Step 6: Display the final answer
print("\n💬 Gemini's Answer:")
print(response.text.strip())
