from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import models
from app.schemas import user as user_schema
from app.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(user: user_schema.LoginInput, db: Session = Depends(get_db)):
    db_user = db.query(models.Utente).filter(models.Utente.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Credenziali non valide")
    token = create_access_token({"sub": db_user.email, "role": db_user.ruolo})
    return {"access_token": token, "token_type": "bearer"}
