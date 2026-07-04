"""Page : Gestion des batteries."""
import streamlit as st
from database.session import SessionLocal
from models.battery import Battery

st.set_page_config(page_title="Batteries — SCIP", layout="wide")
st.title("🔋 Gestion des batteries")

db = SessionLocal()
batteries = db.query(Battery).all()

if not batteries:
    st.warning("Aucune batterie en base.")
else:
    st.dataframe(
        [{
            "Technologie": b.technology, "Capacité (Ah)": b.capacity_ah,
            "Énergie (kWh)": b.energy_kwh, "SOC (%)": b.soc, "SOH (%)": b.soh,
            "Cycles": b.cycles, "Température (°C)": b.temperature_c,
        } for b in batteries],
        use_container_width=True,
    )

db.close()
