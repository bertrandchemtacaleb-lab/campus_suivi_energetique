"""Page : Historique des relevés (heure / jour / semaine / mois / année)."""
import streamlit as st

st.set_page_config(page_title="Historique — SCIP", layout="wide")
st.title("🕒 Historique")

granularity = st.radio(
    "Granularité", ["Heure", "Jour", "Semaine", "Mois", "Année"], horizontal=True
)
st.info(f"Vue « {granularity} » à connecter aux agrégations SQL sur EnergyReading (Phase 2).")
