# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Công Quân · Người gắn nhãn 2: Nguyễn Văn Đăng. Trong kịch bản bài mẫu, bộ 20 nhãn người 1 của Quân đã được chép từ `2A202603675_nhan_doc_lap.md`; nhãn người 2 của Đăng chưa được nộp nên chưa tính đồng thuận hoặc nhãn thống nhất.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** chưa tính; đã có 20/20 nhãn người 1, còn chờ 20/20 nhãn người 2.

## Nhãn đề xuất để hai thành viên kiểm tra

Đây là bản dự thảo do Codex tổng hợp từ mô tả 20 ca và đối chiếu với `docs/mau_giang_vien_nhan_20_ca.md`. **Không dùng cột này làm nhãn độc lập của Quân hoặc Đăng, nhãn thống nhất hay tỉ lệ đồng thuận.**

| Ca | Nhãn đề xuất | Lý do chính |
| --: | --- | --- |
| 1 | Do người dùng | Số tài khoản do khách nhập thiếu hai chữ số. |
| 2 | Hệ thống | Trợ lý truyền sai tham số hàng nặng và hoàn thiếu tiền. |
| 3 | Ngữ cảnh | Hoàn về ví đúng thiết kế nhưng khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX không có dữ liệu chặng nước ngoài. |
| 5 | Ngầm | Hoàn thừa do mã giảm giá, chỉ lộ khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn sai loại yêu cầu. |
| 7 | Hệ thống | Ghi sổ thất bại nhưng trợ lý báo đã hoàn. |
| 8 | Hệ thống | Trợ lý dẫn điều khoản không tồn tại trong câu trả lời. |
| 9 | Do người dùng | Khách nhập mã đơn thay cho mã vận đơn. |
| 10 | Ngữ cảnh | Từ chối đúng chính sách nhưng mâu thuẫn với cam kết khách thấy. |
| 11 | Giới hạn hệ thống | Trợ lý không xử lý được âm thanh. |
| 12 | Ngầm | Chi phí token tăng gấp ba mà không ai phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm đối tác ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền. |
| 15 | Hệ thống | Trợ lý tính 100% thay vì 50% theo chính sách. |
| 16 | Ngữ cảnh | Thông báo lúc 2:14 sáng đúng thiết kế nhưng làm phiền khách. |
| 17 | Ngầm | Bảng giá cũ gây sai lệch hàng loạt mà không ai mở lại. |
| 18 | Ngữ cảnh | Tiền hoàn đúng nhưng thiếu giải thích cách tính. |
| 19 | Giới hạn hệ thống | Đơn 14 tháng vượt cửa sổ dữ liệu 12 tháng. |
| 20 | Hệ thống | Thiếu khóa chống trùng nên hoàn hai lần cho một đơn. |

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chưa có hai bộ nhãn độc lập để xác định các ca không trùng; chỉ viết quy tắc sau khi hai người đã khóa nhãn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Năm dòng dưới đây là **phương án khắc phục đề xuất**, dùng nhãn tham khảo ở trên; nhóm cần xác nhận sau khi hoàn thành hai bộ nhãn độc lập.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Mỗi ngày đếm `refund_ledger_write.error_code = tai_khoan_khong_hop_le`; ngưỡng từ 1 ca | Kiểm tra định dạng tài khoản trước khi tạo lệnh; yêu cầu khách nhập và xác nhận lại, rồi mới thử hoàn | Trưởng nhóm CSKH |
| 20 | Hệ thống | Mỗi lần ghi sổ, cảnh báo nếu một `request_id` có từ 2 `refund_ledger_write.ket_qua = thanh_cong` trong 24 giờ | Bắt buộc `idempotency_key` theo yêu cầu gốc; chặn lệnh thứ hai và đối soát, hoàn tác khoản trùng | Kỹ sư sổ cái |
| 18 | Ngữ cảnh | Mỗi tuần rà mọi `ticket_reopened.reason = hoan_thieu` có `audit_sample_checked` xác nhận số tiền đúng | Ghi rõ phí gốc, tỉ lệ hoàn và phép tính trong thông báo; thử lại mẫu tin với nhân viên CSKH | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Kiểm tra tuổi đơn khi tạo yêu cầu; mọi đơn trên 12 tháng phải có `handoff_to_staff.reason = qua_12_thang` | Nói rõ giới hạn dữ liệu, chuyển nhân viên kèm tóm tắt và không tự đoán trạng thái | PM trợ lý hoàn phí |
| 5 | Ngầm | Kiểm tra mẫu hằng tuần bằng `audit_sample_checked`; cảnh báo ngay nếu `so_tien_da_hoan` khác `so_tien_dung` từ 1 ca | Dừng luồng tính hoàn có mã giảm giá, sửa thứ tự áp dụng giảm giá và đối soát các giao dịch liên quan | Kế toán đối soát |
