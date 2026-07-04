"""
Générateur de données simulées, utilisé tant que le matériel réel
(capteurs, onduleurs, automates) n'est pas raccordé.

Implémente EnergyDataSource afin d'être interchangeable avec les futurs
connecteurs réels (MQTT / Modbus) sans impact sur services/.
"""
import random
from integration.interfaces import EnergyDataSource


class SimulatedDataSource(EnergyDataSource):
    def get_current_production(self) -> float:
        return round(random.uniform(50, 500), 2)  # kW

    def get_current_consumption(self) -> float:
        return round(random.uniform(80, 400), 2)  # kW

    def get_battery_status(self, battery_id: int) -> dict:
        return {
            "battery_id": battery_id,
            "soc": round(random.uniform(20, 100), 1),
            "soh": round(random.uniform(85, 100), 1),
            "voltage": round(random.uniform(48, 54), 1),
            "current": round(random.uniform(-50, 50), 1),
            "temperature_c": round(random.uniform(18, 35), 1),
        }

    def get_inverter_status(self, inverter_id: int) -> dict:
        return {
            "inverter_id": inverter_id,
            "power_kw": round(random.uniform(0, 100), 1),
            "temperature_c": round(random.uniform(25, 60), 1),
            "frequency_hz": 50.0,
            "status": random.choice(["actif", "actif", "actif", "alarme"]),
        }

    def get_weather(self) -> dict:
        return {
            "irradiation_w_m2": round(random.uniform(0, 1000), 1),
            "temperature_c": round(random.uniform(18, 35), 1),
            "humidity_pct": round(random.uniform(30, 90), 1),
            "wind_speed_ms": round(random.uniform(0, 12), 1),
        }
