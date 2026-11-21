# Báo cáo cá nhân — Nguyễn Công Quân — 2A202603675

## 1. Thông tin thành viên

- Họ tên: Nguyễn Công Quân
- MSSV: 2A202603675
- Email: nguyencongquancn06@gmail.com
- Vai trong nhóm: người viết code CP1–CP2; người gắn nhãn 1

## 2. Phần việc phụ trách

- Cài môi trường và triển khai các phép tính A1–A4, B1–B4 trong `src/lab13.py`.
- Kiểm tra công thức cỡ mẫu và hệ số thiết kế của CP4.
- Soạn đặc tả chỉ số, event, rủi ro kinh tế và báo cáo nhóm.
- Gắn độc lập 20 ca lỗi với vai trò người gắn nhãn 1; phần này chưa thực hiện và không được điền thay bằng AI.

## 3. Đóng góp cụ thể

- Hoàn thiện ba hàm A1 và hàm mô hình chi phí; thêm kiểm tra đầu vào để tránh xác suất hoặc giới hạn lần chạy không hợp lệ.
- Viết phần chạy tạo bảng A2–A4, chín kịch bản B1, kịch bản kết hợp B2, giới hạn chạy lại B3, xem lại 100% B4 và ba chỉ số E1.
- Hoàn thiện `chi_so.md` với năm chỉ số, mười event có `trace_id`, kiểm tra chéo event và ba rủi ro kinh tế.
- Soạn `group_report.md` theo bằng chứng hiện có và đánh dấu rõ các phần chưa hoàn thành.
- Sau khi ghép phần của Nguyễn Văn Đăng, chạy lại toàn bộ `lab13.py`, kiểm tra cú pháp Python, xác thực `pilot_plan.yaml`, ba luật dừng và các placeholder còn lại.
- Chuẩn bị `2A202603675_nhan_doc_lap.md` từ 20 ca trong đề gốc để gắn nhãn CP3 độc lập; phiếu không chứa đáp án hoặc nhãn của người thứ hai.

## 4. Bằng chứng

- `src/lab13.py` chạy hết và in `Ba phép thử đáp án biết trước: ĐẠT`.
- Kết quả chính: 4.472 đ mỗi việc thành công (simulated); giới hạn hai lần chạy cho tổng chi phí hệ thống 6.901.220 đ (simulated); chỉ số thử 82,83%, 27,12% và 4,25%.
- Kiểm tra CP4: 1.251 yêu cầu mỗi nhóm; DE = 2,48 với 75 yêu cầu/nhân viên; cần 42 nhân viên mỗi nhóm nên không đủ 40 người; với mức chênh 6 điểm cần 299 yêu cầu/nhân viên.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, có ba luật dừng và không còn dấu `?` ngoài chú thích; không tìm thấy từ bị cấm trong hồ sơ nhóm.
- File bằng chứng: `src/lab13.py`, `report/team/chi_so.md`, `report/team/group_report.md`, `report/team/2A202603675_nhan_doc_lap.md`.

## 5. Công cụ AI đã dùng

Sử dụng Codex để hỗ trợ đọc yêu cầu, triển khai code, soát công thức và định dạng báo cáo. Kết quả được tự kiểm tra bằng ba phép thử A1, chạy `lab13.py` trên hai CSV của repo, đối chiếu các mốc sai số 2% trong hướng dẫn và không dùng AI để tạo hai bộ nhãn độc lập hoặc kết quả duyệt chéo.

## 6. Tự đánh giá

Phần code CP1–CP2, hồ sơ chỉ số và kiểm tra tích hợp sau khi ghép bài đã có output tái lập được. Hồ sơ hiện đề xuất No-go có căn cứ vì chưa có hai bộ nhãn CP3 độc lập; Quân vẫn phải tự hoàn thành bộ nhãn số 1 và tham gia duyệt chéo trước khi nộp bản chốt.
