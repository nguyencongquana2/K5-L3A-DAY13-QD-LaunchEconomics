# Báo cáo cá nhân — Nguyễn Văn Đăng — 2A202603371

> Bản nháp Codex chuẩn bị theo yêu cầu hoàn thiện phần việc của Đăng. Đăng cần tự kiểm tra, xác nhận đóng góp thực tế và sửa báo cáo trước khi nộp; nội dung dưới đây không thay cho hai bộ nhãn độc lập hay buổi duyệt chéo.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Đăng
- MSSV: 2A202603371
- Email: nguyenvandang2201@gmail.com
- Vai trò được phân công: người kiểm số; người gắn nhãn 2 kiêm giữ hồ sơ; tiếp quản code CP4–CP5.

## 2. Phần việc phụ trách

- Kiểm tra số A–B và bảng `bang_chi_phi.md`.
- Gắn độc lập 20 ca lỗi, sau đó cùng người gắn nhãn 1 so nhãn và thống nhất bảng khắc phục.
- Tính năm câu D1; soạn kế hoạch pilot, kiểm tra YAML và điều kiện dừng.
- Giữ hồ sơ launch v0, ghép số và đề xuất cuối theo bằng chứng; tham gia duyệt chéo.

## 3. Bằng chứng hiện có trong repo

- `src/lab13.py` in A1–B4, E1 và đủ năm kết quả D1. A2 cho 4.472 đ/việc thành công (simulated); D1 cho 1.251 yêu cầu/nhóm ở MDE 5 điểm và 859 hiệu dụng/nhóm ở MDE 6 điểm.
- `report/team/bang_chi_phi.md` đã ghi bảng A1–B4 và nhãn simulated ở các khoản dùng phút giả lập.
- `report/team/pilot_plan.yaml` đã điền cách chia 20 nhân viên/nhóm, 299 yêu cầu/người, ba luật dừng và đánh đổi power khoảng 0,64 nếu tác động thật 5 điểm.
- `report/team/ho_so_launch_v0.md` đã tổng hợp bảy mục và đề xuất No-go theo bằng chứng hiện tại.

Các file trên được Codex tạo hoặc cập nhật theo yêu cầu người dùng. Đăng cần xác nhận phần nào mình đã tự kiểm tra hoặc đóng góp trước khi nhận là công việc cá nhân.

## 4. Cách tự kiểm tra cần xác nhận

- Chạy `cd src` rồi `python -X utf8 lab13.py`; đối chiếu A1 = 1,20 · 1,25 · 1,25, A2 = 4.472 đ (simulated), D1 = 1.251 · 3.103 · 1.000 · 300 · 299.
- Chạy `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"` trong `src/`, sau đó kiểm tra không còn dấu hỏi trong YAML.
- Tự tính tay ít nhất một khoản, ví dụ 890 phút xem lại × 2.000 đ/phút = 1.780.000 đ (simulated), rồi ghi rõ đã thực hiện.

## 5. Công cụ AI đã dùng

Codex được người dùng yêu cầu hỗ trợ rà repo, điền bảng số có thể tái lập, viết công thức cỡ mẫu và lập bản nháp kế hoạch/hồ sơ. Đăng cần xác nhận công cụ mình thực sự dùng và cách mình tự kiểm tra trong lần nộp cuối.

## 6. Việc cần Đăng tự hoàn thành

- Gắn độc lập 20 ca vào cột người 2 trong `bang_loi.md` trước khi xem nhãn người 1; hai người chỉ so nhãn sau khi cả hai bộ đã khóa.
- Cùng nhóm xác nhận năm dòng khắc phục; không điền tỉ lệ đồng thuận khi chưa có hai bộ nhãn.
- Điền `phieu_cham.md` theo hồ sơ nhóm khác và kết quả buổi duyệt chéo thực tế; không tự tạo điểm.
- Kiểm tra lại các con số, phạm vi và đề xuất No-go; ghi đóng góp thật sự của mình vào báo cáo này.
