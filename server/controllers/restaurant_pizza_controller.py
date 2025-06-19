from flask import Blueprint, jsonify, make_response, request
from models.restaurant_pizza import RestaurantPizza
from models.__init__ import db
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['GET', 'POST'])
def restaurant_pizzas():
    if request.method == 'GET':
        restaurant_pizzas = RestaurantPizza.query.all()
        response_body = [restaurant_pizza.to_dict() for restaurant_pizza in restaurant_pizzas]
        return make_response(response_body, 200)
    elif request.method == 'POST':
        if 0 < request.get_json.get('price') < 30:
            new_restaurant_pizza = RestaurantPizza(
                price=request.get_json.get('price'),
                pizza_id=request.get_json.get('pizza_id'),
                restaurant_id=request.get_json.get('restaurant_id')
            )
            db.session.add(new_restaurant_pizza)
            db.session.commit()
        
        if new_restaurant_pizza:
            response_body = new_restaurant_pizza.to_dict()
            status_code = 200
        else:
            response_body = { "errors": ["Price must be between 1 and 30"] }
            status_code = 400