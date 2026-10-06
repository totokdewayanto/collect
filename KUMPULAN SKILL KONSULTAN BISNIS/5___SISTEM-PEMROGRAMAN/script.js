const API_BASE = window.location.origin;

const formatCurrency = (value) => new Intl.NumberFormat("id-ID", {
  style: "currency",
  currency: "IDR",
  maximumFractionDigits: 2,
}).format(Number(value));

const setStatus = (message, isError = false) => {
  const status = document.getElementById("form-status");
  status.textContent = message;
  status.classList.toggle("error", isError);
};

const loadDashboard = async () => {
  const status = document.getElementById("dashboard-status");
  try {
    const response = await fetch(`${API_BASE}/api/dashboard`);
    if (!response.ok) throw new Error("Data dashboard gagal dimuat.");
    const dashboard = await response.json();
    document.getElementById("kpi-revenue").textContent = formatCurrency(dashboard.kpis.total_omzet);
    document.getElementById("kpi-underpaid").textContent = formatCurrency(dashboard.kpis.kurang_bayar_pokok);
    document.getElementById("kpi-interest").textContent = formatCurrency(dashboard.kpis.sanksi_bunga);
    document.getElementById("kpi-bill").textContent = formatCurrency(dashboard.kpis.total_tagihan);

    const rows = document.getElementById("audit-rows");
    rows.replaceChildren(...dashboard.audit_breakdown.map((item) => {
      const row = document.createElement("tr");
      [item.jenis_pajak, item.pokok_spt, item.pokok_audit, item.kurang_bayar, item.sanksi, item.total_tagihan].forEach((value, index) => {
        const cell = document.createElement("td");
        cell.textContent = index === 0 ? value : formatCurrency(value);
        row.append(cell);
      });
      return row;
    }));
    status.textContent = "Dashboard diperbarui dari API.";
  } catch (error) {
    status.textContent = error.message || "Dashboard tidak dapat dimuat.";
    status.classList.add("error");
  }
};

const calculateAmortization = async (event) => {
  event.preventDefault();
  const status = document.getElementById("amortization-status");
  status.textContent = "Menghitung jadwal...";
  status.classList.remove("error");
  try {
    const response = await fetch(`${API_BASE}/api/finance/amortization`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        investment: Number(document.getElementById("investment").value),
        useful_life: Number(document.getElementById("useful-life").value),
      }),
    });
    if (!response.ok) throw new Error("API gagal menghitung jadwal amortisasi.");
    const result = await response.json();
    document.getElementById("annual-expense").textContent = formatCurrency(result.annual_expense);
    const rows = document.getElementById("amortization-rows");
    rows.replaceChildren(...result.schedule.map((item) => {
      const row = document.createElement("tr");
      [item.year, item.opening_book_value, item.annual_expense, item.closing_book_value].forEach((value, index) => {
        const cell = document.createElement("td");
        cell.textContent = index === 0 ? `Tahun ${value}` : formatCurrency(value);
        row.append(cell);
      });
      return row;
    }));
    status.textContent = "Jadwal amortisasi berhasil dihitung.";
  } catch (error) {
    status.textContent = error.message || "Gagal menghitung amortisasi.";
    status.classList.add("error");
  }
};

const calculateTax = async (event) => {
  event.preventDefault();
  setStatus("Menghitung data dari API...");

  try {
    const [ppnResponse, pph21Response, ebupotResponse] = await Promise.all([
      fetch(`${API_BASE}/api/tax/ppn-gross-up`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          omzet_supermarket: Number(document.getElementById("omzet-supermarket").value),
          omzet_otc: Number(document.getElementById("omzet-otc").value),
          omzet_resep: Number(document.getElementById("omzet-resep").value),
        }),
      }),
      fetch(`${API_BASE}/api/tax/pph21-separator`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          jasa_bruto: Number(document.getElementById("jasa-bruto").value),
          persentase_sarana: Number(document.getElementById("persentase-sarana").value),
        }),
      }),
      fetch(`${API_BASE}/api/tax/ebupot-unifikasi`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          kso_bruto: Number(document.getElementById("kso-bruto").value),
          sewa_bruto: Number(document.getElementById("sewa-bruto").value),
        }),
      }),
    ]);

    if (!ppnResponse.ok || !pph21Response.ok || !ebupotResponse.ok) {
      throw new Error("API mengembalikan error.");
    }

    const [ppn, pph21, ebupot] = await Promise.all([
      ppnResponse.json(),
      pph21Response.json(),
      ebupotResponse.json(),
    ]);

    const totalPpn = ppn.total_ppn;
    const totalPph21 = pph21.dpp_pph21;
    const totalPph23 = ebupot.pph23_terutang;
    const totalPph42 = ebupot.pph42_terutang;
    const total = totalPpn + totalPph21 + totalPph23 + totalPph42;

    document.getElementById("result-ppn").textContent = formatCurrency(totalPpn);
    document.getElementById("result-dpp").textContent = formatCurrency(ppn.total_dpp);
    document.getElementById("result-pph21").textContent = formatCurrency(totalPph21);
    document.getElementById("result-pph23").textContent = formatCurrency(totalPph23);
    document.getElementById("result-pph42").textContent = formatCurrency(totalPph42);
    document.getElementById("result-total").textContent = formatCurrency(total);
    setStatus("Perhitungan berhasil diterima dari API.");
  } catch (error) {
    setStatus(error.message || "Gagal menghitung data.", true);
  }
};

const generateXml = async (event) => {
  event.preventDefault();
  const status = document.getElementById("xml-status");
  status.textContent = "Membuat file XML...";
  status.classList.remove("error");

  try {
    const response = await fetch(`${API_BASE}/api/tax/xml-coretax`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        npwp: document.getElementById("xml-npwp").value.trim(),
        nama_penjual: document.getElementById("xml-seller").value.trim(),
        items: [{
          kode: document.getElementById("xml-code").value.trim(),
          nomor: document.getElementById("xml-number").value.trim(),
          tanggal: document.getElementById("xml-date").value,
          deskripsi: document.getElementById("xml-description").value.trim(),
          dpp: Number(document.getElementById("xml-dpp").value),
          ppn: Number(document.getElementById("xml-ppn").value),
        }],
      }),
    });

    if (!response.ok) {
      throw new Error("API gagal membuat XML. Periksa kembali data faktur.");
    }

    const xml = await response.blob();
    const url = URL.createObjectURL(xml);
    const download = document.createElement("a");
    download.href = url;
    download.download = "faktur-coretax.xml";
    download.click();
    URL.revokeObjectURL(url);
    status.textContent = "XML berhasil dibuat dan diunduh.";
  } catch (error) {
    status.textContent = error.message || "Gagal membuat XML.";
    status.classList.add("error");
  }
};

const toggleMenu = () => {
  const menu = document.getElementById("nav-menu");
  const toggle = document.getElementById("nav-toggle");
  const isOpen = menu.classList.toggle("open");
  toggle.setAttribute("aria-expanded", String(isOpen));
};

const initFaq = () => {
  document.querySelectorAll(".faq-question").forEach((button) => {
    button.addEventListener("click", () => {
      const item = button.closest(".faq-item");
      const isOpen = item.classList.contains("active");
      document.querySelectorAll(".faq-item").forEach((faq) => {
        faq.classList.remove("active");
        faq.querySelector(".faq-question").setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        item.classList.add("active");
        button.setAttribute("aria-expanded", "true");
      }
    });
  });
};

document.addEventListener("DOMContentLoaded", () => {
  loadDashboard();
  initFaq();
  document.getElementById("nav-toggle").addEventListener("click", toggleMenu);
  document.getElementById("calc-form").addEventListener("submit", calculateTax);
  document.getElementById("xml-form").addEventListener("submit", generateXml);
  document.getElementById("amortization-form").addEventListener("submit", calculateAmortization);
});
