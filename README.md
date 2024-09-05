# Movie Review and Recommendation API

## Overview

This project is a Django-based API for managing movie reviews and recommendations. It integrates with The Movie Database (TMDb) API to fetch movie data, but allows for manual entry and management of movie details. Users can create, read, update, and delete movie reviews, and the API includes endpoints for movie recommendations based on user reviews.

## Features

- **User Authentication:** Register, log in, log out, and manage user sessions.
- **Movie Management:** Manually add, update, and delete movies.
- **Review Management:** Create, read, update, and delete reviews for movies.
- **Recommendation System:** Get movie recommendations based on user reviews.
- **API Documentation:** Interactive API documentation using Swagger/OpenAPI.

## Prerequisites

- Python 3.8+
- Django 4.x
- Django REST Framework (DRF)
- `scikit-surprise` (for recommendation system)

## Installation
1. **Clone the repository:**

   ```bash
   git clone https://github.com/mandeepdhaka/movie_review_recommendation_project/
   cd movie_review_recommendation_project

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install the required packages:**
    ```bash
   pip install -r requirements.txt
2. **Run database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5.**Start the development server:**
   ```bash
   pthon manage.py runserver


## API Endpoints
User Authentication
Register: POST /api/auth/register/
Login: POST /api/auth/login/
Logout: POST /api/auth/logout/
Movie Management
List Movies: GET /api/movies/
Create Movie: POST /api/movies/
Retrieve Movie: GET /api/movies/<int:pk>/
Update Movie: PUT /api/movies/<int:pk>/ or PATCH /api/movies/<int:pk>/
Delete Movie: DELETE /api/movies/<int:pk>/
Review Management
List Reviews: GET /api/reviews/
Create Review: POST /api/reviews/
Retrieve Review: GET /api/reviews/<int:pk>/
Update Review: PUT /api/reviews/<int:pk>/ or PATCH /api/reviews/<int:pk>/
Delete Review: DELETE /api/reviews/<int:pk>/
Recommendations
Get Recommendations: GET /api/recommendations/ (Requires user authentication)
API Documentation
Interactive Documentation: Swagger UI
Usage
Add Movie Details: Send a POST request to /api/movies/ with the movie details.

Add Reviews: Send a POST request to /api/reviews/ with review details including the movie ID and user ID.

Get Recommendations: Send a GET request to /api/recommendations/ to get movie recommendations based on user reviews.

