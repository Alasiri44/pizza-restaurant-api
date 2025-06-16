from . import db, SerializerMixin

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    restaurant_id = db.Column(db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.ForeignKey('pizzas.id'))
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if price < 30 or price > 1:
            self._price = price
        else:
            print('Must be an integer between 1 and 30')
            
    def __repr__(self):
        return f'<Restaurant_Pizza {self.id}, {self.price} >'