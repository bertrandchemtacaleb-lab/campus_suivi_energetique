# Solar Campus Intelligence Platform (SCIP)

Plateforme logicielle de supervision, d'analyse, de simulation et de gestion
d'une centrale photovoltaïque de campus universitaire — inspirée des
systèmes SCADA, EMS et des jumeaux numériques industriels.

## Structure du projet

```
scip/
├── Home.py          # Point d'entrée Streamlit (racine — obligatoire pour Streamlit Cloud)
├── pages/           # 14 pages Streamlit, préfixées 01_ à 14_
├── components/      # Composants Streamlit réutilisables
├── config/          # Configuration centralisée (env, constantes)
├── database/        # Connexion PostgreSQL, session, migrations Alembic
├── models/          # Modèles SQLAlchemy (couche données)
├── services/        # Logique métier : énergie, finance, alertes, IA, simulation
├── integration/      # Connecteurs externes : MQTT, Modbus, météo, données simulées
├── api/             # API REST (FastAPI)
├── exports/         # Génération de rapports PDF / Excel / CSV
├── data/demo/       # Jeux de données de démonstration
├── tests/           # Tests automatisés
└── docs/            # Documentation technique
```

> **Important** : `Home.py` et `pages/` doivent rester à la racine du projet
> (et non dans un sous-dossier `app/`). Streamlit place le dossier du
> script principal en tête de `sys.path` : s'il était dans `app/`, les
> imports comme `from database.session import ...` échoueraient une fois
> déployés, faute de retrouver les packages situés à la racine.

## Principe d'architecture

Le projet est organisé en couches indépendantes pour permettre de basculer
des données simulées vers des données réelles (capteurs, onduleurs,
automates) **sans modifier la couche métier ni la couche présentation** :

1. **Couche données** (`models/`, `database/`) — schéma PostgreSQL.
2. **Couche métier** (`services/`) — calculs énergétiques, financiers, IA.
   Ne dépend jamais directement d'une source de données physique.
3. **Couche intégration** (`integration/`) — implémente une interface
   commune (`integration/interfaces.py`), que la source soit simulée
   (`integration/simulated/`) ou réelle (MQTT, Modbus, API météo).
4. **Couche présentation** (`app/`, `api/`) — Streamlit et API REST,
   consomment uniquement la couche métier.

## Démarrage rapide

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # renseigner les variables de connexion
# initialiser la base de données
alembic upgrade head
# lancer l'API
uvicorn api.main:app --reload
# lancer le frontend (dans un autre terminal)
streamlit run Home.py
```

## État du projet

Ceci est le squelette initial (Phase 1 du plan de développement) :
arborescence, modèles de données, interfaces de services et pages
Streamlit vides ou minimales, prêts à être complétés module par module.
