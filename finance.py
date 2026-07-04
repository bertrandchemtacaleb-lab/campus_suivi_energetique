"""Modèle : suivi financier (ROI, amortissement, économies)."""
from sqlalchemy import Float, Date
from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base


class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    period: Mapped[Date] = mapped_column(Date)  # mois de référence
    investment_total: Mapped[float] = mapped_column(Float, default=0.0)
    maintenance_cost: Mapped[float] = mapped_column(Float, default=0.0)
    energy_savings: Mapped[float] = mapped_column(Float, default=0.0)   # € économisés
    grid_kwh_price: Mapped[float] = mapped_column(Float, default=0.0)
    roi_percent: Mapped[float] = mapped_column(Float, nullable=True)
    payback_years: Mapped[float] = mapped_column(Float, nullable=True)
