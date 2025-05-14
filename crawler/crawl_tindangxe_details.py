import requests
from bs4 import BeautifulSoup
import json
from models.tindangxe import TinDangXe 
from mongoengine import connect



def crawl_detail(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return
    
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("title").text.strip() if soup.find("title") else ""

    # Lưu vào MongoDB
    tin_dang_xe = TinDangXe(
        url=url,
        title=title
    )
    tin_dang_xe.save()  # Lưu vào MongoDB

    with open ("data/bonbanh_details.jsonl", "a", encoding="utf-8") as f:
        json.dump({"url": url, "title": title}, f, ensure_ascii=False)
        f.write("\n")
        