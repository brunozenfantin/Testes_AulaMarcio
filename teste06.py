#Exemplo para atualizar um Post
import requests

dados = {
    "title": "Titulo atualizado",
    "body": "novo texto atualizado",
    "userId": 1
}

resposta = requests.put("https://jsonplaceholder.typicode.com/posts/1",
                        json=dados)

post_atualizado = resposta.json()

print("O Post foi atualizado com sucesso", post_atualizado)