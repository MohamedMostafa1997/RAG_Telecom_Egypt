from langchain_chroma import Chroma
from config import CHROMA_DB_PATH, COLLECTION_NAME

def load_vector_store(embeddings):
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_PATH
    )