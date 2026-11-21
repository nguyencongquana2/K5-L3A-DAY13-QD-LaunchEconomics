# Bảng chi phí · Nhiệm vụ A và B

Nguồn: chạy `python -X utf8 lab13.py` trong `src/` trên hai CSV của repo. Chi phí có phút nhân viên đều ghi `simulated`; giá và lương là giả định của lab. Số tiền làm tròn đến đồng, tỷ lệ làm tròn đến một hoặc hai chữ số thập phân.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt > 1; đã nằm trong Token + Tool | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | Token + Tool + Xem lại + Làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | dữ liệu giả lập |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công là 4.472 ÷ 274,65 = **16,3 lần** hoá đơn chia số yêu cầu (simulated).
- Làm lại chiếm **51,8%** tổng chi phí, lớn nhất; xem lại chiếm **40,7%** (đều simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 đ (simulated) | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 đ (simulated) | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 đ (simulated) | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 đ (simulated) | 0,85× |

- `quoc_te` không đáng xử lý trong pilot: 22.515 đ/việc, bằng 1,88× nhân viên tự làm (simulated). Dù chạy trung bình 2,32 lần, chỉ 27,33% thành công; chạy lại tới 3 lần không giải quyết được lỗi lặp lại.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Tỉ lệ việc thành công trong phạm vi là 900/1.200 yêu cầu của mẫu; chi phí biến đổi mỗi việc thành công là 3.414 đ (simulated). Chi phí cố định giả định: 40 triệu đ/tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Ở cả hai khối lượng đã tính, chi phí vẫn dưới 12.000 đ/việc (simulated); khoản cố định mỗi việc tăng gấp đôi khi khối lượng giảm một nửa. Chưa suy ra kết luận cho quy mô pilot nhỏ hơn nữa.

## B1 · Đổi từng yếu tố

Mốc gốc: **4.472 đ/việc (simulated)**. Mỗi dòng chỉ thay một yếu tố.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại × 0,5 | 3.315 đ (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ attempt > 2; yêu cầu vượt giới hạn chuyển nhân viên | 4.237 đ (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc (+46,3%)**, simulated.
- Ba yếu tố ảnh hưởng mạnh nhất: **1. làm lại (+51,8%) · 2. xem lại (+40,7%) · 3. lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Chi phí trợ lý và mỗi việc thành công gồm phút `_simulated`.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | **6.901.220 đ (simulated)** | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- **2 lần** rẻ nhất cho cả hệ thống: 6.901.220 đ (simulated). Không trùng với **1 lần**, phương án có chi phí mỗi việc thành công thấp nhất 4.111 đ nhưng chuyển thêm 85 yêu cầu sang nhân viên so với 2 lần.

## B4 · Nếu phải xem lại tất cả

- Trong 982 yêu cầu `noi_dia` + `hang_nang`, có 948 yêu cầu chạy ok và 900 thành công; xem lại 5 phút/ca, làm lại 9 phút/ca cho 48 ca cho **11.743 đ/việc = 0,98×** nhân viên tự làm (simulated). Nếu làm lại theo trung bình 15,3 phút từ dữ liệu, chi phí là **12.414 đ = 1,03×** (simulated).
- Pilot phải đo phút xem lại và làm lại thực tế, cùng mức giảm xem lại vẫn an toàn; ở 100% xem lại, lợi ích chi phí gần như biến mất.
