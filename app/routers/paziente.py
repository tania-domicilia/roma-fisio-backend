from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import paziente as schema
from app.core.database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/pazienti", tags=["pazienti"])

@router.post("/", response_model=schema.PazienteOut)
def create_paziente(data: schema.PazienteCreate, db: Session = Depends(get_db)):
    nuovo = models.Paziente(**data.dict())
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.get("/", response_model=List[schema.PazienteOut])
def list_pazienti(db: Session = Depends(get_db)):
    return db.query(models.Paziente).all()

@router.get("/{paziente_id}", response_model=schema.PazienteOut)
def get_paziente(paziente_id: UUID, db: Session = Depends(get_db)):
    paziente = db.query(models.Paziente).filter(models.Paziente.id == paziente_id).first()
    if not paziente:
        raise HTTPException(status_code=404, detail="Paziente non trovato")
    return paziente

@router.put("/{paziente_id}", response_model=schema.PazienteOut)
def update_paziente(paziente_id: UUID, data: schema.PazienteUpdate, db: Session = Depends(get_db)):
    paziente = db.query(models.Paziente).filter(models.Paziente.id == paziente_id).first()
    if not paziente:
        raise HTTPException(status_code=404, detail="Paziente non trovato")
    for field, value in data.dict().items():
        setattr(paziente, field, value)
    db.commit()
    db.refresh(paziente)
    return paziente

@router.delete("/{paziente_id}")
def delete_paziente(paziente_id: UUID, db: Session = Depends(get_db)):
    paziente = db.query(models.Paziente).filter(models.Paziente.id == paziente_id).first()
    if not paziente:
        raise HTTPException(status_code=404, detail="Paziente non trovato")
    db.delete(paziente)
    db.commit()
    return {"detail": "Paziente eliminato"}
