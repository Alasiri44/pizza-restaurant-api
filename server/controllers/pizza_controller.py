from flask import Blueprint, jsonify, make_response
from models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas')
def pizzas():
    pizzas = Pizza.query.all()
    response_body = []
    for pizza in pizzas:
        body = pizza.to_dict()
        response_body.append(body)
    return make_response(response_body, 200)
