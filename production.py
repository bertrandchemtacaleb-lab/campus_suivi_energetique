"""Endpoints : production et consommation en temps réel / historique."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from services.energy_service import EnergyService
from api.schemas import EnergySnapshot

router = APIRouter()


@router.get("/live", response_model=EnergySnapshot)
def get_live_snapshot(db: Session = Depends(get_db)):
    service = EnergyService(db)
    return service.get_live_snapshot()
