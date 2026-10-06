from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_frontend_assets_are_served():
    assert client.get("/").status_code == 200
    assert client.get("/style.css").status_code == 200
    assert client.get("/script.js").status_code == 200


def test_dashboard_data():
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    payload = response.json()
    assert payload["kpis"]["total_omzet"] == 57_000_000_000
    assert len(payload["audit_breakdown"]) == 5


def test_amortization_schedule():
    response = client.post(
        "/api/finance/amortization",
        json={"investment": 18_000_000_000, "useful_life": 4},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["annual_expense"] == 4_500_000_000
    assert len(payload["schedule"]) == 4
    assert payload["schedule"][-1]["closing_book_value"] == 0


def test_amortization_rejects_unsupported_life():
    response = client.post(
        "/api/finance/amortization",
        json={"investment": 18_000_000_000, "useful_life": 5},
    )
    assert response.status_code == 422


def test_ppn_gross_up():
    response = client.post(
        "/api/tax/ppn-gross-up",
        json={"omzet_supermarket": 45_000_000_000, "omzet_otc": 8_000_000_000, "omzet_resep": 4_000_000_000},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["total_dpp"] == 51_351_351_351.35135
    assert payload["total_ppn"] == 5_648_648_648.648649


def test_pph21_separator():
    response = client.post(
        "/api/tax/pph21-separator",
        json={"jasa_bruto": 1_500_000_000, "persentase_sarana": 50},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["jasa_sarana"] == 750_000_000.0
    assert payload["jasa_murni"] == 750_000_000.0
    assert payload["dpp_pph21"] == 375_000_000.0


def test_ebupot_unifikasi():
    response = client.post(
        "/api/tax/ebupot-unifikasi",
        json={"kso_bruto": 250_000_000, "sewa_bruto": 300_000_000},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["pph23_terutang"] == 5_000_000.0
    assert payload["pph42_terutang"] == 30_000_000.0


def test_xml_generator():
    response = client.post(
        "/api/tax/xml-coretax",
        json={
            "npwp": "013456789012000",
            "nama_penjual": "PT SERBA ADA SEJAHTERA",
            "perusahaan": "PT Serba Ada Sejahtera",
            "items": [
                {"kode": "01", "nomor": "010.000-25.00000001", "tanggal": "2025-12-31", "deskripsi": "Penjualan Ritel", "dpp": 40_540_540_541, "ppn": 4_459_459_946},
                {"kode": "01", "nomor": "010.000-25.00000002", "tanggal": "2025-12-31", "deskripsi": "Penjualan Apotek", "dpp": 7_207_207_207, "ppn": 792_792_793},
            ],
        },
    )
    assert response.status_code == 200
    xml = response.text
    assert xml.startswith("<?xml")
    assert "<TAX_INVOICE_BATCH" in xml
    assert "010.000-25.00000002" in xml


def test_invalid_payload_returns_422():
    response = client.post("/api/tax/ppn-gross-up", json={"omzet_supermarket": -1})
    assert response.status_code == 422
