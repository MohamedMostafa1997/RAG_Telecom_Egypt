CHROMA_DB_PATH = "./chroma_telecom_db"
COLLECTION_NAME = "telecom_egypt"

EMBEDDING_MODEL = "intfloat/multilingual-e5-large"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

OLLAMA_MODEL = "gemma4:e2b"  

TESSERACT_PATH = r"RAG_Telecom_Egypt\Tesseract-OCR\tesseract.exe"

TELECOM_URLS = {
    "mobile": [
        "https://te.eg/wps/portal/te/Personal/Mobile/Prepaid-12PT",
        "https://te.eg/wps/portal/te/Personal/Mobile/Control-WE-MIX",
        "https://te.eg/wps/portal/te/Personal/Mobile/WE-Gold",
        "https://te.eg/wps/portal/te/Personal/Mobile/Nitro-mobile-internet",
        "https://te.eg/wps/portal/te/Personal/Mobile/Nitro-mifi/",
    ],
    "home_internet": [
        "https://te.eg/wps/portal/te/Personal/WEInternet/",
        "https://te.eg/wps/portal/te/Personal/WELandline/",
        "https://te.eg/wps/portal/te/Personal/WE-Air-Prepaid",
        "https://te.eg/wps/portal/te/Personal/WE-Air-Postpaid",
    ],
    "promotions": [
        "https://te.eg/wps/portal/te/Personal/Promotions/Internet-Promotions/",
        "https://te.eg/wps/portal/te/Personal/Promotions/Mobile-Promotions/",
        "https://te.eg/wps/portal/te/Personal/Promotions/Landline-Promotions/",
        "https://te.eg/wps/portal/te/Personal/All-Promotions/",
    ],
    "support": [
        "https://te.eg/wps/portal/te/Personal/Help And Support",
    ],
    "business": [
        "https://te.eg/wps/portal/te/Business/Mobile-Services/WE-Business",
        "https://te.eg/wps/portal/te/Business/Mobile-Services/WE-Business-Value",
        "https://te.eg/wps/portal/te/Business/Mobile-Services/WE-Business-Internet",
        "https://te.eg/wps/portal/te/Business/Data-Connectivity/Business-ADSL",
        "https://te.eg/wps/portal/te/Business/Data-Connectivity/IP-VPN",
    ],
    "about": [
        "https://www.te.eg/wps/portal/te/About/About Us/",
        "https://www.te.eg/wps/portal/te/About/Contact Us/",
    ]
}