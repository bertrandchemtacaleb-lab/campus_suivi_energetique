"""Endpoints : gestion des bâtiments."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models.building import Building
from api.schemas import BuildingOut

router = APIRouter()


@router.get("/", response_model=list[BuildingOut])
def list_buildings(db: Session = Depends(get_db)):
    return db.query(Building).all()


@router.get("/{building_id}", response_model=BuildingOut)
def get_building(building_id: int, db: Session = Depends(get_db)):
    return db.get(Building, building_id)
