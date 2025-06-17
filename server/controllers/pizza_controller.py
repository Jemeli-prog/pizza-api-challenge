from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = []
    for pizza in pizzas:
        pizza_list.append({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })
    return jsonify(pizza_list)
