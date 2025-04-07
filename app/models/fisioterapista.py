from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.core.database import Base

class Fisioterapista(Base):
    __tablename__ = "fisioterapisti"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    nominativo = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    distretti = Column(String, nullable=False)  # Esempio: "IV, V"
    zone_coperte = Column(String, nullable=False)  # Testo libero
    note = Column(String)

    zone_preferite = Column(String, nullable=True)  # Zone preferite (testo libero)
    geo_zones = Column(String)  # GeoJSON delle zone preferite
