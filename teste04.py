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
print("Post cadastrado com Sucesso: \n\n")
print(novo_post["id"])

print(novo_post["title"])