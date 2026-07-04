"""
Maintenance prédictive : estimation du risque de panne d'un équipement
à partir de son historique de fonctionnement (température, cycles, âge...).
"""
import numpy as np
from sklearn.ensemble import RandomForestClassifier


class PredictiveMaintenanceModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self._trained = False

    def train(self, features: np.ndarray, failure_labels: np.ndarray) -> None:
        """`features` : ex. [âge_jours, cycles, température_moyenne, nb_alarmes_30j].
        `failure_labels` : 1 si panne survenue dans la fenêtre de prédiction, sinon 0."""
        self.model.fit(features, failure_labels)
        self._trained = True

    def failure_probability(self, features: np.ndarray) -> float:
        if not self._trained:
            raise RuntimeError("Le modèle doit être entraîné avant utilisation (train()).")
        return float(self.model.predict_proba([features])[0][1])
