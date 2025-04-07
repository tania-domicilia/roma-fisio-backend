from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import piano as schema
from app.core.database import get_db
from typing import List
from uuid import UUID

router = APIRouter(prefix="/piani", tags=["piani"])

@router.post("/", response_model=schema.PianoOut)
def crea_piano(data: schema.PianoCreate, db: Session = Depends(get_db)):
    nuovo = models.PianoTerapeutico(**data.dict())
    db.add(nuovo)
    db.commit()
    db.refresh(nuovo)
    return nuovo

@router.get("/", response_model=List[schema.PianoOut])
def lista_piani(db: Session = Depends(get_db)):
    return db.query(models.PianoTerapeutico).all()
