from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

# Importações internas do nosso projeto
from . import models, schemas
from .database import engine, get_db

# Cria as tabelas no banco de dados automaticamente na inicialização (Ideal para este primeiro momento)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Orientta Hunter AI",
    description="SaaS de Inteligência Comercial e ATS para Job Hunters",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "system": "Orientta Hunter AI Core Engine"}

# --- ROTAS DE CLIENTES ---

@app.post("/clientes/", response_model=schemas.ClienteResponse)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    # Converte os dados validados do Pydantic para o modelo do SQLAlchemy
    db_cliente = models.Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.get("/clientes/", response_model=List[schemas.ClienteResponse])
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    return clientes
