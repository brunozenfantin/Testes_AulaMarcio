#Exemplo para deletar o registro
import requests

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print("Status da Solicitação de delete:", response.status_code)