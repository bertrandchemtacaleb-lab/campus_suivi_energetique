"""Tests unitaires : modèles SQLAlchemy."""
from models.building import Building
from models.panel import Panel


def test_create_building(db_session):
    building = Building(name="Bâtiment A", usage="administration", surface_m2=500.0)
    db_session.add(building)
    db_session.commit()

    assert building.id is not None
    assert db_session.query(Building).count() == 1


def test_panel_linked_to_building(db_session):
    building = Building(name="Bâtiment B", usage="laboratoire", surface_m2=300.0)
    db_session.add(building)
    db_session.commit()

    panel = Panel(
        identifier="PV-0001", brand="SunPower", model="X22-370",
        power_wc=370, efficiency=21.5, surface_m2=1.8,
        orientation_deg=0, tilt_deg=30, building_id=building.id,
    )
    db_session.add(panel)
    db_session.commit()

    assert panel.building.name == "Bâtiment B"
