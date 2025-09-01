# 🌍 Ecolog API

Ecolog API is a Django-based backend service designed to manage ecological and environmental data.  
It provides RESTful endpoints for handling users, data collection, and reporting.

---

## 🚀 Features
- User authentication & management (Django `users` app)
- API endpoints for ecological/environmental data
- Database migrations and models for structured storage
- Scalable and easy to extend for research or production

---

Ecolog API Endpoints
This document provides a reference for the key API endpoints available in the project.

1. User Authentication
The following endpoints are powered by the Djoser library and are used for user management.

Register a New User
Used to create a new user account.

URL: http://127.0.0.1/api/users/register

Method: POST

Headers:

Content-Type: application/json

Body (JSON):

JSON

{
    "username": "yourusername",
    "email": "youremail@example.com",
    "password": "yourpassword"
}
Response: 201 Created on success.

# Log In
Used to get an authentication token for a registered user.

URL: api/auth/jwt/create

Method: POST

Headers:

Content-Type: application/json

Body (JSON):

JSON

{
    "email": "youremail@example.com",
    "password": "yourpassword"
}
Response: 200 OK with a token in the body.

Get User Details
Used to retrieve the details of the currently authenticated user.

URL: /api/users/me/

Method: GET

Headers:

Authorization: Token <your_auth_token>

Response: 200 OK with user details in the body.

2. External Data Sources
The following are examples of API calls your backend can make to external services to retrieve data.

Search Wikipedia
This endpoint searches for articles on Wikipedia based on a query.

URL: https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={search_term}

Method: GET

URL Parameter: {search_term} - The word or phrase you want to search for.

Example: ...&srsearch=Geology

Search USGS
This endpoint searches for data and publications from the U.S. Geological Survey.

URL: https://www.sciencebase.gov/catalog/items?q={search_term}&format=json

Method: GET

URL Parameter: {search_term} - The word or phrase you want to search for.

Example: ...q=Volcanoes

## 🛠 Tech Stack
- **Python 3.11+**
- **Django 5+**
- **Django REST Framework**
- **SQLite**
- **Git & GitHub for version control**

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecolog-api.git
   cd ecolog-api
