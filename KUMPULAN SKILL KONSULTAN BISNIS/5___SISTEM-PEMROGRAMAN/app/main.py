from __future__ import annotations

from decimal import Decimal
from pathlib import Path
from typing import Literal
import xml.etree.ElementTree as ET

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="TaxBridge API", version="1.0.0")
PROJECT_ROOT = Path(__file__).resolve().parent.parent

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    status: str
    service: str


class PPNGrossUpInput(BaseModel):
    omzet_supermarket: float = Field(ge=0)
    omzet_otc: float = Field(ge=0)
    omzet_resep: float = Field(ge=0)


class PPNGrossUpOutput(BaseModel):
    categories: list[dict[str, float | str]]
    total_dpp: float
    total_ppn: float


class PPh21Input(BaseModel):
    jasa_bruto: float = Field(ge=0)
    persentase_sarana: float = Field(ge=0, le=100)


class PPh21Output(BaseModel):
    jasa_sarana: float
    jasa_murni: float
    dpp_pph21: float


class EbupotInput(BaseModel):
    kso_bruto: float = Field(ge=0)
    sewa_bruto: float = Field(ge=0)


class EbupotOutput(BaseModel):
    pph23_terutang: float
    pph42_terutang: float


class AmortizationInput(BaseModel):
    investment: float = Field(ge=0)
    useful_life: Literal[4, 8, 16, 20]


class DashboardResponse(BaseModel):
    kpis: dict[str, int | str]
    audit_breakdown: list[dict[str, int | str]]


class XMLItem(BaseModel):
    kode: str
    nomor: str
    tanggal: str
    deskripsi: str
    dpp: float = Field(ge=0)
    ppn: float = Field(ge=0)


class XMLGeneratorInput(BaseModel):
    npwp: str
    nama_penjual: str
    perusahaan: str = "PT Serba Ada Sejahtera"
    items: list[XMLItem]

    @field_validator("items")
    @classmethod
    def validate_items(cls, items: list[XMLItem]) -> list[XMLItem]:
        if not items:
            raise ValueError("items must contain at least one invoice")
        return items


@app.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="taxbridge-api")


@app.get("/api/dashboard", response_model=DashboardResponse)
def dashboard() -> DashboardResponse:
    return DashboardResponse(
        kpis={
            "total_omzet": 57_000_000_000,
            "kurang_bayar_pokok": 3_181_896_396,
            "sanksi_bunga": 122_065_495,
            "total_tagihan": 3_303_961_892,
        },
        audit_breakdown=[
            {"jenis_pajak": "PPN Penyerahan Apotek & Supermarket", "pokok_spt": 5_252_252_252, "pokok_audit": 5_648_648_649, "kurang_bayar": 396_396_396, "sanksi": 55_495_495, "total_tagihan": 451_891_892},
            {"jenis_pajak": "PPh Pasal 21 Dokter & Apoteker", "pokok_spt": 48_000_000, "pokok_audit": 103_500_000, "kurang_bayar": 55_500_000, "sanksi": 7_770_000, "total_tagihan": 63_270_000},
            {"jenis_pajak": "PPh Pasal 23 KSO Alat Cek Medis", "pokok_spt": 3_000_000, "pokok_audit": 8_000_000, "kurang_bayar": 5_000_000, "sanksi": 700_000, "total_tagihan": 5_700_000},
            {"jenis_pajak": "PPh Pasal 4(2) Sewa Booth Apotek", "pokok_spt": 15_000_000, "pokok_audit": 45_000_000, "kurang_bayar": 30_000_000, "sanksi": 4_200_000, "total_tagihan": 34_200_000},
            {"jenis_pajak": "PPh Badan (Tahunan 2025)", "pokok_spt": -1_925_000_000, "pokok_audit": 770_000_000, "kurang_bayar": 2_695_000_000, "sanksi": 53_900_000, "total_tagihan": 2_748_900_000},
        ],
    )


@app.post("/api/finance/amortization")
def amortization(payload: AmortizationInput) -> dict[str, float | list[dict[str, float | int]]]:
    annual_expense = payload.investment / payload.useful_life
    schedule = [
        {
            "year": year,
            "opening_book_value": payload.investment - (year - 1) * annual_expense,
            "annual_expense": annual_expense,
            "closing_book_value": payload.investment - year * annual_expense,
        }
        for year in range(1, payload.useful_life + 1)
    ]
    return {"annual_expense": annual_expense, "schedule": schedule}


@app.post("/api/tax/ppn-gross-up", response_model=PPNGrossUpOutput)
def ppn_gross_up(payload: PPNGrossUpInput) -> PPNGrossUpOutput:
    divisor = Decimal("111")
    rate = Decimal("0.11")

    def gross_up(value: float) -> Decimal:
        amount = Decimal(str(value))
        return amount * Decimal("100") / divisor

    def tax(value: Decimal) -> Decimal:
        return value * rate

    categories = [
        {
            "kategori": "Supermarket Ritel (BKP)",
            "nilai_bruto": payload.omzet_supermarket,
            "dpp": float(gross_up(payload.omzet_supermarket)),
            "ppn": float(tax(gross_up(payload.omzet_supermarket))),
        },
        {
            "kategori": "Apotek OTC (Obat Bebas)",
            "nilai_bruto": payload.omzet_otc,
            "dpp": float(gross_up(payload.omzet_otc)),
            "ppn": float(tax(gross_up(payload.omzet_otc))),
        },
        {
            "kategori": "Apotek Resep Dokter (BKP)",
            "nilai_bruto": payload.omzet_resep,
            "dpp": float(gross_up(payload.omzet_resep)),
            "ppn": float(tax(gross_up(payload.omzet_resep))),
        },
    ]
    total_dpp = float(sum((gross_up(payload.omzet_supermarket), gross_up(payload.omzet_otc), gross_up(payload.omzet_resep)), Decimal("0")))
    total_ppn = float(
        sum(
            (tax(gross_up(payload.omzet_supermarket)), tax(gross_up(payload.omzet_otc)), tax(gross_up(payload.omzet_resep))),
            Decimal("0"),
        ).quantize(Decimal("0.000001"))
    )
    return PPNGrossUpOutput(
        categories=categories,
        total_dpp=total_dpp,
        total_ppn=total_ppn,
    )


@app.post("/api/tax/pph21-separator", response_model=PPh21Output)
def pph21_separator(payload: PPh21Input) -> PPh21Output:
    jasa_sarana = payload.jasa_bruto * (payload.persentase_sarana / 100)
    jasa_murni = payload.jasa_bruto * ((100 - payload.persentase_sarana) / 100)
    dpp_pph21 = 0.5 * jasa_murni
    return PPh21Output(
        jasa_sarana=jasa_sarana,
        jasa_murni=jasa_murni,
        dpp_pph21=dpp_pph21,
    )


@app.post("/api/tax/ebupot-unifikasi", response_model=EbupotOutput)
def ebupot_unifikasi(payload: EbupotInput) -> EbupotOutput:
    return EbupotOutput(
        pph23_terutang=payload.kso_bruto * 0.02,
        pph42_terutang=payload.sewa_bruto * 0.10,
    )


@app.post("/api/tax/xml-coretax", response_class=PlainTextResponse)
def xml_coretax(payload: XMLGeneratorInput) -> PlainTextResponse:
    try:
        root = ET.Element("TAX_INVOICE_BATCH", {"version": "4.0", "npwp_penjual": payload.npwp, "nama_penjual": payload.nama_penjual})
        for item in payload.items:
            faktur = ET.SubElement(root, "FAKTUR_PAJAK")
            ET.SubElement(faktur, "KODE_TRANSAKSI").text = item.kode
            ET.SubElement(faktur, "NOMOR_FAKTUR").text = item.nomor
            ET.SubElement(faktur, "TANGGAL_FAKTUR").text = item.tanggal
            peny = ET.SubElement(faktur, "PENYERAHAN")
            ET.SubElement(peny, "DESKRIPSI").text = item.deskripsi
            ET.SubElement(peny, "DPP").text = str(int(item.dpp))
            ET.SubElement(peny, "PPN").text = str(int(item.ppn))
        xml = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        return PlainTextResponse(content=xml.decode("utf-8"), media_type="application/xml")
    except Exception as exc:  # pragma: no cover - should be unreachable
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    return FileResponse(PROJECT_ROOT / "index.html", media_type="text/html")


@app.get("/style.css")
def stylesheet() -> FileResponse:
    return FileResponse(PROJECT_ROOT / "style.css", media_type="text/css")


@app.get("/script.js")
def javascript() -> FileResponse:
    return FileResponse(PROJECT_ROOT / "script.js", media_type="application/javascript")
