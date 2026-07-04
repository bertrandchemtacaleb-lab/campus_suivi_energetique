"""Page : Digital Twin — jumeau numérique interactif du campus."""
import streamlit as st
from database.session import SessionLocal
from models.building import Building

st.set_page_config(page_title="Digital Twin — SCIP", layout="wide")
st.title("🏛️ Digital Twin du campus")

st.info(
    "Prototype à construire en priorité (risque technique élevé — voir rapport, section 6). "
    "Objectif : rendu 3D interactif (PyVista ou Plotly 3D) avec sélection de bâtiment, "
    "flux d'énergie animés et code couleur selon l'état."
)

db = SessionLocal()
buildings = db.query(Building).all()

if not buildings:
    st.warning("Aucun bâtiment en base. Ajoutez des bâtiments via le module Administration ou les jeux de données démo.")
else:
    selected_name = st.selectbox("Sélectionner un bâtiment", [b.name for b in buildings])
    selected = next(b for b in buildings if b.name == selected_name)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(f"Vue 3D — {selected.name}")
        st.write("Zone réservée au rendu PyVista / Plotly 3D (à implémenter, Phase 3).")
    with col2:
        st.subheader("Fiche bâtiment")
        st.write(f"**Usage** : {selected.usage}")
        st.write(f"**Surface** : {selected.surface_m2} m²")
        st.write(f"**Étages** : {selected.num_floors}")
        st.write(f"**Priorité d'alimentation** : {selected.priority}")

db.close()
