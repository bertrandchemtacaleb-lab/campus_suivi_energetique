"""Schémas Pydantic pour l'API REST (validation des entrées/sorties)."""
from pydantic import BaseModel
from datetime import datetime


class EnergySnapshot(BaseModel):
    production_kw: float
    consumption_kw: float
    autonomy_kw: float


class BuildingOut(BaseModel):
    id: int
    name: str
    usage: str
    surface_m2: float

    model_config = {"from_attributes": True}


class AlertOut(BaseModel):
    id: int
    type: str
    severity: str
    message: str
    created_at: datetime
    resolved: bool

    model_config = {"from_attributes": True}
