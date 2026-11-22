# Dữ liệu

Thư mục này chứa bộ dữ liệu của **bên thứ ba**, dùng theo giấy phép riêng của nó (**CC BY-NC-SA 4.0**), khác với giấy phép MIT của mã nguồn trong repo.

## Nguồn và giấy phép (ghi nguồn đầy đủ)

| Mục | Nội dung |
|---|---|
| Tên bộ dữ liệu | *Medical Appointment No Shows* |
| Tác giả | Joni Hoppen (tài khoản Kaggle `joniarroba`) |
| Nguồn gốc dữ liệu | Lịch hẹn khám tại các bệnh viện công ở Vitória, bang Espírito Santo, Brazil (theo mô tả trên Kaggle và các nghiên cứu dùng bộ này) |
| Trang gốc | https://www.kaggle.com/datasets/joniarroba/noshowappointments |
| Tệp trong thư mục | `KaggleV2-May-2016.csv` (110.527 dòng, 14 cột, 10.739.535 byte) |
| Giấy phép | **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**: https://creativecommons.org/licenses/by-nc-sa/4.0/ |
| Ngày tải | 21/11/2026 |
| Chỉnh sửa | **Không.** Tệp được đưa vào nguyên vẹn. Đối chiếu SHA-256 với tệp trong file zip tải từ Kaggle: `9132d3e7d0246617df9041d3764f20ad6f08e7b0d9f0997fa254fc5e52eda27d` |

Mẫu ghi nguồn khi dùng lại:

> Hoppen, J. *Medical Appointment No Shows*. Kaggle. https://www.kaggle.com/datasets/joniarroba/noshowappointments. Giấy phép CC BY-NC-SA 4.0.

## Điều kiện khi dùng và chia sẻ lại
- **Ghi nguồn (BY):** nêu tác giả, link nguồn và giấy phép như trên; ghi rõ nếu bạn có chỉnh sửa dữ liệu.
- **Phi thương mại (NC):** không dùng cho mục đích thương mại.
- **Chia sẻ tương tự (SA):** bản chia sẻ lại hoặc bản chỉnh sửa của dữ liệu này phải giữ cùng giấy phép CC BY-NC-SA 4.0.
- Không có bảo đảm nào về dữ liệu. Mã bệnh nhân trong dữ liệu đã được mã hóa từ nguồn; không được cố nhận diện lại cá nhân.

Giấy phép MIT của repo (tệp `LICENSE` ở thư mục gốc) **chỉ áp dụng cho mã nguồn và tài liệu do tác giả repo viết**, không áp dụng cho các tệp trong thư mục `data/`. Xem thêm tệp [`LICENSE`](LICENSE) trong thư mục này.

## Cách lấy dữ liệu để chạy
Tệp `KaggleV2-May-2016.csv` đã có sẵn trong thư mục này, chạy trực tiếp được:
```
python src/phan_tich_noshow.py
```
Nếu bạn xóa tệp hoặc muốn dùng bản mới nhất, tải lại từ trang Kaggle ở trên (cần tài khoản Kaggle), giải nén và đặt `KaggleV2-May-2016.csv` (hoặc file zip, tên nào cũng được miễn bên trong có tệp CSV đó) vào thư mục này. Script tự tìm dữ liệu trong `data/` và báo cách tải nếu không thấy.

Lưu ý: giá trị `Yes` ở cột `No-show` nghĩa là bệnh nhân **vắng mặt**.
