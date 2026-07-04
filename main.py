"""
Point d'entrée de l'API REST SCIP (FastAPI).

Lancement : uvicorn api.main:app --reload
"""
from fastapi import FastAPI
from api.routers import production, buildings, equipment, alerts, reports

app = FastAPI(
    title="Solar Campus Intelligence Platform — API",
    description="API REST exposant les données de supervision de la centrale photovoltaïque.",
    version="1.0.0",
)

app.include_router(production.router, prefix="/api/production", tags=["Production"])
app.include_router(buildings.router, prefix="/api/buildings", tags=["Bâtiments"])
app.include_router(equipment.router, prefix="/api/equipment", tags=["Équipements"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["Alertes"])
app.include_router(reports.router, prefix="/api/reports", tags=["Rapports"])


@app.get("/health", tags=["Santé"])
def health_check():
    return {"status": "ok"}
