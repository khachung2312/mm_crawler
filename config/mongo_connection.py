
from pymongo import MongoClient

# Kết nối đến MongoDB
def get_mongo_connection(uri="mongodb://localhost:27017/"):
    try:
        client = MongoClient(uri)
        db = client['mm_crawler']  # Kết nối tới database 'mm_crawler'
        # Kiểm tra kết nối
        client.admin.command('ping')  # Thực hiện lệnh ping để kiểm tra kết nối
        print("Kết nối MongoDB thành công!") 
        return db
    except Exception as e:
        print(f"Lỗi kết nối MongoDB: {e}")
        return None

# Hàm lấy collection cụ thể
def get_collection(collection_name):
    db = get_mongo_connection()
    if db:
        collection = db[collection_name]
        return collection
    else:
        return None
