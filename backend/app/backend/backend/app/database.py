import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Busca a URL do banco no arquivo .env
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://orientta_admin:orientta_pass@db:5432/orientta_hunter"
)

# Cria o motor de conexão
engine = create_engine(DATABASE_URL)

# Configura a sessão que será usada nas rotas da API
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os nossos modelos de banco de dados
Base = declarative_base()

# Dependência para injetar a sessão do banco nas requisições
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
