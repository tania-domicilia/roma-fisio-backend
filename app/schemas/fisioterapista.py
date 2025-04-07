from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class FisioterapistaBase(BaseModel):
    nominativo: str
    telefono: str
    distretti: str
    zone_coperte: str
    note: Optional[str] = None
    zone_preferite: Optional[str] = None

class FisioterapistaCreate(FisioterapistaBase):
    pass

class FisioterapistaUpdate(FisioterapistaBase):
    pass

class FisioterapistaOut(FisioterapistaBase):
    id: UUID

    class Config:
        orm_mode = True

class GeoZoneUpdate(BaseModel):
    geo_zones: str
