import requests
from bs4 import BeautifulSoup
import json

def crawl_detail(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").text.strip() if soup.find("title") else ""

    with open ("data/bonbanh_details.jsonl", "a", encoding="utf-8") as f:
        json.dump({"url": url, "title": title}, f, ensure_ascii=False)
        f.write("\n")
        