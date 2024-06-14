from flask import Blueprint, jsonify

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
    

@main.route('/<id>')
def get_product(id):
    try:
        product=ProductModel.get_product(id)
        if product != None:
            return jsonify(product)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}),500