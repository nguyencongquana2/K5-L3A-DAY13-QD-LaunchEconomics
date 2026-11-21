# Báo cáo cá nhân — Nguyễn Văn Đăng — 2A202603371

## 1. Thông tin thành viên

- Họ tên: Nguyễn Văn Đăng
- MSSV: 2A202603371
- Email: nguyenvandang2201@gmail.com
- Vai trò: người kiểm số; người gắn nhãn 2 kiêm giữ hồ sơ; tiếp quản code CP4–CP5.

## 2. Phần việc phụ trách

- Kiểm tra các kết quả chi phí và độ nhạy A–B, hoàn thiện `bang_chi_phi.md`.
- Tính cỡ mẫu D1, lập `pilot_plan.yaml`, kiểm tra cách chia nhóm và luật dừng.
- Tổng hợp bảy mục trong `ho_so_launch_v0.md` và đối chiếu đề xuất Gate 2a với số liệu.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 và tham gia duyệt chéo; hai phần này chưa có bằng chứng hoàn thành trong repo.

## 3. Đóng góp cụ thể

- Bổ sung vào `src/lab13.py` các hàm tính cỡ mẫu hai tỉ lệ, hệ số thiết kế và cỡ mẫu hiệu dụng; in đủ năm kết quả D1. Với mục tiêu tăng 5 điểm, phép tính cần 1.251 yêu cầu hiệu dụng mỗi nhóm. Chia theo nhân viên với 75 yêu cầu/người cần 42 nhân viên mỗi nhóm, vượt 40 nhân viên của công ty.
- Hoàn thiện bảng A1–B4 trong `bang_chi_phi.md`, ghi rõ nhãn `simulated` cho chi phí dùng phút giả lập. Kết quả A2 là 4.472 đ/việc thành công; giới hạn hai lần chạy cho tổng chi phí hệ thống thấp nhất, 6.901.220 đ (simulated).
- Điền `pilot_plan.yaml`: phân ngẫu nhiên 20 nhân viên can thiệp và 20 nhân viên đối chứng, phân tầng theo depot; cần 299 yêu cầu/người để đạt khoảng 859 yêu cầu hiệu dụng mỗi nhóm khi MDE là 6 điểm. Kế hoạch ghi rõ đánh đổi: nếu tác động thật chỉ 5 điểm thì power khoảng 0,64, cùng ba luật dừng về an toàn, chi phí và mức dùng.
- Cập nhật `ho_so_launch_v0.md` với bảy mục có số, trạng thái và vai trò phụ trách. Đề xuất No-go tại Gate 2a vì chưa có hai bộ nhãn lỗi độc lập và chưa kiểm chứng cơ chế chống hoàn trùng; không coi số liệu thử nghiệm không có đối chứng là tác động của trợ lý.

## 4. Bằng chứng

- Commit `cda67dc` do Nguyễn Văn Đăng đứng tên ghi nhận thay đổi ở `src/lab13.py`, `bang_chi_phi.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md` và bản trước của báo cáo này. Các file là bằng chứng của phần việc đã ghi ở mục 3.
- Chạy `cd src` rồi `python -X utf8 lab13.py`: ba phép thử A1 in **ĐẠT** (1,20; 1,25; 1,25); A2 in 4.471,97 đ/việc (làm tròn 4.472 đ, simulated); D1 in 1.251, 3.103, trần 1.000, trần 300 và 299 yêu cầu/người.
- Kiểm tra riêng khoản xem lại: 890 phút × 2.000 đ/phút = **1.780.000 đ (simulated)**, khớp A2. Kiểm tra cỡ mẫu cụm: `20 × 299 ÷ [1 + (299 − 1) × 0,02] = 859,20`, đạt mức cần 859 hiệu dụng/nhóm cho MDE 6 điểm.
- `yaml.safe_load` đọc được `pilot_plan.yaml`; file có ba luật dừng và không còn giá trị `?` cần điền.

## 5. Công cụ AI đã dùng

Tôi dùng Codex để hỗ trợ đọc yêu cầu, viết công thức và mã, lập bản nháp các bảng và rà tính nhất quán của hồ sơ. Tôi kiểm tra lại bằng cách chạy `lab13.py` trên hai CSV gốc, đối chiếu ba phép thử A1 và các mốc số trong hướng dẫn, tính lại khoản xem lại và cỡ mẫu cụm như mục 4, rồi kiểm tra YAML bằng `yaml.safe_load`. Tôi không dùng AI để tạo bộ nhãn lỗi độc lập hoặc điểm duyệt chéo.

## 6. Tự đánh giá

Phần kiểm số A–B, code D1, kế hoạch pilot và hồ sơ Gate 2a có file và kết quả tái lập được. Tôi ghi rõ giới hạn của mô hình: phút xem lại/làm lại là simulated; mẫu thử không có nhóm đối chứng; pilot chỉ đủ power 0,80 cho MDE 6 điểm, không phải 5 điểm. CP3 và phiếu duyệt chéo còn thiếu bằng chứng thực tế, nên tôi chưa nhận là phần việc đã hoàn thành và chưa khẳng định bài nhóm đạt điểm tối đa.
