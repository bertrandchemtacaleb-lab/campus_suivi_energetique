"""Page : Finance — ROI, amortissement, économies."""
import streamlit as st
from services.finance_service import FinanceService
from components.kpi_cards import render_kpi_row

st.set_page_config(page_title="Finance — SCIP", layout="wide")
st.title("💰 Finance")

st.subheader("Calculette d'indicateurs")
investment = st.number_input("Investissement total (€)", min_value=0.0, value=100000.0)
annual_savings = st.number_input("Économies annuelles (€)", min_value=0.0, value=15000.0)
kwh_produced = st.number_input("kWh produits cumulés", min_value=0.0, value=50000.0)

if st.button("Calculer"):
    roi = FinanceService.compute_roi(annual_savings, investment)
    payback = FinanceService.compute_payback_period(investment, annual_savings)
    co2 = FinanceService.compute_co2_avoided(kwh_produced)
    render_kpi_row({
        "ROI annuel": f"{roi} %",
        "Amortissement": f"{payback} ans",
        "CO₂ évité": f"{co2} kg",
    })
