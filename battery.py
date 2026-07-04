"""Modèle : batteries de stockage."""
from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Battery(Base):
    __tablename__ = "batteries"

    id: Mapped[int] = mapped_column(primary_key=True)
    technology: Mapped[str] = mapped_column(String(50))       # Lithium, GEL, AGM...
    capacity_ah: Mapped[float] = mapped_column(Float)
    energy_kwh: Mapped[float] = mapped_column(Float)
    voltage: Mapped[float] = mapped_column(Float)
    depth_of_discharge: Mapped[float] = mapped_column(Float)  # %
    soc: Mapped[float] = mapped_column(Float, default=100.0)   # state of charge %
    soh: Mapped[float] = mapped_column(Float, default=100.0)   # state of health %
    cycles: Mapped[int] = mapped_column(Integer, default=0)
    temperature_c: Mapped[float] = mapped_column(Float, nullable=True)
    current_a: Mapped[float] = mapped_column(Float, nullable=True)

    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=True)
    building: Mapped["Building"] = relationship(back_populates="batteries")
