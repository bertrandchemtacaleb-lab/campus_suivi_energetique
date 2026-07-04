"""
Connecteur MQTT — à implémenter en Phase 6 (intégration temps réel).

Doit exposer une classe `MqttDataSource(EnergyDataSource)` qui s'abonne
aux topics des capteurs (ex: "scip/campus/+/production") et met à jour
un cache interne consulté par les méthodes de l'interface.
"""
from config.settings import settings

BROKER_HOST = settings.mqtt_broker_host
BROKER_PORT = settings.mqtt_broker_port
TOPIC_PREFIX = settings.mqtt_topic_prefix

# TODO Phase 6 : implémenter la connexion paho-mqtt, les callbacks on_connect/
# on_message, et la classe MqttDataSource(EnergyDataSource).
