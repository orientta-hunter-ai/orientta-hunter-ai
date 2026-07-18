from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- Schemas para Cliente ---

class ClienteBase(BaseModel):
    nome: str
    cargo_objetivo: str
    cidade: Optional[str] = None
    modalidade: Optional[str] = None
    linkedin: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    pretensao_salarial: Optional[str] = None
    palavras_chave: Optional[str] = None
    ativo: Optional[bool] = True

class ClienteCreate(ClienteBase):
    pass # Usado no momento de criar um novo cliente (recebe os dados do Base)

class ClienteResponse(ClienteBase):
    id: int
    data_cadastro: datetime

    class Config:
        from_attributes = True # Permite que o Pydantic leia diretamente dos modelos do SQLAlchemy
