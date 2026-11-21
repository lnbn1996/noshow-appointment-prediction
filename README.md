# noshow-appointment-prediction

Dự đoán bệnh nhân vắng mặt lịch hẹn khám (no-show) bằng học máy trên dữ liệu đặt lịch công khai. Bài thực hành cá nhân môn *Năng lực số nâng cao* (CT999), cao học CNTT, Trường Đại học Cần Thơ.

## Mục tiêu
1. Mô hình học máy đơn giản dự đoán vắng mặt tốt đến đâu khi chỉ dùng thông tin có sẵn lúc đặt lịch?
2. Yếu tố nào liên quan nhiều nhất đến việc vắng mặt?

## Phương pháp
- Làm sạch dữ liệu (bỏ 1 dòng tuổi âm, 5 dòng ngày khám trước ngày đặt), tạo biến `lead_days` (số ngày đặt trước) và thứ trong tuần.
- Chia 80% huấn luyện / 20% kiểm tra, phân tầng theo nhãn, `random_state=42`.
- So sánh hồi quy logistic, cây quyết định (độ sâu 6) và rừng ngẫu nhiên (200 cây), đều dùng trọng số lớp cân bằng.
- Chỉ số: accuracy, precision, recall, F1, AUC.

## Kết quả chính (tập kiểm tra 22.105 lượt hẹn, lớp dương = vắng mặt)

| Mô hình | AUC | Recall | Precision | F1 |
|---|---|---|---|---|
| Hồi quy logistic | 0,664 | 0,558 | 0,313 | 0,401 |
| Cây quyết định | 0,719 | 0,806 | 0,304 | 0,441 |
| Rừng ngẫu nhiên | 0,723 | 0,829 | 0,303 | 0,443 |

Số ngày đặt trước là biến quan trọng nhất (0,78). Chi tiết ở `docs/bai_bao_overleaf.pdf`.

## Cấu trúc thư mục
```
data/      chỉ chứa hướng dẫn tải dữ liệu (không đăng lại dữ liệu gốc)
src/       phan_tich_noshow.py: huấn luyện, đánh giá, sinh hình
results/   ket_qua.json và các hình PNG; results/poster/ là bản hình lớn cho poster
docs/      bài báo (PDF), báo cáo so sánh giấy phép
```

## Cách chạy
```
pip install -r requirements.txt
# tải dữ liệu theo data/README.md, đặt data/KaggleV2-May-2016.csv.zip
python src/phan_tich_noshow.py            # hình và ket_qua.json vào results/
python src/phan_tich_noshow.py --poster   # hình chữ to, 400 dpi, vào results/poster/
```

## Giấy phép
- **Mã nguồn và tài liệu do tác giả viết:** [MIT](LICENSE).
- **Dữ liệu:** *Medical Appointment No Shows* (Joni Hoppen, Kaggle) theo **CC BY-NC-SA 4.0**, không thuộc giấy phép MIT của repo này và không được đăng lại ở đây. Chỉ dùng phi thương mại, phải ghi nguồn. Xem `data/README.md`.

## Đạo đức dữ liệu
Dữ liệu đã được mã hóa mã bệnh nhân từ nguồn. Repo không cố nhận diện lại cá nhân. Mô hình chỉ ở mức xếp hạng rủi ro để ưu tiên nhắc lịch, không dùng để từ chối hay đặt chồng lịch tự động (precision khoảng 0,30).

## Trích dẫn
Xem [CITATION.cff](CITATION.cff). Đóng góp: xem [CONTRIBUTING.md](CONTRIBUTING.md).
