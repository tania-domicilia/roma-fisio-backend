from pydantic import BaseModel
from uuid import UUID
from datetime import date
from typing import Optional

class PianoBase(BaseModel):
    paziente_id: UUID
    fisioterapista_id: UUID
    data_inizio: date
    data_fine: date
    note: Optional[str] = None

class PianoCreate(PianoBase):
    pass

class PianoOut(PianoBase):
    id: UUID

    class Config:
        orm_mode = True
