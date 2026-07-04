"""Point d'entrée de l'application Streamlit SCIP."""
import streamlit as st

st.set_page_config(
    page_title="SCIP — Solar Campus Intelligence Platform",
    page_icon="☀️",
    layout="wide",
)

st.title("☀️ Solar Campus Intelligence Platform")
st.markdown(
    """
    Bienvenue sur la plateforme de supervision de la centrale photovoltaïque du campus.

    Utilisez le menu latéral pour accéder aux différents modules :
    tableau de bord, jumeau numérique, gestion des équipements,
    intelligence artificielle, simulation, maintenance, finance et rapports.
    """
)

st.info(
    "Données actuellement en mode **simulé**. "
    "Basculez `DATA_SOURCE_MODE=real` dans `.env` une fois le matériel raccordé."
)
