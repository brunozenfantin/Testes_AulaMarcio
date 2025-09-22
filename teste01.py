import requests
#exemplo com path param 
#equivalente a fazer um comando Select * FORM post where id = 6
# /Post é a tabela [Rota que direciona para listar os Posts]
# /6 é o id da tabela [aponta para o registro 6 da tabela POST]
response = requests.get("https://jsonplaceholder.typicode.com/posts/6")
print(response)

post = response.json()

print("o titulo do site é: \n\n", post["id"],post["title"], "\n\n" )
print("e o texto do post é: \n\n", post["body"])