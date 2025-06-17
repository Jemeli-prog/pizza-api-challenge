from flask import Flask, jsonify
from .config import app, db, migrate

# Import models to ensure they are registered with SQLAlchemy
from .models import restaurant, pizza, restaurant_pizza

# Import blueprints
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def index():
    return jsonify(message="Welcome to the Pizza Restaurant API!")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
