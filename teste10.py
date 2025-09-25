from flask import Flask, jsonify, request

app = Flask(__name__)

#simular banco de dados 
usuarios = [
    {"id":1,"nome":"Ana"},
    {"id":2,"nome":"Joana"}
]

@app.route("/")
def home():
    return "<h1>Backend com o Flask</h1>"

#GET usuarios/ - lista todos 
@app.route("/usuarios", methods=["GET"])
def listar_uruarios():
    return jsonify(usuarios)

#GET usuarios/id - busca o usuario pelo ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar_usuario(id):
    usuario = next((u for u in usuarios if u["id"] == id), None)
    
    if usuario:
        return jsonify(usuario) #retorna usuario encontrado 
    
    return jsonify({"erro": "usuario não encontrado" }), 404 

#POST cadastra usuario
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()

    novo = {
        "id":len(usuarios) + 1,
        "nome": dados.get("nome")
    }

    usuarios.append(novo)
    return jsonify(novo), 201


#inicia o server
if __name__ == "__main__":
    app.run(debug=True, port=8000)