# Roma Fisio Backend

## Setup

1. Copia `.env.example` in `.env` e personalizza i valori.
2. Avvia con Docker:

```bash
docker-compose up --build
```

## Struttura

- `app/models`: ORM models SQLAlchemy
- `app/routers`: Endpoints API REST
- `app/schemas`: Pydantic models per validazione
- `app/core`: Config, auth, utils
- `app/services`: Business logic

