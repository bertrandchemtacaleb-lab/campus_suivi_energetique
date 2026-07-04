"""Page : Alertes."""
import streamlit as st
from database.session import SessionLocal
from models.alert import Alert

st.set_page_config(page_title="Alertes — SCIP", layout="wide")
st.title("🚨 Alertes")

db = SessionLocal()
alerts = db.query(Alert).order_by(Alert.created_at.desc()).all()

if not alerts:
    st.success("Aucune alerte active.")
else:
    for a in alerts:
        icon = {"info": "ℹ️", "warning": "⚠️", "critical": "🔴"}.get(a.severity, "ℹ️")
        st.write(f"{icon} **{a.type}** — {a.message} ({a.created_at:%d/%m/%Y %H:%M})")

db.close()
