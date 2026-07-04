"""Page : Génération de rapports."""
import streamlit as st
from exports.pdf_report import generate_pdf_report
from exports.excel_export import generate_excel_export

st.set_page_config(page_title="Rapports — SCIP", layout="wide")
st.title("📄 Rapports")

col1, col2 = st.columns(2)
with col1:
    if st.button("Générer un rapport PDF"):
        path = generate_pdf_report()
        with open(path, "rb") as f:
            st.download_button("Télécharger le PDF", f, file_name="rapport_scip.pdf")

with col2:
    if st.button("Générer un export Excel"):
        path = generate_excel_export()
        with open(path, "rb") as f:
            st.download_button("Télécharger l'Excel", f, file_name="export_scip.xlsx")
