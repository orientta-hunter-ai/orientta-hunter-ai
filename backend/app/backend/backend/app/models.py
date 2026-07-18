from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cargo_objetivo = Column(String(255), nullable=False)
    cidade = Column(String(100))
    modalidade = Column(String(50)) # Presencial, Remoto, Híbrido
    linkedin = Column(String(255))
    email = Column(String(255))
    telefone = Column(String(50))
    pretensao_salarial = Column(String(100))
    palavras_chave = Column(Text) # Separadas por vírgula
    ativo = Column(Boolean, default=True)
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    vagas = relationship("Vaga", back_populates="cliente")

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False, unique=True)
    segmento = Column(String(100))
    cidade = Column(String(100))
    linkedin = Column(String(255))
    site = Column(String(255))
    
    # Inteligência Comercial: métricas calculadas automaticamente
    score_resposta = Column(Float, default=0.0) 
    
    # Relacionamentos
    vagas = relationship("Vaga", back_populates="empresa")
    conexoes = relationship("Conexao", back_populates="empresa")

class Vaga(Base):
    __tablename__ = "vagas"

    id = Column(Integer, primary_key=True, index=True)
    cargo = Column(String(255), nullable=False)
    url = Column(String(500), unique=True, nullable=False)
    cidade = Column(String(100))
    modelo = Column(String(50))
    status = Column(String(50), default="Nova") # Nova, Contatada, Entrevista, Encerrada
    job_hunter_score = Column(Float, default=0.0) # Nota calculada pela IA
    data_publicacao = Column(DateTime(timezone=True))
    data_descoberta = Column(DateTime(timezone=True), server_default=func.now())

    # Chaves Estrangeiras
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    # Relacionamentos
    empresa = relationship("Empresa", back_populates="vagas")
    cliente = relationship("Cliente", back_populates="vagas")

class Conexao(Base):
    __tablename__ = "conexoes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    cargo = Column(String(100)) # Ex: Talent Acquisition, Tech Recruiter
    linkedin = Column(String(255))
    email = Column(String(255))
    
    empresa_id = Column(Integer, ForeignKey("empresas.id"))
    empresa = relationship("Empresa", back_populates="conexoes")

class KnowledgeBase(Base):
    """
    Memória da IA: Armazena o histórico e aprendizado contínuo das interações.
    """
    __tablename__ = "knowledge_base"

    id = Column(Integer, primary_key=True, index=True)
    entidade_tipo = Column(String(50)) # 'Empresa', 'Conexao', 'Vaga'
    entidade_id = Column(Integer)
    insight = Column(Text, nullable=False) # Ex: "O recrutador João prefere contato de manhã."
    data_registro = Column(DateTime(timezone=True), server_default=func.now())
