"""Service métier : indicateurs financiers (ROI, amortissement, coûts)."""


class FinanceService:
    @staticmethod
    def compute_roi(total_savings: float, total_investment: float) -> float:
        """Retour sur investissement, en pourcentage."""
        if total_investment <= 0:
            return 0.0
        return round((total_savings / total_investment) * 100, 2)

    @staticmethod
    def compute_payback_period(total_investment: float, annual_savings: float) -> float:
        """Durée d'amortissement, en années."""
        if annual_savings <= 0:
            return float("inf")
        return round(total_investment / annual_savings, 2)

    @staticmethod
    def compute_kwh_cost(total_cost: float, total_kwh_produced: float) -> float:
        """Coût actualisé du kWh produit par l'installation."""
        if total_kwh_produced <= 0:
            return 0.0
        return round(total_cost / total_kwh_produced, 4)

    @staticmethod
    def compute_co2_avoided(kwh_produced: float, grid_emission_factor_kg_per_kwh: float = 0.4) -> float:
        """CO2 évité (kg), en comparant à un facteur d'émission réseau de référence."""
        return round(kwh_produced * grid_emission_factor_kg_per_kwh, 2)
