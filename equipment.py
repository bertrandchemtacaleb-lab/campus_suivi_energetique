"""Endpoints : panneaux, onduleurs, batteries."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models.panel import Panel
from models.inverter import Inverter
from models.battery import Battery

router = APIRouter()


@router.get("/panels")
def list_panels(db: Session = Depends(get_db)):
    return db.query(Panel).all()


@router.get("/inverters")
def list_inverters(db: Session = Depends(get_db)):
    return db.query(Inverter).all()


@router.get("/batteries")
def list_batteries(db: Session = Depends(get_db)):
    return db.query(Battery).all()
