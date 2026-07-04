"""
Service métier : moteur de simulation "what-if".

Permet de recalculer les indicateurs (production, autonomie, ROI...) en
fonction de paramètres modifiés par l'utilisateur (nombre de panneaux,
inclinaison, capacité batterie, consommation) — sans toucher aux données
réelles en base.
"""
from dataclasses import dataclass


@dataclass
class SimulationParameters:
    num_panels: int
    panel_power_wc: float
    tilt_deg: float
    orientation_deg: float
    battery_capacity_kwh: float
    estimated_consumption_kwh_per_day: float
    peak_sun_hours: float = 5.0  # PSH par défaut, à ajuster selon la localisation


class SimulationService:
    @staticmethod
    def run(params: SimulationParameters) -> dict:
        installed_power_kwc = (params.num_panels * params.panel_power_wc) / 1000

        # Facteur d'orientation/inclinaison simplifié — à remplacer par un
        # modèle solaire plus précis (ex: pvlib) si une meilleure fidélité
        # est nécessaire.
        orientation_factor = 1 - abs(params.orientation_deg) / 180 * 0.3
        tilt_factor = 1 - abs(params.tilt_deg - 30) / 90 * 0.2
        performance_factor = max(0.5, orientation_factor * tilt_factor)

        estimated_daily_production_kwh = (
            installed_power_kwc * params.peak_sun_hours * performance_factor
        )
        autonomy_ratio = (
            estimated_daily_production_kwh / params.estimated_consumption_kwh_per_day
            if params.estimated_consumption_kwh_per_day > 0 else 0
        )

        return {
            "installed_power_kwc": round(installed_power_kwc, 2),
            "estimated_daily_production_kwh": round(estimated_daily_production_kwh, 2),
            "autonomy_ratio_pct": round(autonomy_ratio * 100, 1),
            "battery_capacity_kwh": params.battery_capacity_kwh,
        }
