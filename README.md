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

Số ngày đặt trước là biến quan trọng nhất (0,78). Số liệu đầy đủ ở `results/ket_qua.json`.

## Cấu trúc thư mục
```
data/      dữ liệu gốc KaggleV2-May-2016.csv (CC BY-NC-SA 4.0), kèm README.md và LICENSE ghi nguồn
src/       phan_tich_noshow.py: huấn luyện, đánh giá, sinh hình
results/   ket_qua.json và các hình PNG; results/poster/ là bản hình lớn cho poster
docs/      báo cáo so sánh giấy phép nguồn mở (PDF)
```

## Cách chạy
```
pip install -r requirements.txt
# dữ liệu đã có sẵn trong data/ (nếu thiếu, xem data/README.md để tải từ Kaggle)
python src/phan_tich_noshow.py            # hình và ket_qua.json vào results/
python src/phan_tich_noshow.py --poster   # hình chữ to, 400 dpi, vào results/poster/
```

## Giấy phép
Repo có hai phần với hai giấy phép khác nhau:
- **Mã nguồn và tài liệu do tác giả viết** (`src/`, `results/`, `docs/`, README...): [MIT](LICENSE).
- **Dữ liệu** trong `data/`: *Medical Appointment No Shows* của Joni Hoppen (Kaggle), giấy phép **CC BY-NC-SA 4.0**, đưa vào nguyên vẹn, không chỉnh sửa, và **không** thuộc giấy phép MIT. Chỉ dùng phi thương mại, phải ghi nguồn, bản chia sẻ lại giữ cùng giấy phép. Nguồn đầy đủ ở `data/README.md` và `data/LICENSE`.

## Đạo đức dữ liệu
Dữ liệu đã được mã hóa mã bệnh nhân từ nguồn. Repo không cố nhận diện lại cá nhân. Mô hình chỉ ở mức xếp hạng rủi ro để ưu tiên nhắc lịch, không dùng để từ chối hay đặt chồng lịch tự động (precision khoảng 0,30).

## Trích dẫn
Xem [CITATION.cff](CITATION.cff). Đóng góp: xem [CONTRIBUTING.md](CONTRIBUTING.md).
