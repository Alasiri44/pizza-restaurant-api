from . import db, SerializerMixin
# Restaurant Model
class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name} {self.id}>'