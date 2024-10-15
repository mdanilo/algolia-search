from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa a extensão Flask-CORS
from algoliasearch.search_client import SearchClient

app = Flask(__name__)
CORS(app)  # Habilita CORS para o aplicativo

client = SearchClient.create("0A7VAU2G2V", "311bee779c8826859bb705b29ab2dab4")
index = client.init_index('algolia')

@app.route("/search/<name>", methods=["GET"])
def obter_dados(name: str):
    # Fazer a pesquisa no índice com o nome fornecido
    results = index.search(name)
    
    # Extrair os produtos dos resultados
    products = results.get("hits", [])

    # Retornar os produtos como JSON
    return jsonify(products)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
