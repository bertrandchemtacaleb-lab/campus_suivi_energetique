"""Page : Gestion de la maintenance."""
import streamlit as st
from database.session import SessionLocal
from models.maintenance import MaintenanceIntervention

st.set_page_config(page_title="Maintenance — SCIP", layout="wide")
st.title("🛠️ Maintenance")

db = SessionLocal()
interventions = db.query(MaintenanceIntervention).all()

if not interventions:
    st.warning("Aucune intervention enregistrée.")
else:
    st.dataframe(
        [{
            "Équipement": i.equipment_reference, "Description": i.description,
            "Statut": i.status, "Coût": i.cost,
        } for i in interventions],
        use_container_width=True,
    )

with st.expander("➕ Planifier une intervention"):
    st.write("Formulaire à implémenter (Phase 5).")

db.close()
