import os

os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

LINK_FILE = "data/bonbanh_links.txt"
PAGE_FILE = "logs/last_page.txt"
LAST_LINK_FILE = "logs/last_link.txt"

def load_crawled_links() -> set:
    """Đọc tất cả link đã crawl từ LINK_FILE, trả về set."""
    if not os.path.exists(LINK_FILE):
        return set()
    with open(LINK_FILE, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())
    
def save_new_links(link: str):
    """Ghi thêm 1 link mới vào LINK_FILE ngay lập tức."""
    with open(LINK_FILE, "a", encoding="utf-8") as f:
        f.write(link + "\n")

def get_last_page() -> int:
    """Đọc page cuối cùng đã crawl; nếu chưa có, trả về 1."""
    try:
        with open(PAGE_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            return int(content) if content.isdigit() else 1
    except FileNotFoundError:
        return 1


def save_last_page(page: int):
    """Ghi page hiện tại vào PAGE_FILE."""
    with open(PAGE_FILE, "w", encoding="utf-8") as f:
        f.write(str(page))
