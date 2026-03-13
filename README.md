# Pizza Delivery API

A Django REST API for a pizza delivery service with user authentication, order management, and delivery tracking.

## Overview

A RESTful API for managing pizza orders including user registration, menu browsing, order placement with size selection, and order status tracking.

## Features

- **User Authentication** — Registration and login
- **Order Management** — Place orders with size and quantity
- **Order Status** — Track orders (Pending → In Transit → Delivered)
- **Pizza Sizes** — Small, Medium, Large, Extra Large options
- **Heroku Ready** — Configured for Heroku deployment

## Tech Stack

- **Python** 3.x
- **Django** + **Django REST Framework**
- **Pipenv** — Dependency management
- **SQLite** — Database

## Getting Started

```bash
git clone https://github.com/okekefrancis112/pizza-delivery-api.git
cd pizza-delivery-api
pipenv install
pipenv shell
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | User login |
| GET | `/orders/` | List all orders |
| POST | `/orders/` | Place a new order |
| GET | `/orders/<id>/` | Get order details |
| PUT | `/orders/<id>/` | Update order status |

## License

MIT
