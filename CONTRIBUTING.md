# Hướng dẫn đóng góp

Cảm ơn bạn đã quan tâm. Repo này là bài thực hành học tập, nhưng góp ý và sửa lỗi đều được hoan nghênh.

## Báo lỗi hoặc đề xuất
1. Mở một *issue* mô tả vấn đề: bạn đã chạy lệnh nào, kết quả mong đợi và kết quả thực tế, phiên bản Python và scikit-learn.
2. Nếu lỗi liên quan đến số liệu trong bài, ghi rõ số ở `results/ket_qua.json` và số bạn thu được.

## Gửi thay đổi (pull request)
1. Fork repo và tạo nhánh từ `main`, ví dụ `fix/ten-loi` hoặc `feat/ten-tinh-nang`.
2. Giữ thay đổi nhỏ, một mục đích mỗi pull request.
3. Chạy lại `python src/phan_tich_noshow.py` và bảo đảm chạy không lỗi; cập nhật `results/` nếu số liệu đổi.
4. Mô tả thay đổi và lý do trong pull request.

## Quy ước
- Python 3.10 trở lên, mã theo PEP 8, đặt `random_state` cố định để tái lập được.
- Không đưa dữ liệu gốc (CSV) vào repo: dữ liệu theo giấy phép CC BY-NC-SA 4.0, xem `data/README.md`.
- Không thêm thông tin định danh bệnh nhân dưới bất kỳ hình thức nào.
- Đóng góp mã sẽ theo giấy phép MIT của repo.
