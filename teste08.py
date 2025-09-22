import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 8000))
server.listen(1)
print("servidor rodando na porta 8000")
while True:
    response = "<p> Esse é um servidor web teste </p>"
