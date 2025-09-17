#Tarea #1 comparación de una api de Flask con Api Laravel usando la api comun fakestoreapi.com

#Importamos ua flask con sus metodos
from flask import Flask, jsonify, request
import requests #para api fakestore

# --------- API FLASK ----------- #

#APP
app = Flask(__name__)

#Metodo get para devolver todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get('https://fakestoreapi.com/products')
    return jsonify(response.json())

#Metodo get para devolver un producto por id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_single_product(product_id):
    response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
    return jsonify(response.json())

#Metodo post para crear un producto
@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    response = requests.post('https://fakestoreapi.com/products', json=data)
    return jsonify(response.json()), 201

#Metodo put para actualizar un producto
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    response = requests.put(f'https://fakestoreapi.com/products/{product_id}', json=data)
    return jsonify(response.json()), 200

#Metodo delete para eliminar un producto
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    response = requests.delete(f'https://fakestoreapi.com/products/{product_id}')
    return jsonify({"message": f"Producto {product_id} eliminado correctamente"}), 200