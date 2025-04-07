from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS per frontend Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://clinquant-hummingbird-be10bb.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Roma Fisio backend attivo!"}

@app.post("/auth/login")
def login(email: str = Form(...), password: str = Form(...)):
    if email == "admin@roma-fisio.it" and password == "admin123":
        return {"token": "fake-jwt-token"}
    else:
        raise HTTPException(status_code=401, detail="Credenziali non valide")