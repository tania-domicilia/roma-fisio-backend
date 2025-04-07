from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class PazienteBase(BaseModel):
    nome: str
    cognome: str
    telefono: str
    indirizzo: str
    citta: str
    cap: str
    data_inizio_piano: date
    data_fine_piano: date
    note: Optional[str] = None

class PazienteCreate(PazienteBase):
    pass

class PazienteUpdate(PazienteBase):
    pass

class PazienteOut(PazienteBase):
    id: UUID

    class Config:
        orm_mode = True
