
import requests
from bs4 import BeautifulSoup

def get_links_from_page(page_num: int):
    url = f"https://bonbanh.com/oto/page,{page_num}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException:
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    car_items = soup.select("li.car-item.row1, li.car-item.row2")  # ✅ đúng selector

    links = []

    for item in car_items:
        a_tag = item.find("a", href=True)
        if a_tag:
            link = "https://bonbanh.com/" + a_tag["href"]
            links.append(link)

    return links  
