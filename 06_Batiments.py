"""Page : Gestion des bâtiments."""
import streamlit as st
from database.session import SessionLocal
from models.building import Building

st.set_page_config(page_title="Bâtiments — SCIP", layout="wide")
st.title("🏢 Gestion des bâtiments")

db = SessionLocal()
buildings = db.query(Building).all()

if not buildings:
    st.warning("Aucun bâtiment en base.")
else:
    st.dataframe(
        [{
            "Nom": b.name, "Usage": b.usage, "Surface (m²)": b.surface_m2,
            "Étages": b.num_floors, "Salles": b.num_rooms, "Priorité": b.priority,
        } for b in buildings],
        use_container_width=True,
    )

db.close()
