"""Page : Tableau de bord — vue temps réel de la centrale."""
import streamlit as st
from database.session import SessionLocal
from services.energy_service import EnergyService
from components.kpi_cards import render_kpi_row
from components.charts import line_chart

st.set_page_config(page_title="Tableau de bord — SCIP", layout="wide")
st.title("📊 Tableau de bord")

db = SessionLocal()
energy_service = EnergyService(db)
snapshot = energy_service.get_live_snapshot()

render_kpi_row({
    "Production instantanée": f"{snapshot['production_kw']} kW",
    "Consommation instantanée": f"{snapshot['consumption_kw']} kW",
    "Autonomie": f"{snapshot['autonomy_kw']} kW",
})

st.divider()
st.subheader("Production sur 24h (exemple)")
# TODO : remplacer par les relevés réels agrégés via EnergyService
demo_hours = list(range(24))
demo_production = [max(0, 50 * (1 - abs(h - 12) / 12)) for h in demo_hours]
st.plotly_chart(line_chart(demo_hours, demo_production, "Production (kW)", "kW"), use_container_width=True)

db.close()
