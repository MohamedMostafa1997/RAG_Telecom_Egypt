import torch
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL

def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cuda" if torch.cuda.is_available() else "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )