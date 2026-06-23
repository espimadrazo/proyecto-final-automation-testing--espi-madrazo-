from pages.users_api_page import UsersApi
from utils.logger import logger
import pytest_check as pcheck

api = UsersApi()

# GET ONE USER TEST
def test_get_one_user():
    response = api.get_one_user(2)

    logger.info("SENT GET USER REQUEST")

    # STATUS VALIDATION
    pcheck.equal(
        response.status_code,
        200,
        "WRONG STATUS"
        )

    logger.info("STATUS CHECKED")

    # JSON ID VALIDATION
    body = response.json()

    pcheck.equal(
        body["id"],
        2,
        "JSON ID DOES NOT MATCH"
        )

    logger.info("JSON ID CHECKED")

# UPDATE USER TEST
def test_update_user(users_data):
    response = api.update_user(
        users_data["id"],
        users_data["name"],
        users_data["username"],
        users_data["email"]
    )

    logger.info("SENT UPDATE USER REQUEST")

    # STATUS VALIDATION
    pcheck.equal(
        response.status_code,
        200,
        "UPDATE FAILED"
    )

    logger.info("STATUS CHECKED")

# DELETE USER TEST
def test_delete_user(users_data):
    response = api.delete_user(
        users_data["id"]
    )

    logger.info("SENT DELETE REQUEST")

    # STATUS VALIDATION
    pcheck.equal(
        response.status_code,
        200,
        "USER DELETION FAILED"
    )

    logger.info("STATUS CHECKED")

