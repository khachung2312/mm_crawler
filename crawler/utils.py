import os

LINK_FILE = "data/bonbanh_links.txt"
PAGE_FILE = "logs/last_page.txt"

def load_crawled_links():
    if not os.path.exists(LINK_FILE):
        return set()
    with open(LINK_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())
    
def save_new_links(links):
    with open(LINK_FILE, "a", encoding="utf-8") as f:
        for link in links:
            f.write(links)

def get_last_page():
    if not os.path.exists(PAGE_FILE):
        return 1
    with open(PAGE_FILE, "r") as f:
        return int(f.read().strip())

def save_last_page(page):
    with open(PAGE_FILE, "w") as f:
        f.write(str(page))