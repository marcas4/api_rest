from flask import Blueprint, jsonify, request

# Entities
from models.entities.Product import Product

# Models
from models.ProductModel import ProductModel

main=Blueprint('product_blueprint', __name__)

@main.route('/')
def get_products():
    try:
        products=ProductModel.get_products()
        return jsonify(products)
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    

@main.route('/<int:id>')
def get_product(id):
    try:
        product=ProductModel.get_product(id)
        if product:
            return jsonify(product)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500
    
@main.route('/add', methods=['POST'])
def add_product():
    try:
        # Se debe validar que los datos lleguen correctamente
        nombre = request.json['nombre']
        valor_unitario = int(request.json['valor_unitario'])
        product=Product(id="",nombre=nombre, valor_unitario=valor_unitario)
        
        affected_rows=ProductModel.add_product(product)

        if affected_rows == 1:
            return jsonify(product.id)
        else:
            return jsonify({'message': "Error on insert"}),500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500


@main.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        # Se debe validar que los datos lleguen correctamente
        nombre = request.json['nombre']
        valor_unitario = int(request.json['valor_unitario'])
        product=Product(id, nombre, valor_unitario)
        
        affected_rows=ProductModel.update_product(id, nombre, valor_unitario)

        if affected_rows == 1:
            return jsonify({'message': "Product updated successfully"})
        else:
            return jsonify({'message': "No product updated"}), 404
        
    except Exception as ex:
        return jsonify({'message': str(ex)}),500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        product=Product(id)
        affected_rows=ProductModel.delete_product(product)

        if affected_rows == 1:
            return jsonify(product.id)
        else:
            return jsonify({'message': "Error no product delete"}), 500
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 404 