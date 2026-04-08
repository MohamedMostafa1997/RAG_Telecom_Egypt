from langchain_ollama import ChatOllama
from config import OLLAMA_MODEL

def load_llm():
    return ChatOllama(
        model=OLLAMA_MODEL,
        #temperature=0.3  
    )