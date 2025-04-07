from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 👇 Aggiungi questa parte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://clinquant-hummingbird-be10bb.netlify.app"],  # o ["*"] per tutti
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Roma Fisio backend attivo!"}
