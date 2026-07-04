"""
Service métier : calculs énergétiques (production, consommation, rendement).
Ne dépend que de l'interface EnergyDataSource et de la base de données —
jamais d'un connecteur concret.
"""
from sqlalchemy.orm import Session
from sqlalchemy import func
from integration.interfaces import get_active_data_source
from models.history import EnergyReading


class EnergyService:
    def __init__(self, db: Session):
        self.db = db
        self.data_source = get_active_data_source()

    def get_live_snapshot(self) -> dict:
        """Retourne l'état énergétique instantané du site."""
        production = self.data_source.get_current_production()
        consumption = self.data_source.get_current_consumption()
        return {
            "production_kw": production,
            "consumption_kw": consumption,
            "autonomy_kw": round(production - consumption, 2),
        }

    def get_aggregated_production(self, source_entity: str, granularity: str = "day") -> float:
        """Agrège la production sur une entité (bâtiment, panneau...) et une
        granularité donnée, à partir des relevés bruts en base."""
        query = self.db.query(func.sum(EnergyReading.value_kwh)).filter(
            EnergyReading.source_entity == source_entity,
            EnergyReading.source_type == "production",
        )
        # TODO : filtrer par fenêtre temporelle selon `granularity`
        # (hour/day/week/month/semester/year) via EnergyReading.timestamp.
        return query.scalar() or 0.0

    def compute_performance_ratio(self, expected_kwh: float, actual_kwh: float) -> float:
        """Calcule le Performance Ratio (PR), indicateur clé de rendement PV."""
        if expected_kwh <= 0:
            return 0.0
        return round((actual_kwh / expected_kwh) * 100, 2)
