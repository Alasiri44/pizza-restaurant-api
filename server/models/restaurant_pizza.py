from models.__init__  import db, SerializerMixin

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.ForeignKey('pizzas.id'))
    
    restaurant = db.relationship('Restaurant', back_populates= 'restaurant_pizzas' )
    pizza = db.relationship('Pizza', back_populates= 'restaurant_pizzas')
    
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizzas.restaurant_pizzas', )
    
    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, price):
        if price < 30 or price > 1:
            self.price = price
        else:
            print('Must be an integer between 1 and 30')
            
    def __repr__(self):
        return f'<Restaurant_Pizza {self.id}, {self.price} >'