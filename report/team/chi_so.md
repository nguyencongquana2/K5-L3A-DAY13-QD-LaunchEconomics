# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ mở trợ lý trong nhóm can thiệp | Số yêu cầu có `agent_suggestion_shown`, chia số yêu cầu thuộc nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ hoàn sai tiền qua kiểm tra mẫu | Số mẫu có số tiền đã hoàn khác số tiền đúng, chia tổng số mẫu được kiểm tra trong tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên CSKH | `quyet_dinh`, `phut_xem_lai`, `trace_id` | Khi nhân viên giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi giao dịch hoàn phí |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi agent chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng ticket |
| `ticket_reopened` | Hệ thống ticket | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại ticket |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: nối `refund_request_created`, `ticket_closed` và `ticket_reopened` bằng `trace_id`.
- Tỉ lệ bỏ qua gợi ý: dùng `agent_suggestion_shown` và `staff_review_decision`.
- Tỉ lệ lỗi lọt đến khách: dùng `refund_request_created` và `ticket_reopened`.
- Tỉ lệ mở trợ lý: dùng `refund_request_created` với `arm` và `agent_suggestion_shown`.
- Tỉ lệ hoàn sai tiền: dùng `audit_sample_checked`.

Chỉ số trong đợt chạy thử là 82,83%; dữ liệu này chưa có nhóm đối chứng nên chưa thể kết luận tác động của trợ lý.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng 51,8%, từ 4.472 đ lên 6.787 đ (simulated) | Tỉ lệ `staff_rework_completed` theo tuần vượt 7% | Thu hẹp về `noi_dia` và rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× chi phí nhân viên; lên 12.414 đ = 1,03× nếu làm lại mất trung bình 15,3 phút (simulated) | Tỉ lệ có `staff_review_decision` còn trên 50% cuối bước rollout 0,25 | Chỉ giảm xem lại theo bậc khi tỉ lệ sửa + bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định tăng từ 1.185 lên 2.370 đ/việc khi khối lượng giảm một nửa (simulated) | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot và rà lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
