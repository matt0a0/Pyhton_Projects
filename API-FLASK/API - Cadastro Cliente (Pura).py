#API CRUD (Criar,Ler,Atualizar -> Ativar(Desbloquear/Bloquear) e Deletar)
from flask import Flask,jsonify,request,Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash,check_password_hash
from bson import json_util
from bson.objectid import ObjectId

#$Instância do Flask 
app = Flask(__name__)

#Conexão com o DB
app.config['MONGO_URI'] = 'mongodb://localhost/pymongo_teste'
mongo = PyMongo(app)

#Rotas da API - Regra de Negócio

#Criar - POST
@app.route("/users",methods=['POST']) #cOLOCA OS DADOS NO DB
def create_user():
    #Recebe os dados
    nome = request.json['nome']
    senha = request.json['senha']
    email = request.json['email']

    if nome and senha and email:
        hashed_password = generate_password_hash(senha)
        id = mongo.db.users.insert_one(
            {'nome' : nome, 'senha' : hashed_password, 'email' : email}
        )
        resposta_cliente = {
            'id' : str(id),
            'nome' : nome,
            'senha' : hashed_password,
            'email' : email
        }
        return resposta_cliente
    else:
        return not_found()
#Buscar - GET
@app.route('/users',methods=['GET']) #Busca os dados no DB
def buscar_usuarios():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response,mimetype="appllication/json")

#Buscar Apenas Um user
@app.route('/users/<id>', methods=['GET'])
def buscar_usuario(id):
    user = mongo.db.users.find_one({'_id' : ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response,mimetype="appllication/json")

#Deletar Usuário
@app.route('/users/<id>',methods=['DELETE'])
def deletar_usuario(id):
    mongo.db.users.delete_one({"_id" : ObjectId(id)})
    response = jsonify({'mensagem' : "O usuário " + id + " foi deletado com Sucesso"})
    return response

#Atualizar Usuário----------
@app.route('/users/<id>',methods=['PUT'])
def atualizar_usuário(id):
    #Assim como em criar usuário preciso instanciar as variáveis
    nome = request.json['nome']
    senha = request.json['senha']
    email = request.json['email']

    #Regra de criação
    if nome and senha and email:
        alt_hashed_password = generate_password_hash(senha)
        mongo.db.users.update_one({"_id" : ObjectId(id)}, {'$set' : { 'nome' : nome, 'senha' : alt_hashed_password, 'email' : email}})
        response = jsonify({'mensagem' : "O usuário com o id:" + id + "foi atualizado com sucesso"})
        return response
    
#Caso acesse uma rota que não existe - Erro
@app.errorhandler(404)
def not_found(error=None):
    resposta = jsonify({'mensagem' : 'Recurso Não Encontrado :' + request.url, 'status' : 404})
    resposta.status_code = 404
    return resposta



if __name__ == "__main__":
    app.run(debug=True)