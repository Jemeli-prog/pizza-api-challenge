from server.config import db
from sqlalchemy.orm import validates

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    # Validations
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        if len(name) > 50:
            raise ValueError("Name must be 50 characters or less")
        return name

    @validates('address')
    def validate_address(self, key, address):
        if not address:
            raise ValueError("Address cannot be empty")
        if len(address) > 100:
            raise ValueError("Address must be 100 characters or less")
        return address

    def __repr__(self):
        return f'<Restaurant {self.name}>'
