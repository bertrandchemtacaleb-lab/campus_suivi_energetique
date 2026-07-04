"""
Configuration centralisée de la plateforme SCIP.
Toutes les valeurs sont lues depuis les variables d'environnement (.env).
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Base de données
    database_url: str = "postgresql+psycopg://scip_user:scip_password@localhost:5432/scip_db"

    # Sécurité
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60

    # Météo
    weather_api_key: str = ""
    weather_api_url: str = "https://api.openweathermap.org/data/2.5"

    # MQTT
    mqtt_broker_host: str = "localhost"
    mqtt_broker_port: int = 1883
    mqtt_topic_prefix: str = "scip/campus"

    # Modbus
    modbus_host: str = "localhost"
    modbus_port: int = 502

    # Source de données : "simulated" ou "real"
    data_source_mode: str = "simulated"


settings = Settings()
