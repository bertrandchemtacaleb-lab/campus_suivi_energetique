# Architecture technique — SCIP

## Vue d'ensemble

La plateforme est organisée en quatre couches indépendantes :

```
┌───────────────────────────────────────────┐
│  Présentation   : app/ (Streamlit), api/    │
├───────────────────────────────────────────┤
│  Métier         : services/ (+ services/ai) │
├───────────────────────────────────────────┤
│  Intégration    : integration/ (MQTT,       │
│                   Modbus, météo, simulé)    │
├───────────────────────────────────────────┤
│  Données        : models/, database/        │
└───────────────────────────────────────────┘
```

## Règle de dépendance

Les flèches de dépendance ne vont que vers le bas :

- `app/` et `api/` dépendent de `services/`.
- `services/` dépend de `integration/interfaces.py` (jamais d'une
  implémentation concrète comme `mqtt_client.py`).
- `integration/` dépend de `config/` et, pour la persistance, de `models/`.
- `models/` dépend uniquement de `database/base.py`.

Cette règle garantit que basculer `DATA_SOURCE_MODE=simulated` vers
`real` dans `.env` ne nécessite aucune modification de `services/`,
`app/` ni `api/` — seule la factory `get_active_data_source()` dans
`integration/interfaces.py` change de branche.

## Base de données

Voir `docs/data_dictionary.md` pour le détail des tables. Le schéma est
géré par SQLAlchemy (`models/`) et versionné via Alembic
(`database/migrations/`).

## Prochaines étapes (voir rapport de projet)

1. Initialiser Alembic et générer la première migration.
2. Peupler `data/demo/` avec un jeu de données réaliste (voir cahier des
   charges, catégories B/D/F en priorité).
3. Prototyper le rendu 3D du Digital Twin (page `app/pages/2_Digital_Twin.py`).
4. Entraîner les premiers modèles IA sur les données de démonstration.
