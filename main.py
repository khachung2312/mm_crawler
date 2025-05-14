"""
main.py
"""
from crawler.crawl_tindangxe_links import get_links_from_page
from crawler.crawl_tindangxe_details import crawl_detail
from crawler.utils import (
    load_crawled_links,
    save_new_links,
    get_last_page,
    save_last_page,
)
import time

def main():
    crawled_links = load_crawled_links()  # từ bonbanh_links.txt
    last_page = get_last_page()  # ví dụ: 500

    # 1. Crawl link mới từ page 1 đến gặp link đã crawl
    new_links = []
    page = 1
    while True:
        print(f"Crawling new links page {page}")
        links = get_links_from_page(page)
        if not links:
            break

        fresh_links = [l for l in links if l not in crawled_links]
        if not fresh_links:
            break

        new_links.extend(fresh_links)
        page += 1
        time.sleep(1)

    # 2. Lưu và crawl chi tiết các link mới
    save_new_links(new_links)
    for link in new_links:
        crawl_detail(link)
        time.sleep(1)

    # 3. Tiếp tục từ page hôm qua
    page = last_page
    while True:
        print(f"Continuing from old page {page}")
        links = get_links_from_page(page)
        if not links:
            break

        fresh_links = [l for l in links if l not in crawled_links and l not in new_links]
        if not fresh_links:
            page += 1
            continue

        save_new_links(fresh_links)
        for link in fresh_links:
            crawl_detail(link)
            time.sleep(1)

        page += 1
        save_last_page(page)

if __name__ == "__main__":
    main()
