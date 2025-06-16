from flask import Flask, make_response
from flask_migrate import Migrate
from server.models import db, pizza, restaurant, restaurant_pizza

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False
    app.json.compact = False
    
    migrate = Migrate(app, db)
    db.init_app(app)
    
    return app