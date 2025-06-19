from models.__init__  import db, SerializerMixin
# Restaurant Model
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates= 'restaurant', cascade= 'all, delete-orphan',)
    # serialize_rules = ('-restaurant_pizzas.restaurant', )
    serialize_only = ('id', 'name', 'address',)
    
    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name} {self.id}>'