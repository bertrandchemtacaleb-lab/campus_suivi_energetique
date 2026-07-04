"""Endpoints : alertes."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.session import get_db
from models.alert import Alert
from api.schemas import AlertOut

router = APIRouter()


@router.get("/", response_model=list[AlertOut])
def list_alerts(resolved: bool | None = None, db: Session = Depends(get_db)):
    query = db.query(Alert)
    if resolved is not None:
        query = query.filter(Alert.resolved == resolved)
    return query.order_by(Alert.created_at.desc()).all()
