import requests

#função para mostrar todos os posts recebidos
def mostra_posts(posts):
    #forma de usar o laço for (inblock)
    for post in posts:
        print("o titulo do site é: \n\n", post["userId"], " - " ,post["id"], post["title"], "\n\n" )
    
    #forma de usar o alço for (inline)
    [print("o titulo do site é:", post["id"]) for post in posts]

#exemplo com path param [REST] [API ]

# /Post é a tabela [Rota que direciona para listar os Posts]

response = requests.get("https://jsonplaceholder.typicode.com/posts")

#posts = response.json()

#chama a função de forma aninhada
mostra_posts(response.json())
