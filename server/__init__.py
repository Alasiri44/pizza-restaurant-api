from flask import Flask, make_response
from flask_migrate import Migrate
from models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICAIONS'] = False
    migrate = Migrate(app, db)
    db.init_app(app)
    
    return app