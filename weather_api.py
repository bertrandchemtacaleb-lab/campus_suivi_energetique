"""Connecteur vers l'API météo externe (irradiation, température, vent)."""
import requests
from config.settings import settings


def fetch_current_weather(lat: float, lon: float) -> dict:
    """Interroge l'API météo configurée et retourne les données brutes.
    À adapter selon le fournisseur choisi (OpenWeatherMap, etc.)."""
    if not settings.weather_api_key:
        raise RuntimeError("WEATHER_API_KEY non configurée dans .env")

    response = requests.get(
        f"{settings.weather_api_url}/weather",
        params={"lat": lat, "lon": lon, "appid": settings.weather_api_key, "units": "metric"},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
