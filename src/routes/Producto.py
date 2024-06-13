from flask import Blueprint, jsonify

main=Blueprint('producto_blueprint', __name__)

@main.route('/')
def get_movies():
    return jsonify({'message': "GESCAS"})