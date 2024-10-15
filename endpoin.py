from flask import Flask, jsonify, request
from algoliasearch.search_client import SearchClient

app = Flask(__name__)

client = SearchClient.create("SIZMAGZTIC", "4bb7bc325b929f19973cc2436a860f96")

index = client.init_index('products_index')

@app.route('/search', methods=['GET'])
def obter_dados():
    nome_produto = request.args.get('nome')

    results = index.search(nome_produto)

    # results = index.search(nome_produto, {
    #     'filters': "brand: COFAP"
    # })

    products = results["hits"]

    print('qtd:', len(products))

    return jsonify(products)

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
