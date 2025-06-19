from __init__ import create_app
from models.pizza import Pizza
from models.restaurant import Restaurant
from models.restaurant_pizza import RestaurantPizza
from flask import make_response
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from models.__init__ import db
from models.__init__ import db
from flask_migrate import Migrate

app = create_app()
    
migrate = Migrate(app, db)
db.init_app(app)
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)


@app.route('/')
def index():
    return f'<h1>Welcome to my header right now</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)