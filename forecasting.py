"""
Prévision de production et de consommation.

Modèle de départ volontairement simple (régression) — cohérent avec un
historique de données encore limité en début de projet. À faire évoluer
vers des modèles plus riches (forêts aléatoires, séries temporelles,
LSTM/TensorFlow) à mesure que l'historique s'étoffe.
"""
import numpy as np
from sklearn.linear_model import LinearRegression


class ProductionForecaster:
    def __init__(self):
        self.model = LinearRegression()
        self._trained = False

    def train(self, irradiation: np.ndarray, temperature: np.ndarray, production_kwh: np.ndarray) -> None:
        X = np.column_stack([irradiation, temperature])
        self.model.fit(X, production_kwh)
        self._trained = True

    def predict(self, irradiation: float, temperature: float) -> float:
        if not self._trained:
            raise RuntimeError("Le modèle doit être entraîné avant utilisation (train()).")
        return float(self.model.predict([[irradiation, temperature]])[0])


class ConsumptionForecaster:
    """Même principe que ProductionForecaster, à entraîner sur l'historique
    de consommation par bâtiment (features : heure, jour de semaine, saison,
    température extérieure...)."""
    def __init__(self):
        self.model = LinearRegression()
        self._trained = False

    def train(self, features: np.ndarray, consumption_kwh: np.ndarray) -> None:
        self.model.fit(features, consumption_kwh)
        self._trained = True

    def predict(self, features: np.ndarray) -> float:
        if not self._trained:
            raise RuntimeError("Le modèle doit être entraîné avant utilisation (train()).")
        return float(self.model.predict([features])[0])
