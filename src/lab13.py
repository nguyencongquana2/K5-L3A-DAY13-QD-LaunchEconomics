"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1 / p
    if not isinstance(k, int) or k < 1:
        raise ValueError('k phải là số nguyên dương hoặc None')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1.0
    if not isinstance(k, int) or k < 1:
        raise ValueError('k phải là số nguyên dương hoặc None')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        if not isinstance(max_lan_chay, int) or max_lan_chay < 1:
            raise ValueError('max_lan_chay phải là số nguyên dương hoặc None')
        runs = runs[runs['attempt'] <= max_lan_chay].copy()
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[
            vuot_gioi_han,
            ['phut_xem_lai_simulated', 'phut_lam_lai_simulated'],
        ] = 0

    tien_token_tung_lan = (
        runs['tokens_in'] / 1000 * gia_vao
        + runs['tokens_out'] / 1000 * gia_ra
    )
    tien_tool_tung_lan = runs['tool_calls'] * gia_tool
    tien_tung_lan = tien_token_tung_lan + tien_tool_tung_lan

    token = tien_token_tung_lan.sum()
    tool = tien_tool_tung_lan.sum()
    chay_lai = tien_tung_lan[runs['attempt'] > 1].sum()
    xem_lai = (
        reqs['phut_xem_lai_simulated'].sum()
        * luong_phut
        * he_so_xem_lai
    )
    lam_lai = (
        reqs['phut_lam_lai_simulated'].sum()
        * luong_phut
        * he_so_lam_lai
    )
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    if thanh_cong == 0:
        raise ValueError('Không có yêu cầu thành công để tính chi phí')

    return {
        'token': token,
        'tool': tool,
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': (token + tool) / len(reqs),
    }


def in_ket_qua(ket_qua):
    """In một kết quả mô hình theo định dạng dễ đối chiếu."""
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:18s} {gia_tri:>14,.2f}')


def tinh_b4_xem_lai_100_phan_tram(runs, reqs):
    """Tính kịch bản xem lại 100% cho noi_dia và hang_nang."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_pham_vi = runs[runs['request_id'].isin(pham_vi['request_id'])].copy()
    co_lan_chay_ok = runs_pham_vi.loc[
        runs_pham_vi['status'] == 'ok', 'request_id'
    ].nunique()
    so_ca_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pham_vi['ket_qua'] == 'thanh_cong').sum())

    tien_token = (
        runs_pham_vi['tokens_in'] / 1000 * GIA_VAO
        + runs_pham_vi['tokens_out'] / 1000 * GIA_RA
    ).sum()
    tien_tool = (runs_pham_vi['tool_calls'] * GIA_TOOL).sum()
    xem_lai = co_lan_chay_ok * 5 * LUONG_PHUT
    lam_lai_9_phut = so_ca_lam_lai * 9 * LUONG_PHUT
    phut_lam_lai_tb = reqs.loc[
        reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'
    ].mean()
    lam_lai_theo_du_lieu = so_ca_lam_lai * phut_lam_lai_tb * LUONG_PHUT

    tong_9_phut = tien_token + tien_tool + xem_lai + lam_lai_9_phut
    tong_theo_du_lieu = tien_token + tien_tool + xem_lai + lam_lai_theo_du_lieu
    return {
        'so_yeu_cau': len(pham_vi),
        'so_yeu_cau_co_lan_ok': co_lan_chay_ok,
        'so_ca_lam_lai': so_ca_lam_lai,
        'thanh_cong': thanh_cong,
        'token_tool': tien_token + tien_tool,
        'xem_lai': xem_lai,
        'lam_lai_9_phut': lam_lai_9_phut,
        'phut_lam_lai_tb': phut_lam_lai_tb,
        'cps_9_phut': tong_9_phut / thanh_cong,
        'cps_theo_du_lieu': tong_theo_du_lieu / thanh_cong,
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    print('\n=== A1 · Ba phép thử ===')
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    in_ket_qua(ket_qua)

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print('loai          so_yc  thanh_cong  lan_chay/yc       cps  so_voi_12000')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        reqs_loai = reqs[reqs['loai'] == loai]
        kq_loai = mo_hinh(runs, reqs_loai)
        ti_le = kq_loai['thanh_cong'] / len(reqs_loai)
        lan_chay = runs['request_id'].isin(reqs_loai['request_id']).sum() / len(reqs_loai)
        print(
            f'{loai:12s} {len(reqs_loai):6d} {ti_le:11.2%} '
            f'{lan_chay:12.2f} {kq_loai["cps"]:9,.0f} '
            f'{kq_loai["cps"] / BASELINE:12.2f}x'
        )

    print('\n=== A4 · Chi phí cố định cho noi_dia + hang_nang ===')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    for ti_le_khoi_luong in [1.0, 0.5]:
        viec_thanh_cong_thang = (
            45_000 * ti_le_khoi_luong * kq_pham_vi['thanh_cong'] / len(reqs)
        )
        co_dinh_moi_viec = 40_000_000 / viec_thanh_cong_thang
        cps_co_dinh = kq_pham_vi['cps'] + co_dinh_moi_viec
        print(
            f'{45_000 * ti_le_khoi_luong:,.0f} yc/thang: '
            f'{viec_thanh_cong_thang:,.0f} viec thanh cong; '
            f'co dinh/viec={co_dinh_moi_viec:,.0f}; '
            f'cps+co_dinh={cps_co_dinh:,.0f} ({cps_co_dinh / BASELINE:.2f}x)'
        )

    print('\n=== B1 · Độ nhạy từng yếu tố ===')
    kich_ban = {
        'Gia token gap doi': dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2),
        'Xem lai giam mot nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2),
        'Lam lai giam mot nua': dict(he_so_lam_lai=0.5),
        'Luong tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay': dict(max_lan_chay=2),
        'Chi 1 lan chay': dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:25s} {cps:10,.0f} {(cps / goc - 1) * 100:+7.1f}%')

    print('\n=== B2 · Kịch bản kết hợp ===')
    ket_hop = mo_hinh(
        runs,
        reqs,
        gia_vao=52,
        gia_ra=260,
        he_so_xem_lai=2,
    )['cps']
    print(
        f'Token gap doi + xem lai gap doi: {ket_hop:,.0f} '
        f'({(ket_hop / goc - 1) * 100:+.1f}%)'
    )

    print('\n=== B3 · Giới hạn chạy lại ===')
    print('gioi_han   tong_tro_ly  khong_thanh_cong  tong_he_thong       cps')
    for gioi_han in [1, 2, 3]:
        kq_gioi_han = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq_gioi_han['thanh_cong']
        tong_he_thong = kq_gioi_han['tong'] + khong_thanh_cong * BASELINE
        print(
            f'{gioi_han:9d} {kq_gioi_han["tong"]:13,.0f} '
            f'{khong_thanh_cong:17d} {tong_he_thong:14,.0f} '
            f'{kq_gioi_han["cps"]:9,.0f}'
        )

    print('\n=== B4 · Xem lại 100% trong phạm vi pilot ===')
    b4 = tinh_b4_xem_lai_100_phan_tram(runs, reqs)
    for ten, gia_tri in b4.items():
        print(f'{ten:24s} {gia_tri:>14,.2f}')

    print('\n=== E1 · Chỉ số tính thử ===')
    chi_so_chinh = (
        (reqs['dong_trong_24h'] == 1)
        & (reqs['mo_lai_trong_7_ngay'] == 0)
    ).mean()
    duoc_xem_lai = reqs[reqs['duoc_xem_lai'] == 1]
    ti_le_bo_qua = duoc_xem_lai['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    ti_le_mo_lai = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    print(f'chi_so_chinh: {chi_so_chinh:.2%}')
    print(f'ti_le_bo_qua: {ti_le_bo_qua:.2%}')
    print(f'ti_le_mo_lai: {ti_le_mo_lai:.2%}')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
