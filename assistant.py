"""
Assistant intelligent — interface de questions/réponses sur l'état de la
centrale (ex. "quelle a été la production hier ?", "quel bâtiment consomme
le plus ?").

Version initiale : un routeur de règles simples vers les services métier.
Une évolution vers un LLM (ex. API Claude) pourra être branchée ici sans
changer l'interface `answer()`.
"""
from services.energy_service import EnergyService


class EnergyAssistant:
    def __init__(self, energy_service: EnergyService):
        self.energy_service = energy_service

    def answer(self, question: str) -> str:
        question_lower = question.lower()

        if "production" in question_lower and "instantané" in question_lower:
            snapshot = self.energy_service.get_live_snapshot()
            return f"La production instantanée est de {snapshot['production_kw']} kW."

        if "consommation" in question_lower and "instantané" in question_lower:
            snapshot = self.energy_service.get_live_snapshot()
            return f"La consommation instantanée est de {snapshot['consumption_kw']} kW."

        return (
            "Je ne sais pas encore répondre à cette question. "
            "Ce module est un point de départ à enrichir avec davantage de règles "
            "ou un modèle de langage."
        )
