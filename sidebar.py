"""Composant réutilisable : barre latérale commune (filtres, infos session)."""
import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.header("SCIP")
        st.caption("Solar Campus Intelligence Platform")
        st.divider()
        # TODO : ajouter sélecteur de bâtiment, plage de dates, etc.
