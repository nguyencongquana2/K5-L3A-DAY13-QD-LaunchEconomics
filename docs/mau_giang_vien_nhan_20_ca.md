# Bài mẫu giảng viên phân loại 20 ca lỗi

Tài liệu này là đáp án minh hoạ dành cho giảng viên, không phải bộ nhãn độc lập của Nguyễn Công Quân hoặc Nguyễn Văn Đăng. Học viên cần hoàn thành hai bộ nhãn độc lập trước khi xem mẫu.

Nguyên tắc: gắn nhãn theo **nguyên nhân gốc**, không theo chỗ cần sửa. Nhãn **Ngầm** chỉ dùng khi sai lệch không được khách, nhân viên hoặc hệ thống nhận ra cho tới khi kiểm tra mẫu hay chi phí.

| Ca | Nhãn mẫu | Lý do theo nguyên nhân gốc |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu hai chữ số trong số tài khoản; lỗi bắt đầu từ dữ liệu đầu vào của người dùng. |
| 2 | Hệ thống | Trợ lý truyền sai tham số hàng thường thay vì hàng nặng, dẫn tới hoàn thiếu so với chính sách. |
| 3 | Ngữ cảnh | Trợ lý hoàn đúng vào ví LogiX theo thiết kế, nhưng kênh nhận tiền không khớp kỳ vọng tài khoản ngân hàng của khách. |
| 4 | Giới hạn hệ thống | LogiX không có dữ liệu của chặng do hãng nước ngoài giao nên trợ lý không thể xác định trạng thái. |
| 5 | Ngầm | Hệ thống hoàn thừa tiền nhưng không khách nào báo và không cảnh báo nào kích; lỗi chỉ lộ qua kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn sai luồng “giao trễ” trong khi vấn đề thật là hàng vỡ; đầu vào phân loại của người dùng sai. |
| 7 | Hệ thống | API ghi sổ thất bại nhưng trợ lý vẫn thông báo đã hoàn thành, trái với trạng thái thực của hệ thống. |
| 8 | Hệ thống | Trợ lý viện dẫn một điều khoản không tồn tại; lỗi đã hiện trực tiếp trong câu trả lời dù số tiền vẫn đúng. |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thay cho mã vận đơn; nguyên nhân gốc là dùng sai loại mã đầu vào. |
| 10 | Ngữ cảnh | Quyết định từ chối đúng chính sách bất khả kháng, nhưng mâu thuẫn với thông điệp “cam kết giao 24 giờ” mà khách đang thấy. |
| 11 | Giới hạn hệ thống | Trợ lý không có khả năng xử lý âm thanh nên không thể đọc tin nhắn thoại 40 giây. |
| 12 | Ngầm | Kết quả vẫn đúng nhưng lỗi dữ liệu làm chi phí token tăng gấp ba trong ba tuần mà không ai phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý; bản thân yêu cầu vượt khả năng được thiết kế. |
| 14 | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền, khiến yêu cầu bị đóng do thao tác sai của người dùng. |
| 15 | Hệ thống | Chính sách quy định hoàn 50% nhưng trợ lý tính 100%; lỗi tính toán đã được nhân viên phát hiện khi xem lại. |
| 16 | Ngữ cảnh | Trợ lý làm đúng thiết kế “gửi ngay khi xong”, nhưng thời điểm 2:14 sáng không phù hợp hoàn cảnh của khách. |
| 17 | Ngầm | Bộ nhớ đệm dùng bảng giá cũ gây lệch tiền trên 212 đơn nhưng không ai mở lại; sai lệch tồn tại mà chưa được nhận ra. |
| 18 | Ngữ cảnh | Số tiền 15.000 đ đúng chính sách, nhưng thiếu cách tính khiến khách hiểu nhầm là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Dữ liệu chỉ truy cập được 12 tháng trong khi đơn đã 14 tháng; trợ lý không thể tra ngoài cửa sổ dữ liệu. |
| 20 | Hệ thống | Thiếu khoá chống trùng làm trợ lý thực hiện hai lệnh hoàn cho cùng một đơn; đây là lỗi thiết kế hệ thống. |

## Tổng hợp

| Loại | Các ca | Số ca |
| --- | --- | ---: |
| Do người dùng | 1, 6, 9, 14 | 4 |
| Hệ thống | 2, 7, 8, 15, 20 | 5 |
| Ngữ cảnh | 3, 10, 16, 18 | 4 |
| Giới hạn hệ thống | 4, 11, 13, 19 | 4 |
| Ngầm | 5, 12, 17 | 3 |

## Các điểm nên thảo luận trên lớp

- Ca 6 và 9 là **Do người dùng** vì nguyên nhân gốc là chọn sai mục hoặc nhập sai mã; việc trợ lý không hướng dẫn tốt thuộc phần khắc phục.
- Ca 8 và 15 là **Hệ thống**, không phải Ngầm, vì sai lệch đã lộ trong câu trả lời hoặc đã được nhân viên bắt được.
- Ca 12 là **Ngầm** dù kết quả đúng, vì sai lệch nằm ở chi phí và kéo dài ba tuần mà không ai nhận ra.
- Ca 13 là **Giới hạn hệ thống** vì yêu cầu nằm ngoài phạm vi, dù cách trợ lý diễn đạt giới hạn đó chưa tốt.
- Ca 18 là **Ngữ cảnh** vì phép tính đúng nhưng thông tin giải thích không đủ cho hoàn cảnh của khách.
