# Recipe App

A simple Recipe API built with Django Rest Framework, designed for managing recipes, tags, and ingredients. This project demonstrates a fully tested and containerized backend application, with user authentication, image upload support, and robust API endpoints.

---

## Features
- **User Authentication**: User registration and login via `rest_framework.authtoken`.
- **Recipe Management**: Create, update, list, filter, and delete recipes.
- **Tags and Ingredients**: Endpoints for managing tags and ingredients.
- **Image Upload**: Recipes support image uploads for visual appeal.
- **PostgreSQL Database**: Optimized for relational data.
- **Code Quality**: Configured with `flake8` for code linting.
- **Continuous Integration**: Set up with Travis CI for automated testing and builds.
- **Containerization**: Docker and Docker Compose configurations included.
- **Test-Driven Development**: Comprehensive test coverage using TDD principles.

---

## Table of Contents
- [Technologies](#technologies)
- [Setup](#setup)
  - [Development](#development)
  - [Testing](#testing)
- [Endpoints](#endpoints)
- [Linting](#linting)
- [License](#license)

---

## Technologies
- **Django**: Backend framework.
- **Django REST Framework**: API development.
- **PostgreSQL**: Database.
- **Docker & Docker Compose**: Containerization.
- **Travis CI**: Continuous integration.
- **flake8**: Python code linting.

---

## Setup

### Prerequisites
- Install [Docker](https://www.docker.com/).
- Install [Docker Compose](https://docs.docker.com/compose/).
- Optionally install Python 3.10+ and pip if running without Docker.

### Development
1. Clone the repository:
    ```bash
    git clone https://github.com/darkkLUCIFER/recipe-app-api
    cd recipe-app
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

3. The app will be accessible at `http://localhost:8000`.

4. Apply migrations:
    ```bash
    docker-compose exec app python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    docker-compose exec app python manage.py createsuperuser
    ```

6. Access the admin panel at `http://localhost:8000/admin`.

---

### Testing
Run tests inside the Docker container:
```bash
docker-compose exec app python manage.py test
```
