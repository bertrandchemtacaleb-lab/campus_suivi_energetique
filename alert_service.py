"""Service métier : génération et gestion des alertes."""
from sqlalchemy.orm import Session
from models.alert import Alert

# Seuils par défaut — à externaliser en configuration/base de données
# si un paramétrage par bâtiment ou équipement est nécessaire.
THRESHOLDS = {
    "low_production_kw": 5.0,
    "battery_low_soc_pct": 20.0,
    "inverter_overheat_c": 65.0,
    "excessive_consumption_kw": 400.0,
}


class AlertService:
    def __init__(self, db: Session):
        self.db = db

    def check_and_raise(self, metric: str, value: float, source_entity: str) -> Alert | None:
        """Vérifie une métrique par rapport aux seuils et crée une alerte si besoin."""
        rules = {
            "production_kw": ("low_production_kw", value < THRESHOLDS["low_production_kw"], "warning"),
            "battery_soc": ("battery_low_soc_pct", value < THRESHOLDS["battery_low_soc_pct"], "warning"),
            "inverter_temp_c": ("inverter_overheat_c", value > THRESHOLDS["inverter_overheat_c"], "critical"),
            "consumption_kw": ("excessive_consumption_kw", value > THRESHOLDS["excessive_consumption_kw"], "warning"),
        }
        if metric not in rules:
            return None

        threshold_key, triggered, severity = rules[metric]
        if not triggered:
            return None

        alert = Alert(
            type=metric,
            severity=severity,
            message=f"Seuil '{threshold_key}' dépassé pour {source_entity} (valeur={value})",
            source_entity=source_entity,
        )
        self.db.add(alert)
        self.db.commit()
        return alert
