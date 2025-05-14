
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
    crawled = load_crawled_links()
    last_page = get_last_page()

    #P1 Crawl từ page 1 tìm link mới, dừng ngay khi gặp link cũ ===
    print("B1: Crawl từ đầu để tìm tin mới")
    page = 1
    stop_at_page = None

    while True:
        print(f"[B1] Trang {page}…")
        links = get_links_from_page(page)
        if not links:
            print("Không còn page nữa, dừng B1")
            break

        hit_old = False
        count_new = 0  # biến đếm số lượng link trong 1 page
        for link in links:
            if link in crawled:
                print("Gặp link cũ, dừng B1 tại page", page)
                hit_old = True
                break
            crawl_detail(link)
            save_new_links(link)
            crawled.add(link)
            count_new += 1
            time.sleep(1)

        
        print(f"[B1] → Đã crawl {count_new} tin đăng ở trang {page}")

        if hit_old:
            stop_at_page = page
            break

        page += 1
        time.sleep(1)
        # Lưu lại page dừng (nếu không dừng vì link cũ, dùng page cuối)
        new_last_page = max(last_page, stop_at_page or page)
        save_last_page(new_last_page)
        print(f"B1 kết thúc, last_page = {new_last_page}")


    # === PHASE 2: Tiếp tục từ last_page, bỏ qua link cũ, crawl link mới ===
    print("\nB2: Tiếp tục từ page cũ để bắt link new")
    page = last_page
    while True:
        print(f"[B2] Trang {page}…")
        links = get_links_from_page(page)
        if not links:
            print("Không còn page nữa, dừng B2")
            break

        any_new = False
        count_new = 0  # Biến đếm số tin đăng của 1 trang
        for link in links:
            if link in crawled:
                continue
            crawl_detail(link)
            save_new_links(link)
            crawled.add(link)
            any_new = True
            count_new += 1
            time.sleep(1)

        print(f"[B2] → Đã crawl {count_new} tin đăng ở trang {page}")
        page += 1
        save_last_page(page)

        if not any_new:
            print("Trang này không có link mới, chuyển sang page", page)

    print("Hoàn thành crawl.")

if __name__ == "__main__":
    main()
