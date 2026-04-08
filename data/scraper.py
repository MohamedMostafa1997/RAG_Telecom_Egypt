import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from langchain_core.documents import Document
from webdriver_manager.chrome import ChromeDriverManager
from langchain_core.documents import Document
from selenium.webdriver.chrome.service import Service

from data.cleaner import clean_text

def load_telecom_docs(url_dict):
    all_docs = []
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--lang=ar")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    for category, urls in url_dict.items():
        for url in urls:
            try:
                driver.get(url)
                time.sleep(3)
                text = driver.find_element("tag name", "body").text
                text = clean_text(text)
                if len(text) > 100:
                    doc = Document(
                        page_content=text,
                        metadata={"source": url, "category": category, "source_site": "te.eg"}
                    )
                    all_docs.append(doc)
                else:
                    print(f"Empty: {url.split('/')[-1]}")
            except Exception as e:
                print(f"Failed: {url} - {e}")
    driver.quit()
    print(f"Total documents loaded: {len(all_docs)}")
    return all_docs