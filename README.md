# Phân loại văn bản sử dụng phương pháp trích chọn đặc trưng TF-IDF kết hợp với thuật toán SVM, LSTM
## 1. Bộ dữ liệu
Bộ dữ liệu được sử dụng bao gồm 27 chủ đề được lấy tại link: https://github.com/duyvuleo/VNTC.
Tập huấn luyện (training) có khoảng 14375 đoạn văn
Tập kiếm tra (testing) có khoảng 12076 đoạn văn
## 2. Phương pháp giải quyết
- Trích xuất đặc trưng (feature extraction): Sử dụng phương pháp BOW: TF-IDF
- Lựa chọn đặc trưng (feature selection): Sử dụng phương pháp ChiSquare kết hợp với K-Best method (hệ số k = 25000)
- Mô hình sử dụng: Support Vector Machine (SVM), Long Short Term Memory (LSTM)
## 3. Kết quả đạt được
| Mô hình | Accuracy | F1-score |
|---------|----------|----------|
|   SVM   |   91%    |    90%   |
|   LSTM  |   94%    |    93%   |

