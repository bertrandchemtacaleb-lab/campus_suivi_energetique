"""Modèles : maintenance (interventions, techniciens)."""
from sqlalchemy import String, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from database.base import Base


class Technician(Base):
    __tablename__ = "technicians"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    specialty: Mapped[str] = mapped_column(String(80), nullable=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=True)


class MaintenanceIntervention(Base):
    __tablename__ = "maintenance_interventions"

    id: Mapped[int] = mapped_column(primary_key=True)
    equipment_reference: Mapped[str] = mapped_column(String(80))  # ex: "panel:PV-0012"
    description: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(30), default="planifiée")
    scheduled_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    completed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    cost: Mapped[float] = mapped_column(Float, default=0.0)
    parts_used: Mapped[str] = mapped_column(Text, nullable=True)

    technician_id: Mapped[int] = mapped_column(ForeignKey("technicians.id"), nullable=True)
    technician: Mapped["Technician"] = relationship()
