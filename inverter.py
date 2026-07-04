"""Modèle : onduleurs."""
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Inverter(Base):
    __tablename__ = "inverters"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(String(80))
    model: Mapped[str] = mapped_column(String(80))
    power_kw: Mapped[float] = mapped_column(Float)
    mppt_inputs: Mapped[int] = mapped_column(nullable=True)
    efficiency: Mapped[float] = mapped_column(Float, nullable=True)
    input_voltage: Mapped[float] = mapped_column(Float, nullable=True)
    output_voltage: Mapped[float] = mapped_column(Float, nullable=True)
    frequency_hz: Mapped[float] = mapped_column(Float, default=50.0)
    temperature_c: Mapped[float] = mapped_column(Float, nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="actif")
    active_alarms: Mapped[str] = mapped_column(String(255), nullable=True)

    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=True)
    building: Mapped["Building"] = relationship(back_populates="inverters")
