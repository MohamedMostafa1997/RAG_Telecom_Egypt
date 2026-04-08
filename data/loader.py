import os
import pytesseract
from PIL import Image

from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader, Docx2txtLoader, TextLoader, BSHTMLLoader

from config import TESSERACT_PATH

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def load_uploaded_file(file_path):
    ext = file_path.split(".")[-1].lower()
    docs = []

    try:
        if ext == "pdf":
            loader = PyMuPDFLoader(file_path)
            docs = loader.load()

        elif ext == "docx":
            loader = Docx2txtLoader(file_path)
            docs = loader.load()

        elif ext == "txt":
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()

        elif ext in ["html"]:
            loader = BSHTMLLoader(file_path)
            docs = loader.load()

        elif ext in ["jpg", "jpeg", "png"]:
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img, lang="ara+eng")

            if text.strip():
                docs = [
                    Document(
                        page_content=text,
                        metadata={"source": file_path, "type": "image"}
                    )
                ]

        if not docs:
            return []

        for doc in docs:
            doc.metadata["uploaded"] = True
            doc.metadata["file_type"] = ext
            doc.metadata["filename"] = os.path.basename(file_path)

        print(f"Loaded {len(docs)} pages from {os.path.basename(file_path)}")
        return docs

    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return []