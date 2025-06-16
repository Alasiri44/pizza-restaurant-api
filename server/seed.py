import sys
import os

sys.path.append("/home/austin/Moringa/phase4/pizza-restaurant-api")

from server import create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.models import db

from faker import Faker
import random
from random import choice

fake = Faker()
app = create_app()
restaurant_names = [
    "Ember & Ivory",
    "The Gilded Fork",
    "Sable & Silk",
    "Haute Horizon",
    "The Velvet Table",
    "Maison Lumière",
    "Celeste Fine Cuisine",
    "Royale Blossom",
    "Echanson",
    "Opulent Harvest",
    "Golden Elm",
    "Atelier du Flavour",
    "Château Noire",
    "Starlight Supper Club",
    "Aurelian Bistro",
    "Elysian Plate",
    "The Carriage Room",
    "Baroque Banquet",
    "Obsidian & Pearl",
    "Amour et Vin",
    "The Ivory Candle",
    "Savoir Vivre Kitchen",
    "Esquire's Table",
    "Azure Tides",
    "The Scarlet Truffle",
    "Monarch’s Feast",
    "Serenade Supperhouse",
    "Vista Royale",
    "Velvet Fig",
    "Opus Culinary"
]


with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()
    
    
    restaurants = []
    for n in range(len(restaurant_names)):
        restaurant = Restaurant(name=choice(restaurant_names), address=fake.address())
        restaurants.append(restaurant)
    db.session.add_all(restaurants)
    
    # Seed Pizzas
    pizzas = [
        {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
        {"name": "Pepperoni", "ingredients": "Pepperoni, Cheese, Tomato Sauce"},
        {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Chicken, Onions"},
        {"name": "Hawaiian", "ingredients": "Pineapple, Ham, Cheese"},
        {"name": "Veggie", "ingredients": "Bell Peppers, Mushrooms, Olives"},
    ]
    pizza_objs = []
    for p in pizzas:
        pizza = Pizza(name=p["name"], ingredients=p["ingredients"])
        db.session.add(pizza)
        pizza_objs.append(pizza)
    
    db.session.commit()
        
    # Seed RestaurantPizzas
    for _ in range(20):
        rp = RestaurantPizza(
            price=random.uniform(5, 25),
            pizza_id=random.choice(pizza_objs).id,
            restaurant_id=random.choice(restaurants).id
        )
        db.session.add(rp)
    
    db.session.commit()