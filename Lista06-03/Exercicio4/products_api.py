from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_products():
    with open('products_data.json', 'r') as file:
        return json.load(file)

def save_products(products):
    with open('products_data.json', 'w') as file:
        json.dump(products, file)

@app.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    products = load_products()
    products.append(data)
    save_products(products)
    return jsonify({'message': 'Produto adicionado com sucesso'})

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    products = load_products()
    products[product_id] = data
    save_products(products)
    return jsonify({'message': 'Produto atualizado com sucesso'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products()
    del products[product_id]
    save_products(products)
    return jsonify({'message': 'Produto excluído com sucesso'})

if __name__ == '__main__':
    app.run(debug=True)
