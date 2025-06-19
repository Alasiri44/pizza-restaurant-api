from flask import Blueprint, jsonify, make_response, request
from models.restaurant import Restaurant
from models.__init__ import db

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants')
def restaurants():
    restaurants = Restaurant.query.all()
    
    if restaurants:
        response_body = [restaurant.to_dict() for restaurant in restaurants]
        status_code = 200
    else:
        response_body = { "error": "Restaurants not found" }
        status_code = 404
    return make_response(response_body, status_code)

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def restaurants_by_id(id):    
    restaurant = Restaurant.query.filter(Restaurant.id == id).first()
    if request.method == 'GET':

        if restaurant:
            response_body = restaurant.to_dict()
            status_code = 200
        else:
            response_body = { "error": "Restaurant not found" }
            status_code = 404
        return make_response(response_body, status_code)
    
    elif request.method == 'DELETE':
        if restaurant:
            # Reattach the object to the current session before deleting
            restaurant = db.session.merge(restaurant)
            db.session.delete(restaurant)
            db.session.commit()
            
            response_body = {'message': 'The content is deleted successfully'}
            status_code = 204
        else:
            response_body = {'error': 'Restaurant not found'}
            status_code = 404
            
        return make_response(response_body, status_code)