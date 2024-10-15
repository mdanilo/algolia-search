from fastapi import FastAPI
from algoliasearch.search_client import SearchClient

app = FastAPI()

client = SearchClient.create("SIZMAGZTIC", "4bb7bc325b929f19973cc2436a860f96")

index = client.init_index('products_index')

@app.get("/search/{name}")
def get_products(name: str):
    results = index.search(name)

    products = results["hits"]

    return products
