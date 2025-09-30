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
    return{"mensagem": "Bem vindo a API com Fast API Teste 2"}

#GET /usuarios - listar todos
@app.get("/usuarios", response_model=List[Usuario])
def listar_usuarios():
    return usuarios

#GET /usuarios/{id} buscar usuario pelo id ou byID
@app.get("/usuarios/{id}")
def busca_usuario(id: int):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
    return {"ERRO": "Usuario nao encontrado"}

#POST /usuarios cadastrar novos usuarios no dicionario
@app.post("/usuarios", response_model= Usuario)
def cadastrar_usuarios(user: Usuario):
    usuarios.append(user)
    return user