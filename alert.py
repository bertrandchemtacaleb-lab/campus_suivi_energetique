"""Modèle : alertes générées automatiquement."""
from sqlalchemy import String, DateTime, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.base import Base


class Alert(Base):
    __tablename__ = "alerts"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(50))     # production_faible, panne, surchauffe...
    severity: Mapped[str] = mapped_column(String(20))  # info, warning, critical
    message: Mapped[str] = mapped_column(Text)
    source_entity: Mapped[str] = mapped_column(String(80), nullable=True)  # ex: "inverter:12"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    resolved: Mapped[bool] = mapped_column(Boolean, default=False)
    resolved_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
