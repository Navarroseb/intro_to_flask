import os
import json
from flask import Flask, jsonify, request 
from dotenv import load_dotenv 

##cargar variables de entorno
load_dotenv()

app = Flask(__name__)
## configuración

app.config['DEBUG'] = True
app.config['ENV'] = "development"

##code here

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    saludo = {
        "mesaje": "Hola desde mi primera API con Flask"
    }
    return jsonify(saludo)

@app.route('/<name>/<int:age>', methods=['GET'])
def saludo(name, age):
    mensaje= {
        "msg": f"Hola, soy {name} y tengo {age} años"
    }    
    
app.route('/api/search/<category><type>', methods=['POST', 'PUT'])
def search_post_put(category):

    params = request.args

    print(params)
    print(request.data)

    datos_en_json = request.get_jason()

    return jsonify({ 
                    "msg": "buscando",
                    "category": category,
                    "params": params,
                    "method": request.method,
                    "datos": datos_en_json
    })    


## fin code
if __name__ == '__main__':
    app.run()