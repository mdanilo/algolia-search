from flask import Flask, jsonify, request
from algoliasearch.search_client import SearchClient

app = Flask(__name__)

# client = SearchClient.create("SIZMAGZTIC", "4bb7bc325b929f19973cc2436a860f96")
# index = client.init_index('products_index')

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
