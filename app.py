from flask import Flask,request
import json
import random
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route("/")
def index():
    return "Olá, mundo! :D"

#Apresenta extratos de um determinado mês
@app.route('/extratos', methods=['GET'])
def getExtratosAPI():
    extratos = []
    for n in range(30):
        dia = str(n+1)
        if int(dia) < 10:
            dia = '0'+dia
        extratos.append(
            {"data": dia + '-oct-2023', "valor_lancado": round(random.uniform(0.00, 900.00), 2)})
    extratos_json = {"extratos": extratos}
    return json.dumps(extratos_json, indent=6)

pessoas = {"pessoas":[{"nome":"Fulano", "cpf":"000.000.000-00", "email":"fulano@emailficticio.com"},{"nome":"Ciclana", "cpf":"111.111.111-11", "email":"ciclana@emailficticio.com"},{"nome":"Beltrana", "cpf":"222.222.222-22", "email":"beltrana@@emailficticio.com"}]}

#Busca todas as pessoas
@app.route('/pessoas', methods=['GET'])
def getPessoasAPI():
    return json.dumps(pessoas, indent=6)

#Busca pessoas por meio de uma URI com parâmetros
@app.route('/pessoa', methods=['GET'])
def getPessoaAPI():
    return json.dumps(getPessoa(request.args.get('index')), indent=6)

def getPessoa(index):
    return pessoas["pessoas"][int(index)]


if __name__ == '__main__':
    app.run()
