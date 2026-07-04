# Dictionnaire de données — SCIP

| Table                      | Modèle                          | Rôle |
|----------------------------|----------------------------------|------|
| buildings                  | models.building.Building         | Bâtiments du campus |
| panels                     | models.panel.Panel               | Panneaux photovoltaïques |
| inverters                  | models.inverter.Inverter         | Onduleurs |
| batteries                  | models.battery.Battery           | Batteries de stockage |
| users / roles              | models.user.User / Role          | Comptes et permissions |
| alerts                     | models.alert.Alert               | Alertes générées automatiquement |
| maintenance_interventions  | models.maintenance.MaintenanceIntervention | Interventions de maintenance |
| technicians                | models.maintenance.Technician    | Techniciens |
| financial_records          | models.finance.FinancialRecord   | Suivi financier mensuel |
| energy_readings            | models.history.EnergyReading     | Relevés bruts horodatés (production/consommation) |

Toutes les granularités d'historique (heure, jour, semaine, mois, année)
sont calculées par agrégation SQL sur `energy_readings`, plutôt que
stockées en dur, pour éviter la duplication et les incohérences.

À compléter au fur et à mesure de la collecte des données réelles
(cahier des charges, catégories A à I).
