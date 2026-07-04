"""Page : Simulation — moteur what-if."""
import streamlit as st
from services.simulation_service import SimulationService, SimulationParameters

st.set_page_config(page_title="Simulation — SCIP", layout="wide")
st.title("🧪 Simulation")

col1, col2 = st.columns(2)
with col1:
    num_panels = st.number_input("Nombre de panneaux", min_value=1, value=100)
    panel_power = st.number_input("Puissance unitaire (Wc)", min_value=50, value=400)
    tilt = st.slider("Inclinaison (°)", 0, 90, 30)
with col2:
    orientation = st.slider("Orientation / azimut (°)", -180, 180, 0)
    battery_capacity = st.number_input("Capacité batterie (kWh)", min_value=0.0, value=50.0)
    consumption = st.number_input("Consommation estimée (kWh/jour)", min_value=0.0, value=800.0)

if st.button("Lancer la simulation"):
    params = SimulationParameters(
        num_panels=num_panels, panel_power_wc=panel_power, tilt_deg=tilt,
        orientation_deg=orientation, battery_capacity_kwh=battery_capacity,
        estimated_consumption_kwh_per_day=consumption,
    )
    result = SimulationService.run(params)
    st.success("Simulation terminée")
    st.json(result)
