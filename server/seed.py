from server.config import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    print("Deleting existing data...")
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()
    db.session.commit()

    print("Creating restaurants...")
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Mama Mia's", address="456 Oak Ave")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Pine Ln")
    db.session.add_all([r1, r2, r3])
    db.session.commit()

    print("Creating pizzas...")
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie Delight", ingredients="Dough, Tomato Sauce, Mozzarella, Bell Peppers, Onions, Mushrooms")
    p4 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese") # For Postman example
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

    print("Creating restaurant pizzas...")
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=p1)
    rp4 = RestaurantPizza(price=8, restaurant=r2, pizza=p3)
    rp5 = RestaurantPizza(price=5, restaurant=r3, pizza=p4) # For Postman example
    db.session.add_all([rp1, rp2, rp3, rp4, rp5])
    db.session.commit()

    print("Seeding complete!")
