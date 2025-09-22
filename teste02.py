#exemplo usando Query params, ou seja, filtragem embutida na URL

import requests

parametro = {
    "userId":2,
    "id": 17
}

response = requests.get("https://jsonplaceholder.typicode.com/posts",
                        params = parametro)

#post = response.json()
posts = response.json()

#print("Título:", post["title"])

#print("Corpo:", post["body"])

#print("ID do usuário:", post["userId"])

print("Posts Encontrados no domínio:\n\n")

for post in posts:
    print(post["userId"],post["id"],post["title"])

#print("e o Texto do POST é: \n\n", post["body"])