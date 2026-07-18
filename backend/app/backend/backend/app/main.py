from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Orientta Hunter AI",
    description="SaaS de Inteligência Comercial e ATS para Job Hunters",
    version="1.0.0"
)

# Configuração de CORS para permitir requisições do frontend React/Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": "Orientta Hunter AI Core Engine",
        "message": "Sistemas de inteligência prontos para iniciar."
    }

@app.get("/health")
def health_check():
    # Futuramente validaremos conexão com DB e Redis aqui
    return {"status": "healthy"}
