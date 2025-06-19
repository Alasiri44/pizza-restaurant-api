# Single-database configuration for Flask.

A simple Flask REST API to manage restaurants, pizzas, and their associations using a many-to-many relationship through `RestaurantPizza`.

## Setup
### 1. Clone the repository

```console
$ git clone <your-repo-url>
$ cd pizza-restaurant-api
```

### 2. Create virtual environment and install dependencies

Using Pipenv:

```console
$ pipenv install
$ pipenv shell
```

Or using venv + pip:

```console
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 3. Set environment variables (optional)

```
$ export PYTHON_PATH=*
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

### 4. Initialize the database

```console
$ flask db init
$ flask db migrate -m "Initial migration"
$ flask db upgrade
```

---

## 🌱 Seed the Database

```console
$ python seed.py
```

Ensure `seed.py` contains sample data for restaurants, pizzas, and restaurant-pizza relationships.

---


## 📁 Folder Structure

```
pizza-restaurant-api/
├── app.py
├── models/
│   ├── __init__.py
│   ├── restaurant.py
│   ├── pizza.py
│   └── restaurant_pizza.py
├── controllers/
│   └── restaurant_controller.py
├── migrations/
├── seed.py
├── requirements.txt
└── README.md
```

---

## 📌 Route Summary

| Method | Route                             | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | /restaurants                      | Get all restaurants                  |
| GET    | /restaurants/<int:id>             | Get a specific restaurant by ID      |
| DELETE | /restaurants/<int:id>             | Delete a restaurant by ID            |
| GET    | /pizzas                           | Get all pizzas                       |
| POST   | /restaurant_pizzas                | Add a pizza to a restaurant          |

---

## 🔁 Example Requests & Responses

### `GET /restaurants`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mama's Pizza",
    "address": "123 Main St",
    "pizzas": [
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "cheese, pepperoni"
      }
    ]
  }
]
```

---

### `GET /restaurants/<id>`

**Response:**
```json
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "cheese, pepperoni"
    }
  ]
}
```

**404 Response:**
```json
{ "error": "Restaurant not found" }
```

---

### `DELETE /restaurants/<id>`

**Response (204):**
```json
{ "message": "Deleted successfully" }
```

**404 Response:**
```json
{ "error": "Restaurant not found" }
```

---

### `POST /restaurant_pizzas`

**Request:**
```json
{
  "price": 15,
  "restaurant_id": 1,
  "pizza_id": 2
}
```

**Success Response:**
```json
{
  "id": 2,
  "name": "Pepperoni",
  "ingredients": "cheese, pepperoni"
}
```

**Validation Error:**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## ✅ Validation Rules

### For `RestaurantPizza`:

- `price` must be between 1 and 30
- `restaurant_id` must refer to an existing restaurant
- `pizza_id` must refer to an existing pizza

---

## 📮 Using Postman

1. Open Postman and set base URL: `http://127.0.0.1:5000`
2. Create the following requests:
   - `GET /restaurants`
   - `GET /restaurants/<id>`
   - `DELETE /restaurants/<id>`
   - `GET /pizzas`
   - `POST /restaurant_pizzas`
3. For POST requests, set header:
   ```
   Content-Type: application/json
   ```
4. Test with valid and invalid data to confirm validation works.

---

## ✅ Submission Checklist

- [x] MVC folder structure is used (`models`, `controllers`)
- [x] Models have relationships and validations
- [x] All required routes are implemented
- [x] Postman tests pass successfully
- [x] This `README.md` is complete and accurate

---

## 💬 Author

Created by Austin Pamba. Feel free to reach out with any questions.