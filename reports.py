"""Endpoints : génération de rapports (PDF/Excel/CSV)."""
from fastapi import APIRouter
from fastapi.responses import FileResponse
from exports.pdf_report import generate_pdf_report
from exports.excel_export import generate_excel_export

router = APIRouter()


@router.get("/pdf")
def download_pdf_report():
    path = generate_pdf_report()
    return FileResponse(path, filename="rapport_scip.pdf", media_type="application/pdf")


@router.get("/excel")
def download_excel_export():
    path = generate_excel_export()
    return FileResponse(
        path, filename="export_scip.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
