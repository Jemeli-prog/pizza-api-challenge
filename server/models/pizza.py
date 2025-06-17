from server.config import db
from sqlalchemy.orm import validates

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    # Relationships
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    # Validations
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        if len(name) > 50:
            raise ValueError("Name must be 50 characters or less")
        return name

    @validates('ingredients')
    def validate_ingredients(self, key, ingredients):
        if not ingredients:
            raise ValueError("Ingredients cannot be empty")
        if len(ingredients) > 200:
            raise ValueError("Ingredients must be 200 characters or less")
        return ingredients

    def __repr__(self):
        return f'<Pizza {self.name}>'
