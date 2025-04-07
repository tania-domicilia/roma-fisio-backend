from sqlalchemy import Column, String, Date
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.core.database import Base

class Paziente(Base):
    __tablename__ = "pazienti"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    indirizzo = Column(String, nullable=False)
    citta = Column(String, nullable=False)
    cap = Column(String, nullable=False)
    data_inizio_piano = Column(Date, nullable=False)
    data_fine_piano = Column(Date, nullable=False)
    note = Column(String)
