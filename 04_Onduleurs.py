"""Page : Gestion des onduleurs."""
import streamlit as st
from database.session import SessionLocal
from models.inverter import Inverter

st.set_page_config(page_title="Onduleurs — SCIP", layout="wide")
st.title("🔌 Gestion des onduleurs")

db = SessionLocal()
inverters = db.query(Inverter).all()

if not inverters:
    st.warning("Aucun onduleur en base.")
else:
    st.dataframe(
        [{
            "Marque": i.brand, "Modèle": i.model, "Puissance (kW)": i.power_kw,
            "Rendement (%)": i.efficiency, "Température (°C)": i.temperature_c,
            "Statut": i.status, "Alarmes": i.active_alarms,
        } for i in inverters],
        use_container_width=True,
    )

db.close()
