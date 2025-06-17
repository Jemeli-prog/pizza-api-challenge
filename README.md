#  Pizza Restaurant API

This is a RESTful API for a Pizza Restaurant built with Flask, following the Model-View-Controller (MVC) pattern.

## Setup Instructions

Follow these steps to set up and run the API locally.

### 1. Create a Virtual Environment and Install Packages

Navigate to the project root directory and run:

```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

### 2. Run Database Setup Commands

Ensure you are in the `pipenv shell` and then run the following commands to initialize, migrate, and upgrade your database:

```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 3. Seed the Database

To populate your database with sample data, run the seed script:

```bash
python server/seed.py
```

### 4. Run the Flask Application

```bash
python server/app.py
```

The API will be running on `http://127.0.0.1:5555`.

##  Project Structure

The project follows an MVC pattern:

```
.
├── server/
│   ├── __init__.py
│   ├── app.py                # App setup and blueprint registration
│   ├── config.py             # DB config, Flask app instance, SQLAlchemy, Migrate
│   ├── models/               # 💾 Models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/          # 🎯 Route handlers (Controllers)
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   ├── seed.py               # Seed data script
├── migrations/               # Database migration scripts
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

## 🧩 Models

### Restaurant
-   `id`: Primary Key
-   `name`: String (max 50 chars, unique, not nullable)
-   `address`: String (max 100 chars, not nullable)
-   **Relationships**: Has many `RestaurantPizzas` (cascading delete)

### Pizza
-   `id`: Primary Key
-   `name`: String (max 50 chars, not nullable)
-   `ingredients`: String (max 200 chars, not nullable)
-   **Relationships**: Has many `RestaurantPizzas`

### RestaurantPizza (Join Table)
-   `id`: Primary Key
-   `price`: Integer (validation: must be between 1 and 30, not nullable)
-   `restaurant_id`: Foreign Key to `restaurants.id`
-   `pizza_id`: Foreign Key to `pizzas.id`
-   **Relationships**: Belongs to `Restaurant` and `Pizza`

## 🛠 API Routes

All routes return JSON responses.

### 1. GET /restaurants

Returns a list of all restaurants.

**Example Request:**

```
GET http://127.0.0.1:5555/restaurants
```

**Example Success Response:**

```json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Mama Mia's",
    "address": "456 Oak Ave"
  }
]
```

### 2. GET /restaurants/<int:id>

Returns details of a single restaurant and its associated pizzas.

**Example Request:**

```
GET http://127.0.0.1:5555/restaurants/1
```

**Example Success Response:**

```json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Mozzarella, Pepperoni"
    }
  ]
}
```

**Example Error Response (404 Not Found):**

```json
{
  "error": "Restaurant not found"
}
```

### 3. DELETE /restaurants/<int:id>

Deletes a restaurant and all related `RestaurantPizzas` due to cascading deletes.

**Example Request:**

```
DELETE http://127.0.0.1:5555/restaurants/1
```

**Example Success Response (204 No Content):**

(No content in response body)

**Example Error Response (404 Not Found):**

```json
{
  "error": "Restaurant not found"
}
```

### 4. GET /pizzas

Returns a list of all pizzas.

**Example Request:**

```
GET http://127.0.0.1:5555/pizzas
```

**Example Success Response:**

```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Dough, Tomato Sauce, Mozzarella, Basil"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Mozzarella, Pepperoni"
  }
]
```

### 5. POST /restaurant_pizzas

Creates a new `RestaurantPizza` entry.

**Example Request:**

```
POST http://127.0.0.1:5555/restaurant_pizzas
Content-Type: application/json

{
  "price": 5,
  "pizza_id": 4,
  "restaurant_id": 3
}
```

**Example Success Response (201 Created):**

```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 4,
  "restaurant_id": 3,
  "pizza": {
    "id": 4,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "789 Pine Ln"
  }
}
```

**Example Error Response (400 Bad Request):**

```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## 🔎 Testing with Postman

1.  **Open Postman**
Ensure your Flask API is running (`python server/app.py`)
Run each request in the Postman collection to test the API endpoints
