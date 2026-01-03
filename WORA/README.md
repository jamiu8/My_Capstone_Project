# Weather-Based Outfit Recommendation App

## Project Description
This project is a **REST API application** that allows users to check the current weather for any city and get **outfit recommendations** based on the temperature and weather conditions. Users can also view their **search history** and previously generated recommendations.

The app uses **Django REST Framework (DRF)** and the **OpenWeatherMap API** to fetch real-time weather data. Users must register and authenticate using JWT tokens to access most endpoints.

---

## List of Apps
1. **users** – Handles user authentication, registration, and profiles.  
2. **weather** – Handles fetching weather data from OpenWeatherMap and storing user search history.  
3. **recommendations** – Generates outfit recommendations based on weather data and keeps recommendation history.  

---

## Endpoints

| Endpoint | Method | Description | Auth Required? |
|----------|--------|------------|----------------|
| `/api/users/register/` | POST | Register a new user | No |
| `/api/users/login/` | POST | Login and get JWT token | No |
| `/api/weather/` | GET | Fetch current weather for a city | Yes |
| `/api/weather/history/` | GET | Retrieve logged-in user’s weather search history | Yes |
| `/api/weather/history/?city=<city>` | GET | Retrieve weather history filtered by city | Yes |
| `/api/recommendation/` | GET | Generate outfit recommendation for a city based on latest weather search | Yes |
| `/api/recommendation/history/` | GET | Retrieve logged-in user’s recommendation history | Yes |

---

## Authentication
Endpoints that require authentication must include the JWT token in the request header:


---

## Example Requests & Responses

### 1. Register a new user
**Request**
'''http
POST /api/users/register/
Content-Type: application/json

{
  "username": "jamiu",
  "email": "jamiu@example.com",
  "password": "strongpassword"
}'''

**Response**
'''{
  "success": true,
  "data": {
    "username": "jamiu",
    "email": "jamiu@example.com"
  },
  "error": null
}'''

### 2. Login
**Request**
POST /api/users/login/
Content-Type: application/json

{
  "username": "jamiu",
  "password": "strongpassword"
}

**Response**
{
  "success": true,
  "data": {
    "access": "<jwt-access-token>",
    "refresh": "<jwt-refresh-token>"
  },
  "error": null
}

### 3. Get Weather

**Request**

GET /api/weather/?city=Lagos
Authorization: Bearer <jwt-access-token>


**Response**

{
  "success": true,
  "data": {
    "id": 1,
    "user": 1,
    "city": "Lagos",
    "temperature": 28.5,
    "weather_description": "clear sky",
    "created_at": "2026-01-03T12:00:00Z"
  },
  "error": null
}

4. Weather History

**Request**

GET /api/weather/history/
Authorization: Bearer <jwt-access-token>


**Response**

{
  "success": true,
  "data": [
    {
      "id": 1,
      "city": "Lagos",
      "temperature": 28.5,
      "weather_description": "clear sky",
      "created_at": "2026-01-03T12:00:00Z"
    }
  ],
  "error": null
}

5. Get Outfit Recommendation

**Request**

GET /api/recommendation/?city=Lagos
Authorization: Bearer <jwt-access-token>


**Response**

{
  "success": true,
  "data": {
    "id": 1,
    "search": 1,
    "outfit_text": "Shirt and jeans recommended.",
    "created_at": "2026-01-03T12:05:00Z"
  },
  "error": null
}

6. Recommendation History

**Request**

GET /api/recommendation/history/
Authorization: Bearer <jwt-access-token>


**Response**

{
  "success": true,
  "data": [
    {
      "id": 1,
      "search": 1,
      "outfit_text": "Shirt and jeans recommended.",
      "created_at": "2026-01-03T12:05:00Z"
    }
  ],
  "error": null
} 