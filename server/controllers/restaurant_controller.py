from flask import Blueprint, jsonify, make_response
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants')
def restaurants():
    restaurants = Restaurant.query.all()
    response_body = []
    for restaurant in restaurants:
        body = restaurant.to_dict()
        response_body.append(body)
    return make_response(response_body, 200)

@restaurant_bp.route('/restaurants/<int:id>')
def restaurants_by_id(id):
    restaurants = Restaurant.query.filter(Restaurant.id == id).first()
    response_body = restaurants.to_dict()
    return response_body
