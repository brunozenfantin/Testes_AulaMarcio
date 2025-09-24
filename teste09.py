# Nivel 2 Servidor com http.server mais simples que soket porem ainda basico
from http.server import HTTPServer, BaseHTTPRequestHandler

class MeuHandler(BaseHTTPRequestHandler): 
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.headers("Content-Type", "text/htlm")
            self.end_headers()
            self.wfile.write(b"<h1>Home</h1><p>Bem Vindo ao Backend Nivel 2</p>")
        elif self.path == "/usuarios":
            self.send_response(200)
            self.headers("Content-Type", "aplication/json")
            self.end_headers()
            self.wfile.write(b'{"usuarios": ["Ana", "Joao", "Carlos"]}')
        else:
            self.send_response(404)
            self.headers("Content-Type","text/html")
            self.end_headers()
            self.wfile.write(b"<h1>404 - pagina nao encontrada</h1>")
        
#inicia o servidor        
server = HTTPServer(("localhost", 9091), MeuHandler)
print("Servidor em http:/localhost:9091")
server.serve_forever()