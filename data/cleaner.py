import re

def clean_text(text):
    start_markers = ["Investor Relations CSR"]
    for marker in start_markers:
        if marker in text:
            text = text[text.find(marker) + len(marker):]
    footer_markers = [
        "For all mobile, internet and fixed line users",
        "TELECOMEGYPT",
        "Follow Us",
        "Download Our App",
        "Copyright"
    ]
    for marker in footer_markers:
        if marker in text:
            text = text[:text.find(marker)]
    text = re.sub(r'\s+', ' ', text).strip()
    return text