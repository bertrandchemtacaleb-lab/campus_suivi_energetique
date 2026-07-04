"""Page : Administration — utilisateurs, rôles, permissions, journal."""
import streamlit as st
from components.auth import require_login

st.set_page_config(page_title="Administration — SCIP", layout="wide")
st.title("⚙️ Administration")

if not require_login():
    st.stop()

tab_users, tab_roles, tab_log, tab_config = st.tabs(
    ["Utilisateurs", "Rôles & permissions", "Journal", "Configuration"]
)

with tab_users:
    st.write("Gestion des utilisateurs — CRUD à implémenter (Phase 5).")
with tab_roles:
    st.write("Gestion des rôles et permissions — à implémenter (Phase 5).")
with tab_log:
    st.write("Journal d'activité — à implémenter (Phase 5).")
with tab_config:
    st.write("Paramètres de la plateforme — à implémenter (Phase 5).")
