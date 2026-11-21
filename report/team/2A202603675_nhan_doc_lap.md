# Phiếu gắn nhãn độc lập mẫu của Nguyễn Công Quân

Phiếu này là bài mẫu học viên dùng để tham khảo CP3. Nó không chứng minh việc gắn nhãn độc lập của Nguyễn Công Quân và không được dùng để tính tỉ lệ đồng thuận với nhãn của Nguyễn Văn Đăng.

Năm nhãn được phép dùng:

- **Do người dùng:** đầu vào hoặc thao tác của người dùng sai.
- **Hệ thống:** trợ lý làm sai thiết kế hoặc chính sách và lỗi đã lộ ra.
- **Ngữ cảnh:** trợ lý làm đúng thiết kế nhưng kết quả không phù hợp hoàn cảnh người dùng.
- **Giới hạn hệ thống:** thiếu dữ liệu, ngoài phạm vi hoặc không xử lý được đầu vào.
- **Ngầm:** có sai lệch nhưng không ai nhận ra cho tới khi kiểm tra mẫu hoặc chi phí.

Gắn theo nguyên nhân gốc, không gắn theo chỗ cần sửa.

| Ca | Mô tả | Nhãn của Quân | Lý do ngắn |
| --: | --- | --- | --- |
| 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. | Do người dùng | Khách nhập thiếu dữ liệu tài khoản nên nguyên nhân gốc nằm ở đầu vào. |
| 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. | Hệ thống | Trợ lý truyền sai tham số loại hàng và tính sai mức hoàn. |
| 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”. | Ngữ cảnh | Trợ lý làm đúng thiết kế nhưng kênh nhận tiền không khớp kỳ vọng của khách. |
| 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. | Giới hạn hệ thống | LogiX không có dữ liệu chặng nước ngoài nên trợ lý không thể xử lý. |
| 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. | Ngầm | Hoàn thừa nhưng không ai nhận ra cho tới khi kiểm tra mẫu. |
| 6 | Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. | Do người dùng | Khách chọn sai loại yêu cầu nên trợ lý đi vào luồng không phù hợp. |
| 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”. | Hệ thống | Ghi sổ thất bại nhưng trợ lý báo thành công, sai trạng thái thực tế. |
| 8 | Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. | Hệ thống | Trợ lý viện dẫn điều khoản không tồn tại và lỗi đã lộ trong câu trả lời. |
| 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì. | Do người dùng | Khách dùng sai loại mã đầu vào. |
| 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”. | Ngữ cảnh | Quyết định đúng chính sách nhưng không phù hợp thông tin cam kết khách đang thấy. |
| 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”. | Giới hạn hệ thống | Trợ lý không có khả năng xử lý đầu vào âm thanh. |
| 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. | Ngầm | Chi phí tăng bất thường kéo dài nhưng không ai phát hiện. |
| 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. | Giới hạn hệ thống | Sản phẩm bảo hiểm đối tác nằm ngoài phạm vi trợ lý. |
| 14 | Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng. | Do người dùng | Yêu cầu bị đóng do thao tác xác nhận nhầm của khách. |
| 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. | Hệ thống | Trợ lý tính sai chính sách và nhân viên đã nhìn thấy lỗi. |
| 16 | Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. | Ngữ cảnh | Trợ lý đúng thiết kế nhưng thời điểm gửi không phù hợp hoàn cảnh khách. |
| 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. | Ngầm | Dùng bảng giá cũ gây sai hàng loạt nhưng không ai nhận ra. |
| 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. | Ngữ cảnh | Số tiền đúng nhưng thiếu giải thích khiến khách hiểu sai. |
| 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. | Giới hạn hệ thống | Đơn nằm ngoài cửa sổ dữ liệu 12 tháng mà trợ lý truy cập được. |
| 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. | Hệ thống | Thiếu khoá chống trùng làm hệ thống hoàn hai lần cùng một đơn. |

Hai thành viên chỉ được tính tỉ lệ đồng thuận từ các bộ nhãn do họ tự hoàn thành độc lập trước khi đối chiếu.
