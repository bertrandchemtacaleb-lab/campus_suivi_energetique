"""Page : Gestion des panneaux photovoltaïques."""
import streamlit as st
from database.session import SessionLocal
from models.panel import Panel

st.set_page_config(page_title="Panneaux — SCIP", layout="wide")
st.title("🔆 Gestion des panneaux")

db = SessionLocal()
panels = db.query(Panel).all()

if not panels:
    st.warning("Aucun panneau en base.")
else:
    st.dataframe(
        [{
            "Identifiant": p.identifier, "Marque": p.brand, "Modèle": p.model,
            "Puissance (Wc)": p.power_wc, "Rendement (%)": p.efficiency,
            "Orientation (°)": p.orientation_deg, "Inclinaison (°)": p.tilt_deg,
            "Statut": p.status,
        } for p in panels],
        use_container_width=True,
    )

with st.expander("➕ Ajouter un panneau"):
    st.write("Formulaire à implémenter (CRUD complet, Phase 2).")

db.close()
