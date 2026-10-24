import os
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_chunk_documents(folder_path="data/", chunk_size=500, chunk_overlap=50):
    documents = []

    # Loop through files in the data folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".html") or filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
                text = file.read()

                # If HTML, clean it using BeautifulSoup
                if filename.endswith(".html"):
                    soup = BeautifulSoup(text, "html.parser")
                    text = soup.get_text()

                documents.append(text)

    # Combine all documents into one string
    full_text = "\n".join(documents)

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = splitter.split_text(full_text)

    return chunks
if __name__ == "__main__":
    chunks = load_and_chunk_documents()
    print(f"✅ Loaded and chunked {len(chunks)} text blocks.")
    print("🔍 Preview first chunk:")
    print(chunks[0][:500])
