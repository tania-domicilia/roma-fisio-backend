from sqlalchemy import Column, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.core.database import Base

class PianoTerapeutico(Base):
    __tablename__ = "piani"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    paziente_id = Column(UUID(as_uuid=True), ForeignKey("pazienti.id"), nullable=False)
    fisioterapista_id = Column(UUID(as_uuid=True), ForeignKey("fisioterapisti.id"), nullable=False)
    data_inizio = Column(Date, nullable=False)
    data_fine = Column(Date, nullable=False)
    note = Column(Base.metadata.schema.get("String", lambda: None)(), nullable=True)
