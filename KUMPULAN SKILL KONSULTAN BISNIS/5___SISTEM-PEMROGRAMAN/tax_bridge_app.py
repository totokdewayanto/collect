import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="TaxBridge Enterprise - PT Serba Ada Sejahtera",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ TaxBridge Enterprise: System Integration & Tax Compliance App")
st.caption("Aplikasi System Integration & Tax Audit Calculator — Kasus PT Serba Ada Sejahtera (Supermarket & Pharmacy Addition)")

# Sidebar Navigation
st.sidebar.header("📌 Navigasi Modul System")
module = st.sidebar.radio(
    "Pilih Modul Integrasi:",
    [
        "1. Executive Dashboard SP2DK",
        "2. POS Middleware: PPN & Tax Flag (BKP/OTC)",
        "3. Payroll Medis: PPh 21 Dokter Separator",
        "4. Accounts Payable: e-Bupot PPh 23 & 4(2)",
        "5. Financial ERP: Amortisasi & Rekonsiliasi PPh Badan"
    ]
)

# ---------------------------------------------------------
# MODUL 1: EXECUTIVE DASHBOARD
# ---------------------------------------------------------
if module == "1. Executive Dashboard SP2DK":
    st.header("📊 Executive Summary & Status Audit SP2DK 2025")
    st.info("Status Kasus: Response Filed & Reconciliation Approved (KPP Madya Jakarta — No. S-892/WPJ.07/KP.04/2026)")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Omzet Bruto 2025", "Rp 57.000.000.000")
    col2.metric("Kurang Bayar Pokok Pajak", "Rp 3.181.896.396")
    col3.metric("Sanksi Bunga KUP", "Rp 122.065.495")
    col4.metric("Total Tagihan SP2DK", "Rp 3.303.961.892", delta="-Rp 3.30B", delta_color="inverse")
    
    st.subheader("📋 Rekapitulasi Tagihan Pajak per Jenis Pajak")
    rekap_data = {
        "Jenis Pajak": [
            "PPN Penyerahan Apotek & Supermarket",
            "PPh Pasal 21 Dokter & Apoteker",
            "PPh Pasal 23 KSO Alat Cek Medis",
            "PPh Pasal 4(2) Sewa Booth Apotek",
            "PPh Badan (Tahunan 2025)"
        ],
        "Pokok SPT (Rp)": [5252252252, 48000000, 3000000, 15000000, -1925000000],
        "Pokok Audit (Rp)": [5648648649, 103500000, 8000000, 45000000, 770000000],
        "Kurang Bayar Pokok (Rp)": [396396396, 55500000, 5000000, 30000000, 2695000000],
        "Sanksi Bunga KUP (Rp)": [55495495, 7770000, 700000, 4200000, 53900000],
        "Total Tagihan (Rp)": [451891892, 63270000, 570000, 34200000, 2748900000]
    }
    df_rekap = pd.DataFrame(rekap_data)
    st.dataframe(df_rekap.style.format({
        "Pokok SPT (Rp)": "Rp {:,.0f}",
        "Pokok Audit (Rp)": "Rp {:,.0f}",
        "Kurang Bayar Pokok (Rp)": "Rp {:,.0f}",
        "Sanksi Bunga KUP (Rp)": "Rp {:,.0f}",
        "Total Tagihan (Rp)": "Rp {:,.0f}"
    }), use_container_width=True)

# ---------------------------------------------------------
# MODUL 2: POS MIDDLEWARE - PPN & TAX FLAG
# ---------------------------------------------------------
elif module == "2. POS Middleware: PPN & Tax Flag (BKP/OTC)":
    st.header("🛒 POS Middleware: PPN Auto Gross-Up & Tax Flag Validator")
    st.write("Modul ini mensimulasikan pencatatan POS kasir dengan auto-flagging BKP/Non-BKP serta rumus DPP Gross-Up (100/111).")
    
    st.subheader("🧮 Calculator POS Tax Flag")
    col_a, col_b, col_c = st.columns(3)
    omzet_super = col_a.number_input("Omzet Supermarket (Inklusif PPN)", value=45000000000, step=1000000000)
    omzet_otc = col_b.number_input("Omzet Apotek OTC (Inklusif PPN)", value=8000000000, step=1000000000)
    omzet_resep = col_c.number_input("Omzet Apotek Obat Resep Dokter", value=4000000000, step=1000000000)
    
    # Calculation
    dpp_super = (100 / 111) * omzet_super
    dpp_otc = (100 / 111) * omzet_otc
    dpp_resep = (100 / 111) * omzet_resep
    total_dpp = dpp_super + dpp_otc + dpp_resep
    
    ppn_super = dpp_super * 0.11
    ppn_otc = dpp_otc * 0.11
    ppn_resep = dpp_resep * 0.11
    total_ppn = total_dpp * 0.11
    
    st.markdown("---")
    st.subheader("📈 Hasil Auto-Calculation DPP & PPN 11%")
    res_df = pd.DataFrame({
        "Kategori Penyerahan": ["Supermarket Ritel (BKP)", "Apotek OTC (Obat Bebas BKP)", "Apotek Resep Dokter (BKP Ritel)"],
        "Nilai Bruto (Rp)": [omzet_super, omzet_otc, omzet_resep],
        "DPP Gross-Up (100/111) (Rp)": [dpp_super, dpp_otc, dpp_resep],
        "PPN Keluaran (11%) (Rp)": [ppn_super, ppn_otc, ppn_resep]
    })
    st.table(res_df.style.format({
        "Nilai Bruto (Rp)": "Rp {:,.2f}",
        "DPP Gross-Up (100/111) (Rp)": "Rp {:,.2f}",
        "PPN Keluaran (11%) (Rp)": "Rp {:,.2f}"
    }))
    
    st.success(f"**Total PPN Terutang (Hasil Audit):** Rp {total_ppn:,.2f}")

# ---------------------------------------------------------
# MODUL 3: PAYROLL MEDIS - PPH 21 DOKTER SEPARATOR
# ---------------------------------------------------------
elif module == "3. Payroll Medis: PPh 21 Dokter Separator":
    st.header("👨‍⚕️ Payroll Medis: Pemisah Jasa Sarana vs Jasa Medis Dokter")
    st.write("Sesuai PER-16/PJ/2016 & PMK 168/2023, DPP PPh 21 Dokter Bukan Pegawai = 50% x Jasa Medis Murni Hak Dokter.")
    
    jasa_bruto = st.number_input("Total Pembayaran Jasa Medis & Honorarium (Rp)", value=1500000000, step=100000000)
    pct_sarana = st.slider("Persentase Jasa Sarana Supermarket (%)", min_value=0, max_value=80, value=50)
    
    jasa_sarana = jasa_bruto * (pct_sarana / 100.0)
    jasa_murni = jasa_bruto * ((100 - pct_sarana) / 100.0)
    dpp_pph21 = 0.50 * jasa_murni
    
    st.subheader("🔍 Breakdown Hasil Pemisahan")
    c1, c2, c3 = st.columns(3)
    c1.metric("Jasa Sarana Supermarket (Pendapatan PT)", f"Rp {jasa_sarana:,.0f}")
    c2.metric("Jasa Medis Murni Dokter", f"Rp {jasa_murni:,.0f}")
    c3.metric("DPP PPh 21 Bukan Pegawai (50%)", f"Rp {dpp_pph21:,.0f}")

# ---------------------------------------------------------
# MODUL 4: ACCOUNTS PAYABLE - E-BUPOT PPH 23 & 4(2)
# ---------------------------------------------------------
elif module == "4. Accounts Payable: e-Bupot PPh 23 & 4(2)":
    st.header("💳 Accounts Payable: Validator e-Bupot Unifikasi")
    
    st.subheader("1. Pemotongan PPh Pasal 23 (KSO & Jasa Maintenance)")
    kso_bruto = st.number_input("Nilai Bagi Hasil KSO Alat Cek Medis (Rp)", value=250000000)
    pph23_terutang = kso_bruto * 0.02
    st.info(f"PPh Pasal 23 Terutang (2%): **Rp {pph23_terutang:,.0f}**")
    
    st.subheader("2. Pemotongan PPh Pasal 4(2) Final (Sewa Booth/Ruangan)")
    sewa_bruto = st.number_input("Nilai Sewa Space Booth Apotek (Rp)", value=300000000)
    pph42_terutang = sewa_bruto * 0.10
    st.info(f"PPh Pasal 4(2) Final Terutang (10%): **Rp {pph42_terutang:,.0f}**")

# ---------------------------------------------------------
# MODUL 5: AMORTISASI & PPH BADAN
# ---------------------------------------------------------
elif module == "5. Financial ERP: Amortisasi & Rekonsiliasi PPh Badan":
    st.header("🏢 Financial ERP: Kapitalisasi Investasi & Rekonsiliasi Fiskal")
    
    investasi = st.number_input("Nilai Investasi Awal Apotek (Rp)", value=18000000000, step=1000000000)
    masa_amortisasi = st.selectbox("Masa Amortisasi Harta Tak Berwujud (Kelompok 1)", [4, 8, 16, 20], index=0)
    
    amortisasi_tahunan = investasi / masa_amortisasi
    st.success(f"**Beban Amortisasi Fiskal per Tahun:** Rp {amortisasi_tahunan:,.0f}")
    
    st.subheader("📊 Tabel Amortisasi 4 Tahun")
    df_amort = pd.DataFrame({
        "Tahun": [f"Tahun {i}" for i in range(1, masa_amortisasi + 1)],
        "Nilai Sisa Awal (Rp)": [investasi - (i * amortisasi_tahunan) for i in range(masa_amortisasi)],
        "Beban Amortisasi (Rp)": [amortisasi_tahunan] * masa_amortisasi,
        "Nilai Buku Akhir (Rp)": [investasi - ((i + 1) * amortisasi_tahunan) for i in range(masa_amortisasi)]
    })
    st.table(df_amort.style.format({
        "Nilai Sisa Awal (Rp)": "Rp {:,.0f}",
        "Beban Amortisasi (Rp)": "Rp {:,.0f}",
        "Nilai Buku Akhir (Rp)": "Rp {:,.0f}"
    }))
