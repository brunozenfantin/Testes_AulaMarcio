from fastapi import FastAPI
from pydantic import BaseModel
from typing import List 

app = FastAPI(title="Minha Api com FastApi", version="1.0")

class Usuario(BaseModel):
    id: int
    nome: str

#BD simulado(serve para que os @app.get façam a solicitação dos users)
usuarios=[
    Usuario(id=1,nome="Ana"),
    Usuario(id=1,nome="Ana Julia")
    ]

#Rota Principal
@app.get("/")
def home():
    return{"mensagem": "Bem vindo a API com Fast API"}

#GET /usuarios - listar todos
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios