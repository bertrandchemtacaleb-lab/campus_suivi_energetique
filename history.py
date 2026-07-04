"""Modèle : historique des relevés énergétiques (production/consommation)."""
from sqlalchemy import Float, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.base import Base


class EnergyReading(Base):
    """Relevé horodaté — la granularité (heure/jour/mois) se calcule par
    agrégation SQL à partir de ces relevés bruts, plutôt que d'être stockée
    en dur, afin d'éviter la duplication."""
    __tablename__ = "energy_readings"

    id: Mapped[int] = mapped_column(primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True)
    source_type: Mapped[str] = mapped_column(String(30))   # "production" | "consumption"
    source_entity: Mapped[str] = mapped_column(String(80))  # ex: "building:3", "panel:12"
    value_kwh: Mapped[float] = mapped_column(Float)
    irradiation: Mapped[float] = mapped_column(Float, nullable=True)
    temperature_c: Mapped[float] = mapped_column(Float, nullable=True)
    humidity: Mapped[float] = mapped_column(Float, nullable=True)
    wind_speed: Mapped[float] = mapped_column(Float, nullable=True)
