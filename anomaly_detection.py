"""Détection d'anomalies sur les relevés énergétiques et l'état des équipements."""
import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self, contamination: float = 0.05):
        self.model = IsolationForest(contamination=contamination, random_state=42)
        self._trained = False

    def train(self, readings: np.ndarray) -> None:
        """`readings` : matrice (n_samples, n_features), ex. [production, temp, irradiation]."""
        self.model.fit(readings)
        self._trained = True

    def is_anomalous(self, reading: np.ndarray) -> bool:
        if not self._trained:
            raise RuntimeError("Le modèle doit être entraîné avant utilisation (train()).")
        prediction = self.model.predict([reading])  # -1 = anomalie, 1 = normal
        return bool(prediction[0] == -1)
