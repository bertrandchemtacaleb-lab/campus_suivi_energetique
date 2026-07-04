"""Modèles : utilisateurs, rôles et permissions."""
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)   # admin, technicien, lecteur...
    permissions: Mapped[str] = mapped_column(String(500), nullable=True)  # liste sérialisée


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=True)
    role: Mapped["Role"] = relationship()
