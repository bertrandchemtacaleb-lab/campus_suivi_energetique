"""Composant réutilisable : authentification simple pour Streamlit."""
import streamlit as st


def require_login() -> bool:
    """À enrichir : vérification de session / JWT, gestion des rôles.
    Retourne True si l'utilisateur est authentifié."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.warning("Authentification requise (module à implémenter — Phase 1/7).")
        return False
    return True
