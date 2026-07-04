"""Page : Intelligence artificielle — prévisions, anomalies, assistant."""
import streamlit as st
from database.session import SessionLocal
from services.energy_service import EnergyService
from services.ai.assistant import EnergyAssistant

st.set_page_config(page_title="Intelligence Artificielle — SCIP", layout="wide")
st.title("🤖 Intelligence artificielle")

tab_forecast, tab_anomaly, tab_assistant = st.tabs(
    ["Prévisions", "Détection d'anomalies", "Assistant"]
)

with tab_forecast:
    st.write("Prévision de production / consommation — à entraîner sur l'historique réel (Phase 4).")

with tab_anomaly:
    st.write("Détection d'anomalies (IsolationForest) — à connecter aux relevés temps réel (Phase 4).")

with tab_assistant:
    db = SessionLocal()
    assistant = EnergyAssistant(EnergyService(db))
    question = st.text_input("Poser une question sur la centrale")
    if question:
        st.write(assistant.answer(question))
    db.close()
