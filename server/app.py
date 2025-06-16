from server import create_app
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from flask import make_response
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp

app = create_app()
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)

@app.route('/')
def index():
    return f'<h1>Welcome to my header right now</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)