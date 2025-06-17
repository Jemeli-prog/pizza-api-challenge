from flask import Blueprint, jsonify, make_response
from server.config import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

restaurant_bp = Blueprint('restaurant_bp', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = []
    for restaurant in restaurants:
        restaurant_list.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        })
    return jsonify(restaurant_list)

@restaurant_bp.route('/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)

    pizzas_data = []
    for rp in restaurant.restaurant_pizzas:
        pizzas_data.append({
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        })

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas_data
    })

@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return make_response(jsonify({"error": "Restaurant not found"}), 404)

    db.session.delete(restaurant)
    db.session.commit()
    return make_response('', 204)
