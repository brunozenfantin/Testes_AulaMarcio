#Exemplo Usando Query para ordenar e limitar a resposta

import requests

parametros = {
    "_sort": "title", #ordenar pelo coluna id
    "_order": "desc", #asc-ordenar em ordem crescente, desc ordenar ordem decrescente
    "_limit": 10 #limitandoesta limitando a resposta em 10 post
}
#Executa a requisição e guarda o resultado na variável "response"
response = requests.get("https://jsonplaceholder.typicode.com/posts",
                        params=parametros)

posts = response.json() #Desempacota a resposta no formato JSON

print("Os três resultados encontrados são:\n\n")
print(" Usuário |   ID  |  Título\n")
for post in posts:
    print(" | ",post["userId"],"  |  ",post["id"]," | ",post["title"])