#Exemplo para enviar parametros no HEADER da Request
import requests

header = {
    "User-Agent": "Meu AppPython/1.0",
    "Content-Type": "application/json"
}

response = requests.get("https://jsonplaceholder.typicode.com/posts/1",
                       headers=header)

post = response.json()
print("Post Encontrado:", post["title"])
print("Status da Response:", response.status_code)