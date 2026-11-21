# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: QD
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dùng dữ liệu trace của 1.624 lần chạy và 1.200 yêu cầu để tính chi phí mỗi việc thành công, kiểm tra độ nhạy và đặc tả chỉ số cho pilot. Mọi khoản thời gian lấy từ cột `_simulated` đều được ghi nhãn simulated; tử số chi phí tính mọi lần chạy còn mẫu số chỉ tính yêu cầu thành công.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- Nhiệm vụ A–B: `src/lab13.py` tính chi phí từ trace, tách theo loại yêu cầu, chi phí cố định và các kịch bản độ nhạy; `bang_chi_phi.md` đã ghi kết quả chạy lại.
- Nhiệm vụ C: hai người gắn nhãn phải hoàn thành độc lập trong `bang_loi.md`; phần này chưa có bằng chứng nên chưa báo cáo kết quả.
- Nhiệm vụ D: `src/lab13.py` in đủ năm câu D1; `pilot_plan.yaml` ghi kế hoạch chia theo nhân viên và đánh đổi MDE 6 điểm.
- Nhiệm vụ E: `chi_so.md` đặc tả năm chỉ số, mười event có `trace_id` và ba rủi ro kinh tế; `ho_so_launch_v0.md` tổng hợp bằng chứng hiện có và đề xuất No-go tại Gate 2a.

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo sẽ được cập nhật khi có phiếu chấm thực tế.

- Ba phép thử A1 đạt 1,20; 1,25; 1,25. Chi phí mỗi việc thành công là 4.472 đ (simulated), trong đó làm lại chiếm 51,8% và xem lại chiếm 40,7%.
- Trong phạm vi đề xuất xem xét, `noi_dia` có chi phí 2.696 đ/việc và `hang_nang` 8.221 đ/việc (simulated); `quoc_te` lên tới 22.515 đ = 1,88× nhân viên tự làm.
- Giới hạn hai lần chạy cho tổng chi phí hệ thống thấp nhất: 6.901.220 đ (simulated). Xem lại 100% làm chi phí tăng tới 11.743–12.414 đ/việc (simulated).
- Chỉ số trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại trong 7 ngày 4,25%; chưa thể suy ra tác động khi chưa có nhóm đối chứng.
- Kế hoạch pilot chọn 20 nhân viên/nhóm, cần ít nhất 299 yêu cầu/người để đủ 859 hiệu dụng/nhóm cho MDE 6 điểm; nếu tác động thật 5 điểm, power chỉ khoảng 0,64. Đề xuất No-go vì chưa có hai bộ nhãn lỗi độc lập và kiểm chứng cơ chế chống hoàn trùng; chưa có bằng chứng duyệt chéo để điền phiếu.

## 5. Khó khăn và cách xử lý

Môi trường ban đầu chưa có thư viện phân tích; nhóm tạo `.venv` trong `src/`, cài `requirements.txt` và xác nhận import thành công. Nhóm giữ nguyên hai file CSV, đọc `logix_requests.csv` với `keep_default_na=False` và dùng ba phép thử A1 để phát hiện sai công thức trước khi tính tiếp.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Hiện chưa có hai bộ nhãn lỗi độc lập và kết quả duyệt chéo. Kế hoạch pilot mới là đề xuất, chưa được Giám đốc vận hành phê duyệt; dữ liệu thời gian xem lại/làm lại là simulated và cần thay bằng phút đo thật. Mốc 2026-11-30 chỉ khả thi nếu các điều kiện quay lại Gate 2a được hoàn thành trước đó.

## 8. Tài liệu tham khảo

- `docs/du_lieu_va_cong_thuc.md`.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*.
- Google PAIR, *People + AI Guidebook — Errors + Graceful Failure*.
