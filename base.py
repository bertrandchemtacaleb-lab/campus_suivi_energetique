"""
Déclaration de la base ORM SQLAlchemy commune à tous les modèles.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Classe de base pour tous les modèles SQLAlchemy du projet."""
    pass
