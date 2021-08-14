import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

target_names = ["Am nhac", "Am thuc", "Bat dong san", "Bong da", "Chung khoan", "Cum ga", 
                "Cuoc song do day", "Du hoc", "Du lich", "Duong vao WTO", "Gia dinh", 
                "Giai tri tin hoc", "Giao duc", "Gioi tinh", "Hackers va Virus",
                "Hinh su", "Khong gian song", "Kinh doanh quoc te", "Lam dep",
                "Loi song", "Mua sam", "My thuat", "San khau dien anh", "San pham tin hoc moi",
                "Tennis", "The gioi tre", "Thoi trang"]

classes = {
    "Am nhac": 0,
    "Am thuc": 1,
    "Bat dong san": 2,
    "Bong da": 3,
    "Chung khoan": 4,
    "Cum ga": 5,
    "Cuoc song do day": 6,
    "Du hoc": 7,
    "Du lich": 8,
    "Duong vao WTO": 9,
    "Gia dinh": 10,
    "Giai tri tin hoc": 11,
    "Giao duc": 12,
    "Gioi tinh": 13,
    "Hackers va Virus": 14,
    "Hinh su": 15,
    "Khong gian song": 16,
    "Kinh doanh quoc te": 17,
    "Lam dep": 18,
    "Loi song": 19,
    "Mua sam": 20,
    "My thuat": 21,
    "San khau dien anh": 22,
    "San pham tin hoc moi": 23,
    "Tennis": 24,
    "The gioi tre": 25,
    "Thoi trang": 26
}

vocab_size = 5000 
embedding_dim = 64
max_length = 400
trunc_type = 'post'
padding_type = 'post'
oov_tok = '<OOV>' #OOV = Out of Vocabulary

BATCH_SIZE = 32
NUM_EPOCHS = 50