from sqlalchemy import Column, String, Integer
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class Utente(Base):
    __tablename__ = "utenti"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    ruolo = Column(String, nullable=False)
