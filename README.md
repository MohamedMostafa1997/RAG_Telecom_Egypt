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

## Notebook Markdown — What to Write in Each Cell

### Before Cell 0

```markdown
## Step 1 — Imports & Configuration
Import all required libraries and set global constants used throughout the pipeline.
> Run this cell first every time you open the notebook.
```

### Before Cell 1

```markdown
## Step 2 — Knowledge Base URLs
Define the Telecom Egypt pages to scrape, organized by category.
Each category is stored as metadata with every document — this enables filtered retrieval later.
```

### Before Cell 2

```markdown
## Step 3 — Text Cleaning
Remove navigation menus and footer noise that Selenium picks up alongside the main content.
- `start_markers` — cuts everything before the actual page content begins
- `footer_markers` — cuts everything after the page content ends
```

### Before Cell 3

```markdown
## Step 4 — Web Scraping with Selenium
Scrape all URLs using a headless Chrome browser.
We use Selenium because te.eg renders content dynamically with JavaScript.

Expected output:
- OK mobile: Prepaid-12PT
- OK mobile: Control-WE-MIX
- ...
- Total: 21 documents
```

### Before Cell 4

```markdown
## Step 5 — Chunking
Split documents into smaller chunks for embedding.
- `chunk_size=800` — large enough for context, small enough for accurate retrieval
- `chunk_overlap=150` — prevents information loss at chunk boundaries
- Arabic-aware separators ensure sentences are not cut mid-way
```

### Before Cell 5

```markdown
## Step 6 — Multilingual Embeddings
Convert each chunk into a 1024-dimensional vector using intfloat/multilingual-e5-large.
This model supports 50+ languages including Arabic and Egyptian dialect, and runs fully offline.
```

### Before Cell 6

```markdown
## Step 7 — Store in ChromaDB
Save all vectors to a persistent local database at ./chroma_telecom_db.
On subsequent runs, load it directly without re-indexing.
```

### Before Cell 7

```markdown
## Step 8 — Retriever
Search the vector store using MMR (Maximal Marginal Relevance).
MMR returns results that are both relevant AND diverse — avoids returning 5 chunks that say the same thing.
```

### Before Cell 8

```markdown
## Step 9 — LLM & RAG Chain
Initialize Ollama (gemma4:e2b) and build the full RAG chain.
The system prompt instructs the model to detect the user's language and reply in the same language automatically.
```

### Before Cell 9

```markdown
## Step 10 — User Document Upload
Allow users to upload their own documents (PDF, DOCX, TXT, HTML, Images).
Uploaded files are chunked and added to ChromaDB alongside te.eg content.
Images use Tesseract OCR to extract Arabic and English text.
```

### Before Cell 10

```markdown
## Step 11 — Gradio Interface
Launch the chat UI with WE brand colors.
Features: chat history, file upload, source citations, and a clear chat button.
Open http://127.0.0.1:7860 after running this cell.
```

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

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| `ChromeDriver version mismatch` | Update Chrome or run `pip install --upgrade webdriver-manager` |
| `tesseract is not installed` | Follow Step 4 and verify the path in the code |
| `ollama: command not found` | Make sure Ollama is installed and added to PATH |
| `model not found` | Run `ollama run gemma4:e2b` in CMD first |
| `chroma_telecom_db not found` | Run Cells 0–6 in the notebook to build the index |
| Empty responses from LLM | Make sure Ollama is running in the background |
| Image upload returns no text | Make sure Arabic language pack is installed in Tesseract |

---

## Customer Support

For inquiries not answered by the chatbot, contact WE customer support: **16161**
