#Cadastrar um novo post
import requests

dados = {
    "nome": "João Pedro"
}

response =requests.post("http://localhost:8000/usuarios",
                        json=dados)

novo_user = response.json()

if response.status_code == 201:
    print("Post cadastrado com Sucesso: \n\n")
    print(novo_user["id"])
    print(novo_user["nome"])
else:
    print("ERRO", response.status_code) 