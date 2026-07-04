"""
Interfaces communes d'accès aux données temps réel.

Toute source de données (simulée ou réelle) doit implémenter
`EnergyDataSource`. La couche métier (services/) ne dépend jamais
d'une implémentation concrète, seulement de cette interface — c'est ce
qui permet de basculer simulé → réel sans casser le reste du code.
"""
from abc import ABC, abstractmethod
from datetime import datetime


class EnergyDataSource(ABC):
    """Contrat que doit respecter toute source de données énergétiques."""

    @abstractmethod
    def get_current_production(self) -> float:
        """Retourne la production instantanée du site, en kW."""
        raise NotImplementedError

    @abstractmethod
    def get_current_consumption(self) -> float:
        """Retourne la consommation instantanée du site, en kW."""
        raise NotImplementedError

    @abstractmethod
    def get_battery_status(self, battery_id: int) -> dict:
        """Retourne l'état d'une batterie (SOC, SOH, tension, courant...)."""
        raise NotImplementedError

    @abstractmethod
    def get_inverter_status(self, inverter_id: int) -> dict:
        """Retourne l'état d'un onduleur (puissance, température, alarmes...)."""
        raise NotImplementedError

    @abstractmethod
    def get_weather(self) -> dict:
        """Retourne les conditions météo courantes (irradiation, température...)."""
        raise NotImplementedError


def get_active_data_source() -> EnergyDataSource:
    """Factory : retourne la source de données active selon la configuration."""
    from config.settings import settings

    if settings.data_source_mode == "real":
        # from integration.mqtt_client import MqttDataSource
        # return MqttDataSource()
        raise NotImplementedError("Source réelle non encore implémentée (Phase 6).")

    from integration.simulated.data_generator import SimulatedDataSource
    return SimulatedDataSource()
