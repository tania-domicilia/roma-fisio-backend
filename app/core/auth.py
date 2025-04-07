from sqlalchemy.orm import Session
from app.models import models
from app.core.database import SessionLocal
from app.core.security import get_password_hash

def create_user_if_not_exists(email: str, password: str, ruolo: str):
    db: Session = SessionLocal()
    existing = db.query(models.Utente).filter(models.Utente.email == email).first()
    if not existing:
        user = models.Utente(
            email=email,
            password_hash=get_password_hash(password),
            ruolo=ruolo
        )
        db.add(user)
        db.commit()
        print(f"Utente admin creato: {email}")
    db.close()
