from flask import Flask
import json
import random
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route("/")
def index():
    return "Hello this is the new version!"

@app.route('/extratos')
def show_descontos():
    extratos = []
    for n in range(10):
        extratos.append(
            {"data": str(random.randint(1, 30)) + '-oct-2023', "valor_lancado": round(random.uniform(0.00, 900.00), 2)})
    extratos_json = {"extratos": extratos}
    return json.dumps(extratos_json)

if __name__ == '__main__':
    app.run()
