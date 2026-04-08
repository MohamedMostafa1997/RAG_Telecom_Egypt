import os

from data.loader import load_uploaded_file


def process_uploaded_files(docs):
    processed_docs = []

    for doc in docs:
        doc.page_content = doc.page_content.strip()
        doc.metadata["category"] = "user_upload"
        processed_docs.append(doc)

    return processed_docs


def add_file_to_store(file_path, text_splitter, vector_store):

    docs = load_uploaded_file(file_path)

    if not docs:
        return 0

    docs = process_uploaded_files(docs)

    chunks = text_splitter.split_documents(docs)

    vector_store.add_documents(chunks)

    print(f"Added {len(chunks)} chunks from {os.path.basename(file_path)}")
    return len(chunks)