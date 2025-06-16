from . import db, SerializerMixin

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    
    def __repr__(self):
        return f'<Pizza {self.id}, {self.name} with {self.ingredients}>'