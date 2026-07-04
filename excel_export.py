"""Export des données vers Excel (openpyxl)."""
from openpyxl import Workbook
from datetime import datetime
import os


def generate_excel_export(output_dir: str = "/tmp") -> str:
    filename = f"export_scip_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
    path = os.path.join(output_dir, filename)

    wb = Workbook()
    ws = wb.active
    ws.title = "Synthèse"
    ws.append(["Indicateur", "Valeur"])
    ws.append(["Généré le", datetime.now().strftime("%d/%m/%Y %H:%M")])
    # TODO : ajouter les feuilles production / consommation / finance / alertes
    wb.save(path)
    return path
