"""Génération de rapports PDF (synthèse énergétique, financière...)."""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_pdf_report(output_dir: str = "/tmp") -> str:
    """Génère un rapport PDF minimal et retourne son chemin.
    À enrichir avec les données réelles issues des services métier
    (production, consommation, finance, alertes...)."""
    filename = f"rapport_scip_{datetime.now():%Y%m%d_%H%M%S}.pdf"
    path = os.path.join(output_dir, filename)

    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Rapport SCIP — Solar Campus Intelligence Platform")
    c.setFont("Helvetica", 11)
    c.drawString(50, 770, f"Généré le {datetime.now():%d/%m/%Y %H:%M}")
    c.drawString(50, 740, "Section à compléter : production, consommation, finance, alertes.")
    c.save()
    return path
