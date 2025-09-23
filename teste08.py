import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9090))
server.listen(1)
print("servidor rodando na porta 9090")
while True:
    #aceita conexao
    client,addr = server.accept()
    print("conexao de:", addr)

    #recebe uma requisição
    request = client.recv(1024).decode()
    print("requisição", request.split('\n')[0])

    #envia um HTTP simples
    response = """HTTP/1.1 200 OK
Content-Type:text/html

<h1>Olá Servidor Python</h1>
<p> Esse é um servidor web teste </p>
"""
    client.send(response.encode())
    client.close()

