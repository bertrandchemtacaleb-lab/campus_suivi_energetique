"""Modèle : bâtiments du campus."""
from sqlalchemy import String, Float, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Building(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    usage: Mapped[str] = mapped_column(String(80))          # administration, labo, résidence...
    surface_m2: Mapped[float] = mapped_column(Float)
    num_floors: Mapped[int] = mapped_column(Integer, default=1)
    num_rooms: Mapped[int] = mapped_column(Integer, default=0)
    latitude: Mapped[float] = mapped_column(Float, nullable=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=True)
    priority: Mapped[int] = mapped_column(Integer, default=3)  # priorité d'alimentation
    equipment_notes: Mapped[str] = mapped_column(Text, nullable=True)

    panels: Mapped[list["Panel"]] = relationship(back_populates="building")
    inverters: Mapped[list["Inverter"]] = relationship(back_populates="building")
    batteries: Mapped[list["Battery"]] = relationship(back_populates="building")
