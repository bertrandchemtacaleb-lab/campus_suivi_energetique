"""Service métier : planification et suivi de la maintenance."""
from sqlalchemy.orm import Session
from datetime import datetime
from models.maintenance import MaintenanceIntervention


class MaintenanceService:
    def __init__(self, db: Session):
        self.db = db

    def schedule_intervention(self, equipment_reference: str, description: str,
                               scheduled_at: datetime, technician_id: int | None = None) -> MaintenanceIntervention:
        intervention = MaintenanceIntervention(
            equipment_reference=equipment_reference,
            description=description,
            scheduled_at=scheduled_at,
            technician_id=technician_id,
            status="planifiée",
        )
        self.db.add(intervention)
        self.db.commit()
        return intervention

    def close_intervention(self, intervention_id: int, cost: float, parts_used: str = "") -> None:
        intervention = self.db.get(MaintenanceIntervention, intervention_id)
        if intervention is None:
            raise ValueError(f"Intervention {intervention_id} introuvable")
        intervention.status = "terminée"
        intervention.completed_at = datetime.utcnow()
        intervention.cost = cost
        intervention.parts_used = parts_used
        self.db.commit()
