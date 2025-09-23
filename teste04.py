#Cadastrar um novo post
import requests

dados = {
    "title": "Teste Jovem Programador",
    "body": "esse é um teste de request",
    "userId": 1
}

response =requests.post("https://jsonplaceholder.typicode.com/posts",
                        json=dados)

novo_post = response.json()

if response.status_code == 201:
    print("Post cadastrado com Sucesso: \n\n")
    print(novo_post["id"])
    print(novo_post["title"])
else:
    print("ERRO", response.status_code) 