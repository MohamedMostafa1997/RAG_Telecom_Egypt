# Telecom Egypt Intelligent Assistant

A production-ready RAG (Retrieval-Augmented Generation) chatbot that answers customer queries using the official Telecom Egypt website as the primary knowledge base.

---

## Features

- Multi-lingual support: Arabic, English, and Egyptian dialect
- Grounded responses bounded by te.eg content only
- Source citations for every answer
- User document upload: PDF, DOCX, TXT, HTML, Images (with OCR)
- On-premises deployment — no data leaves your machine
- Conversation memory (last 5 turns)

---

## Project Structure

```
telecom-egypt-rag/
│
├── telecom_egypt.ipynb       # Main notebook — full pipeline
├── app.py                    # Standalone Gradio app
├── requirements.txt          # Python dependencies
├── chroma_telecom_db/        # Vector store (created after first run)
└── RAG_Telecom_Egypt/
    └── Tesseract-OCR/
        └── tesseract.exe     # Tesseract installation (see Step 4)
```

---

## Setup Instructions

### Step 1 — Create a Virtual Environment (Recommended)

```bash
conda create -n RAG python=3.10
conda activate RAG
```

Or with venv:

```bash
python -m venv RAG
RAG\Scripts\activate        # Windows
source RAG/bin/activate     # Mac/Linux
```

---

### Step 2 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3 — Install Ollama (Local LLM — No API Key Needed)

1. Download Ollama from: **https://ollama.com/download**
2. Run the installer
3. Open **CMD** and pull the model:

```bash
ollama run gemma4:e2b
```

> This downloads the model. Keep Ollama running in the background before launching the app.

To verify Ollama is running:

```bash
ollama list
```

You should see `gemma4:e2b` in the list.

---

### Step 4 — Install Tesseract OCR (for Image Support)

Tesseract is required to extract text from uploaded images (JPG, PNG, etc.).

#### Windows:

1. Download the installer from:
   **https://github.com/UB-Mannheim/tesseract/wiki**

2. Run the installer. During installation:
   - Check **"Additional language data"**
   - Select **Arabic** from the language list

3. After installation, copy the entire `Tesseract-OCR` folder and place it inside your project like this:

```
RAG_Telecom_Egypt/
└── Tesseract-OCR/
    └── tesseract.exe
```

4. The path is already configured in the code:

```python
pytesseract.pytesseract.tesseract_cmd = r"RAG_Telecom_Egypt\Tesseract-OCR\tesseract.exe"
```

> If you installed Tesseract in a different location, update this path in **Cell 9** of the notebook and in `app.py`.

#### Verify Tesseract works:

Open CMD and run:

```bash
tesseract --version
```

---

### Step 5 — Install ChromeDriver (for Web Scraping)

ChromeDriver is installed **automatically** via `webdriver-manager` when you run Cell 3 in the notebook.

> Just make sure **Google Chrome** is installed on your machine.

---

## Running the Project

### Option A — Jupyter Notebook (Full Pipeline)

```bash
jupyter notebook telecom_egypt.ipynb
```

Run cells **in order from top to bottom**:

| Cell | Description |
|------|-------------|
| Cell 0 | Imports & Configuration |
| Cell 1 | Define Telecom Egypt URLs |
| Cell 2 | Text cleaning function |
| Cell 3 | Scrape te.eg with Selenium *(run once only)* |
| Cell 4 | Split text into chunks |
| Cell 5 | Load multilingual embedding model |
| Cell 6 | Store vectors in ChromaDB *(run once only)* |
| Cell 7 | Test the retriever |
| Cell 8 | Initialize LLM & RAG chain |
| Cell 9 | File upload functions |
| Cell 10 | Launch Gradio interface |

> **Important:** Cells 3 and 6 only need to run **once** to build the index. On subsequent runs, skip directly to Cell 5 and load the existing ChromaDB.

### Option B — Standalone Gradio App

After running the notebook at least once to build the vector store:

```bash
python app.py
```

Then open your browser at: **http://127.0.0.1:7860**

---


## Knowledge Sources

| Category | Pages Scraped |
|----------|--------------|
| Mobile | Prepaid, Control WE MIX, WE Gold, Nitro Internet, Nitro MiFi |
| Home Internet | WE Internet, WE Landline, WE Air Prepaid, WE Air Postpaid |
| Promotions | Internet, Mobile, Landline, All Promotions |
| Business | WE Business, WE Business Value, Business ADSL, IP-VPN |
| Support | Help & Support |
| About | About Us, Contact Us |
| User Uploads | PDF, DOCX, TXT, HTML, Images |

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Web Scraping | Selenium + ChromeDriver |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |
| Embeddings | intfloat/multilingual-e5-large (1024 dims) |
| Vector Store | ChromaDB — persistent, on-premises |
| LLM | Ollama gemma4:e2b — fully offline |
| OCR | Tesseract (Arabic + English) |
| Interface | Gradio |

---


