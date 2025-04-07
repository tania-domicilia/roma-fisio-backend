from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import fisioterapista as schema
from app.core.database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/fisioterapisti", tags=["fisioterapisti"])

@router.post("/", response_model=schema.FisioterapistaOut)
def create_fisioterapista(data: schema.FisioterapistaCreate, db: Session = Depends(get_db)):
    nuovo = models.Fisioterapista(**data.dict())
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.get("/", response_model=List[schema.FisioterapistaOut])
def list_fisioterapisti(db: Session = Depends(get_db)):
    return db.query(models.Fisioterapista).all()

@router.get("/{fisioterapista_id}", response_model=schema.FisioterapistaOut)
def get_fisioterapista(fisioterapista_id: UUID, db: Session = Depends(get_db)):
    fisio = db.query(models.Fisioterapista).filter(models.Fisioterapista.id == fisioterapista_id).first()
    if not fisio:
        raise HTTPException(status_code=404, detail="Fisioterapista non trovato")
    return fisio

@router.put("/{fisioterapista_id}", response_model=schema.FisioterapistaOut)
def update_fisioterapista(fisioterapista_id: UUID, data: schema.FisioterapistaUpdate, db: Session = Depends(get_db)):
    fisio = db.query(models.Fisioterapista).filter(models.Fisioterapista.id == fisioterapista_id).first()
    if not fisio:
        raise HTTPException(status_code=404, detail="Fisioterapista non trovato")
    for field, value in data.dict().items():
        setattr(fisio, field, value)
    db.commit()
    db.refresh(fisio)
    return fisio

@router.delete("/{fisioterapista_id}")
def delete_fisioterapista(fisioterapista_id: UUID, db: Session = Depends(get_db)):
    fisio = db.query(models.Fisioterapista).filter(models.Fisioterapista.id == fisioterapista_id).first()
    if not fisio:
        raise HTTPException(status_code=404, detail="Fisioterapista non trovato")
    db.delete(fisio)
    db.commit()
    return {"detail": "Fisioterapista eliminato"}

@router.put("/{fisioterapista_id}/zone", response_model=schema.FisioterapistaOut)
def update_geo_zones(fisioterapista_id: UUID, data: schema.GeoZoneUpdate, db: Session = Depends(get_db)):
    fisio = db.query(models.Fisioterapista).filter(models.Fisioterapista.id == fisioterapista_id).first()
    if not fisio:
        raise HTTPException(status_code=404, detail="Fisioterapista non trovato")
    fisio.geo_zones = data.geo_zones
    db.commit()
    db.refresh(fisio)
    return fisio
