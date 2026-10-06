import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="TaxBridge Enterprise - PT Serba Ada Sejahtera",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# SKILL-NGODING DESIGN SYSTEM (CSS CUSTOM PROPERTIES & COMPONENTS)
# ---------------------------------------------------------
custom_css = """
<style>
    /* CSS Custom Properties & Design Tokens from SKILL-Ngoding */
    :root {
        --primary: #4f46e5;
        --primary-hover: #4338ca;
        --bg-color: #f8fafc;
        --surface-color: #ffffff;
        --text-main: #0f172a;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --accent-emerald: #10b981;
        --accent-rose: #f43f5e;
        --radius: 0.75rem;
        --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    /* Global Body & Background Styling */
    .main {
        background-color: var(--bg-color);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hero Section Banner (SKILL-Ngoding Layout Pattern) */
    .hero-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
        color: #ffffff;
        padding: 2.5rem 2rem;
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        margin-bottom: 2rem;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #c7d2fe;
        max-width: 800px;
        line-height: 1.6;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.25);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    /* KPI Feature Cards (SKILL-Ngoding Responsive Grid) */
    .kpi-card {
        background: var(--surface-color);
        border: 1px solid var(--border-color);
        border-radius: var(--radius);
        padding: 1.5rem;
        box-shadow: var(--shadow);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .kpi-label {
        font-size: 0.875rem;
        font-weight: 600;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        font-size: 1.75rem;
        font-weight: 800;
        color: var(--text-main);
        margin-top: 0.5rem;
    }
    .kpi-subtext {
        font-size: 0.8rem;
        margin-top: 0.25rem;
    }
    .kpi-danger { color: var(--accent-rose); }
    .kpi-success { color: var(--accent-emerald); }

    /* Tables & Section Headers */
    .section-header {
        border-left: 4px solid var(--primary);
        padding-left: 0.75rem;
        margin: 1.5rem 0 1rem 0;
        font-weight: 700;
        color: var(--text-main);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/isometric/100/hospital.png", width=64)
st.sidebar.title("TaxBridge Enterprise")
st.sidebar.caption("Frontend System Architecture (SKILL-Ngoding Integrated)")

st.sidebar.markdown(
    "<a href=\"https://notebook.google.com/notebook/35f527f3-7a65-4267-8ee5-2cd230356406\" "
    "target=\"_blank\" rel=\"noopener noreferrer\">"
    "📓 Buka NotebookLM Saya</a>",
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")

module = st.sidebar.radio(
    "📌 Navigasi Modul Integrasi:",
    [
        "1. Executive Dashboard SP2DK",
        "2. POS Middleware: PPN & Tax Flag (BKP/OTC)",
        "3. Payroll Medis: PPh 21 Dokter Separator",
        "4. Accounts Payable: e-Bupot PPh 23 & 4(2)",
        "5. Financial ERP: Amortisasi & PPh Badan",
        "6. Auto-Generate XML DJP Coretax"
    ]
)

# ---------------------------------------------------------
# MODUL 1: EXECUTIVE DASHBOARD (WITH HERO SECTION & KPI CARDS)
# ---------------------------------------------------------
if module == "1. Executive Dashboard SP2DK":
    st.markdown("""
    <div class="hero-banner">
        <span class="hero-badge">PERFEKTIF SISTEM TAX COMPLIANCE & RECONCILIATION</span>
        <div class="hero-title">⚖️ Executive Dashboard Audit SP2DK 2025</div>
        <div class="hero-subtitle">
            Integrasi Arsitektur Frontend SKILL-Ngoding dengan Engine Kalkulasi Fiskal PT Serba Ada Sejahtera. 
            Merespons Surat SP2DK No. S-892/WPJ.07/KP.04/2026 KPP Madya Jakarta.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Total Omzet 2025</div>
            <div class="kpi-value">Rp 57.0 B</div>
            <div class="kpi-subtext kpi-success">✓ Supermarket + Apotek</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Kurang Bayar Pokok</div>
            <div class="kpi-value">Rp 3.18 B</div>
            <div class="kpi-subtext kpi-danger">Rekonsiliasi Fiskal Audit</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Sanksi Bunga KUP</div>
            <div class="kpi-value">Rp 122.0 M</div>
            <div class="kpi-subtext kpi-danger">Pasal 9 (2a) UU KUP</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="kpi-card">
            <div class="kpi-label">Total Tagihan SP2DK</div>
            <div class="kpi-value kpi-danger">Rp 3.30 B</div>
            <div class="kpi-subtext">Pokok + Sanksi Terutang</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-header'>📋 Rekapitulasi Pokok & Sanksi Bunga Hasil Audit</h3>", unsafe_allow_html=True)
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
        "Total Tagihan (Rp)": [451891892, 63270000, 5700000, 34200000, 2748900000]
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
    st.markdown("<h2 class='section-header'>🛒 POS Middleware: Auto-Calculate PPN & Tax Flagging</h2>", unsafe_allow_html=True)
    st.write("Engine ini menerapkan validasi BKP/Non-BKP serta perhitungan mundur DPP Gross-Up (100/111).")
    
    col_a, col_b, col_c = st.columns(3)
    omzet_super = col_a.number_input("Omzet Supermarket (Inklusif PPN)", value=45000000000, step=1000000000)
    omzet_otc = col_b.number_input("Omzet Apotek OTC (Inklusif PPN)", value=8000000000, step=1000000000)
    omzet_resep = col_c.number_input("Omzet Apotek Obat Resep Dokter", value=4000000000, step=1000000000)
    
    dpp_super = (100 / 111) * omzet_super
    dpp_otc = (100 / 111) * omzet_otc
    dpp_resep = (100 / 111) * omzet_resep
    total_dpp = dpp_super + dpp_otc + dpp_resep
    
    ppn_super = dpp_super * 0.11
    ppn_otc = dpp_otc * 0.11
    ppn_resep = dpp_resep * 0.11
    total_ppn = total_dpp * 0.11
    
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
    st.success(f"**Total PPN Keluaran Audit:** Rp {total_ppn:,.2f}")

# ---------------------------------------------------------
# MODUL 3: PAYROLL MEDIS - PPH 21 DOKTER SEPARATOR
# ---------------------------------------------------------
elif module == "3. Payroll Medis: PPh 21 Dokter Separator":
    st.markdown("<h2 class='section-header'>👨‍⚕️ Payroll Medis: Pemisah Jasa Sarana vs Jasa Medis Murni</h2>", unsafe_allow_html=True)
    st.write("Sesuai PER-16/PJ/2016 & PMK 168/2023, DPP PPh 21 Dokter Bukan Pegawai = 50% x Jasa Medis Murni Hak Dokter.")
    
    jasa_bruto = st.number_input("Total Pembayaran Jasa Medis & Honorarium (Rp)", value=1500000000, step=100000000)
    pct_sarana = st.slider("Persentase Jasa Sarana Supermarket (%)", min_value=0, max_value=80, value=50)
    
    jasa_sarana = jasa_bruto * (pct_sarana / 100.0)
    jasa_murni = jasa_bruto * ((100 - pct_sarana) / 100.0)
    dpp_pph21 = 0.50 * jasa_murni
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Jasa Sarana Supermarket (Omzet PT)", f"Rp {jasa_sarana:,.0f}")
    c2.metric("Jasa Medis Murni Dokter", f"Rp {jasa_murni:,.0f}")
    c3.metric("DPP PPh 21 Bukan Pegawai (50%)", f"Rp {dpp_pph21:,.0f}")

# ---------------------------------------------------------
# MODUL 4: ACCOUNTS PAYABLE - E-BUPOT PPH 23 & 4(2)
# ---------------------------------------------------------
elif module == "4. Accounts Payable: e-Bupot PPh 23 & 4(2)":
    st.markdown("<h2 class='section-header'>💳 Accounts Payable: Validator e-Bupot Unifikasi</h2>", unsafe_allow_html=True)
    
    kso_bruto = st.number_input("Nilai Bagi Hasil KSO Alat Cek Medis (Rp)", value=250000000)
    pph23_terutang = kso_bruto * 0.02
    st.info(f"PPh Pasal 23 Terutang (2%): **Rp {pph23_terutang:,.0f}**")
    
    sewa_bruto = st.number_input("Nilai Sewa Space Booth Apotek (Rp)", value=300000000)
    pph42_terutang = sewa_bruto * 0.10
    st.info(f"PPh Pasal 4(2) Final Terutang (10%): **Rp {pph42_terutang:,.0f}**")

# ---------------------------------------------------------
# MODUL 5: AMORTISASI & PPH BADAN
# ---------------------------------------------------------
elif module == "5. Financial ERP: Amortisasi & Rekonsiliasi PPh Badan":
    st.markdown("<h2 class='section-header'>🏢 Financial ERP: Kapitalisasi Investasi & Rekonsiliasi Fiskal</h2>", unsafe_allow_html=True)
    
    investasi = st.number_input("Nilai Investasi Awal Apotek (Rp)", value=18000000000, step=1000000000)
    masa_amortisasi = st.selectbox("Masa Amortisasi Harta Tak Berwujud (Kelompok 1)", [4, 8, 16, 20], index=0)
    
    amortisasi_tahunan = investasi / masa_amortisasi
    st.success(f"**Beban Amortisasi Fiskal per Tahun:** Rp {amortisasi_tahunan:,.0f}")
    
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

# ---------------------------------------------------------
# MODUL 6: AUTO-GENERATE XML CORECTAX
# ---------------------------------------------------------
elif module == "6. Auto-Generate XML DJP Coretax":
    st.markdown("<h2 class='section-header'>📦 Generator XML Impor Massal DJP Coretax</h2>", unsafe_allow_html=True)
    st.write("Modul ini menghasilkan berkas XML e-Faktur 4.0 dan e-Bupot Unifikasi untuk diunggah langsung ke portal DJP Coretax.")
    
    tab1, tab2 = st.tabs(["📄 e-Faktur 4.0 (PPN Keluaran)", "📄 e-Bupot Unifikasi (PPh 21/23/4(2))"])
    
    with tab1:
        st.subheader("XML e-Faktur 4.0 Penyerahan BKP Apotek & Supermarket")
        xml_efaktur = """<?xml version="1.0" encoding="UTF-8"?>
<TAX_INVOICE_BATCH version="4.0" npwp_penjual="013456789012000" nama_penjual="PT SERBA ADA SEJAHTERA">
    <FAKTUR_PAJAK>
        <KODE_TRANSAKSI>01</KODE_TRANSAKSI>
        <NOMOR_FAKTUR>010.000-25.00000001</NOMOR_FAKTUR>
        <TANGGAL_FAKTUR>2025-12-31</TANGGAL_FAKTUR>
        <PENYERAHAN>
            <DESKRIPSI>Penjualan Ritel Supermarket (BKP Digabung)</DESKRIPSI>
            <DPP>40540540541</DPP>
            <PPN>4459459459</PPN>
        </PENYERAHAN>
    </FAKTUR_PAJAK>
    <FAKTUR_PAJAK>
        <KODE_TRANSAKSI>01</KODE_TRANSAKSI>
        <NOMOR_FAKTUR>010.000-25.00000002</NOMOR_FAKTUR>
        <TANGGAL_FAKTUR>2025-12-31</TANGGAL_FAKTUR>
        <PENYERAHAN>
            <DESKRIPSI>Penjualan Apotek OTC (Obat Bebas Gross-Up)</DESKRIPSI>
            <DPP>7207207207</DPP>
            <PPN>792792793</PPN>
        </PENYERAHAN>
    </FAKTUR_PAJAK>
    <FAKTUR_PAJAK>
        <KODE_TRANSAKSI>01</KODE_TRANSAKSI>
        <NOMOR_FAKTUR>010.000-25.00000003</NOMOR_FAKTUR>
        <TANGGAL_FAKTUR>2025-12-31</TANGGAL_FAKTUR>
        <PENYERAHAN>
            <DESKRIPSI>Penjualan Apotek Obat Resep Dokter BKP</DESKRIPSI>
            <DPP>3603603604</DPP>
            <PPN>396396396</PPN>
        </PENYERAHAN>
    </FAKTUR_PAJAK>
</TAX_INVOICE_BATCH>"""
        st.code(xml_efaktur, language="xml")
        st.download_button("📥 Download XML e-Faktur 4.0", data=xml_efaktur, file_name="eFaktur_40_PT_SAS_2025.xml", mime="application/xml")
        
    with tab2:
        st.subheader("XML e-Bupot Unifikasi (PPh 21, 23, & 4(2))")
        xml_ebupot = """<?xml version="1.0" encoding="UTF-8"?>
<BUPOT_UNIFIKASI npwp_pemotong="013456789012000" masa_pajak="12" tahun_pajak="2025">
    <BUKTI_POTONG_PPH21>
        <KODE_OBJEK_PAJAK>21-100-02</KODE_OBJEK_PAJAK>
        <NAMA_DOKTER>dr. Hermawan, Sp.A</NAMA_DOKTER>
        <BRUTO_JASA_MEDIS>1140000000</BRUTO_JASA_MEDIS>
        <DPP_50_PERSEN>570000000</DPP_50_PERSEN>
        <PPH_TERUTANG>85500000</PPH_TERUTANG>
    </BUKTI_POTONG_PPH21>
    <BUKTI_POTONG_PPH23>
        <KODE_OBJEK_PAJAK>24-104-01</KODE_OBJEK_PAJAK>
        <NAMA_VENDOR>PT Medika Alat Utama (KSO)</NAMA_VENDOR>
        <NILAI_BRUTO>250000000</NILAI_BRUTO>
        <TARIF>0.02</TARIF>
        <PPH_DIPOTONG>5000000</PPH_DIPOTONG>
    </BUKTI_POTONG_PPH23>
    <BUKTI_POTONG_PPH42>
        <KODE_OBJEK_PAJAK>28-403-01</KODE_OBJEK_PAJAK>
        <NAMA_VENDOR>PT Serba Ada Sejahtera (Sewa Booth)</NAMA_VENDOR>
        <NILAI_SEWA_BRUTO>300000000</NILAI_SEWA_BRUTO>
        <TARIF_FINAL>0.10</TARIF_FINAL>
        <PPH_FINAL>30000000</PPH_FINAL>
    </BUKTI_POTONG_PPH42>
</BUPOT_UNIFIKASI>"""
        st.code(xml_ebupot, language="xml")
        st.download_button("📥 Download XML e-Bupot Unifikasi", data=xml_ebupot, file_name="eBupot_Unifikasi_PT_SAS_2025.xml", mime="application/xml")
