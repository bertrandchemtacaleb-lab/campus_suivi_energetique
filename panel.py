"""Modèle : panneaux photovoltaïques."""
from sqlalchemy import String, Float, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Panel(Base):
    __tablename__ = "panels"

    id: Mapped[int] = mapped_column(primary_key=True)
    identifier: Mapped[str] = mapped_column(String(50), unique=True)
    brand: Mapped[str] = mapped_column(String(80))
    model: Mapped[str] = mapped_column(String(80))
    power_wc: Mapped[float] = mapped_column(Float)           # puissance nominale (Wc)
    voc: Mapped[float] = mapped_column(Float, nullable=True)  # tension à vide
    isc: Mapped[float] = mapped_column(Float, nullable=True)  # courant de court-circuit
    vmpp: Mapped[float] = mapped_column(Float, nullable=True)
    impp: Mapped[float] = mapped_column(Float, nullable=True)
    efficiency: Mapped[float] = mapped_column(Float)
    surface_m2: Mapped[float] = mapped_column(Float)
    orientation_deg: Mapped[float] = mapped_column(Float)     # azimut
    tilt_deg: Mapped[float] = mapped_column(Float)            # inclinaison
    string_number: Mapped[int] = mapped_column(nullable=True)
    installation_date: Mapped[Date] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(30), default="actif")

    building_id: Mapped[int] = mapped_column(ForeignKey("buildings.id"), nullable=True)
    building: Mapped["Building"] = relationship(back_populates="panels")
