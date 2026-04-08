import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import ConversationalRetrievalChain

from rag_model_scripts.llm import load_llm
from rag_model_scripts.embeddings import load_embeddings
from rag_model_scripts.vector_store import load_vector_store
from rag_model_scripts.retriever import create_retriever
from rag_model_scripts.memory import create_memory
from rag_model_scripts.prompt import SYSTEM_PROMPT

from data.scraper import load_telecom_docs
from data.loader import load_uploaded_file
from data.file_pipeline import add_file_to_store

from config import *


class TelecomEgyptChatbot:

    def __init__(self):
        self.vector_store = None
        self.retriever = None
        self.conv_chain = None
        self.memory = None
        self.text_splitter = None
        self.embeddings = None
        self.llm = None

    def setup(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=["\n\n", "\n", ". ", "، ", "  ", " ", ""],
        )

        self.embeddings = load_embeddings()

        if os.path.exists(CHROMA_DB_PATH):
            self.vector_store = load_vector_store(self.embeddings)
        else:
            raw_docs = load_telecom_docs(TELECOM_URLS)
            chunks = self.text_splitter.split_documents(raw_docs)

            self.vector_store = load_vector_store(self.embeddings)
            self.vector_store.add_documents(chunks)

        self.retriever = create_retriever(self.vector_store)
        self.llm = load_llm()
        self.memory = create_memory()

        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", "{question}")
        ])

        self.conv_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            memory=self.memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={"prompt": prompt}
        )

    def chat(self, message, history, uploaded_file):

        if uploaded_file is not None:
            add_file_to_store(
                uploaded_file.name,
                self.text_splitter,
                self.vector_store
            )

        result = self.conv_chain.invoke({"question": message})

        answer = result["answer"]
        sources = result.get("source_documents", [])

        if sources:
            unique_sources = list(set(
                doc.metadata.get("source", "")
                for doc in sources
                if doc.metadata.get("source_site") == "te.eg"
            ))

            if unique_sources:
                answer += "\n\nSources:"
                for src in unique_sources:
                    answer += f"\n- {src}"

        return answer

    def reset_memory(self):
        if self.memory:
            self.memory.clear()
        return []