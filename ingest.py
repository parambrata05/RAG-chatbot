# ingest.py

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def ingest():
    # Load document
    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    split_docs = splitter.split_documents(documents)

    # Local embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS index
    db = FAISS.from_documents(split_docs, embeddings)

    # Save locally
    db.save_local("faiss_index")


if __name__ == "__main__":
    ingest()
