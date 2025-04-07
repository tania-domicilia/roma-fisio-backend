from fastapi import FastAPI
from app.models import models
from app.core.database import engine, SessionLocal
from app.core.auth import create_user_if_not_exists
from app.routers import auth, fisioterapista, paziente, piano

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(fisioterapista.router)
app.include_router(paziente.router)
app.include_router(piano.router)

@app.on_event("startup")
def startup_event():
    create_user_if_not_exists(
        email="admin@roma-fisio.it",
        password="admin123",
        ruolo="coordinatrice"
    )
