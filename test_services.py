"""Tests unitaires : services métier."""
from services.finance_service import FinanceService
from services.simulation_service import SimulationService, SimulationParameters
from services.alert_service import AlertService


def test_compute_roi():
    assert FinanceService.compute_roi(15000, 100000) == 15.0


def test_compute_payback_period():
    assert FinanceService.compute_payback_period(100000, 20000) == 5.0


def test_simulation_service_runs():
    params = SimulationParameters(
        num_panels=100, panel_power_wc=400, tilt_deg=30, orientation_deg=0,
        battery_capacity_kwh=50, estimated_consumption_kwh_per_day=800,
    )
    result = SimulationService.run(params)
    assert result["installed_power_kwc"] == 40.0
    assert result["estimated_daily_production_kwh"] > 0


def test_alert_raised_on_low_battery(db_session):
    service = AlertService(db_session)
    alert = service.check_and_raise("battery_soc", 10.0, "battery:1")
    assert alert is not None
    assert alert.severity == "warning"


def test_no_alert_when_within_threshold(db_session):
    service = AlertService(db_session)
    alert = service.check_and_raise("battery_soc", 80.0, "battery:1")
    assert alert is None
