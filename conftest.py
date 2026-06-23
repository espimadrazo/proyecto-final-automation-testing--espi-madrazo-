import pytest

# POSTS DATA FOR REQUESTS
@pytest.fixture
def post_data():
    return {
        "title": "Lorem ipsum título",
        "body": "Lorem ipsum body",
        "userId": 1
        }

# USER DATA FOR REQUESTS
@pytest.fixture
def users_data():
    return {
        "id": 3,
        "name": "Espi",
        "username": "espi94",
        "email": "espi@gmail.com"
        }