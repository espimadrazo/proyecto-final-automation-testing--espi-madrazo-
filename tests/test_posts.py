from pages.posts_api_page import PostsApi
from utils.logger import logger
import pytest_check as pcheck

api = PostsApi()

# GET ONE POST TEST
def test_get_one_post():
    response = api.get_one_post(5)

    logger.info("INITIALIZED POST REQUEST")

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
        body["id"], 5, "JSON ID DOES NOT MATCH"
        )
    
    logger.info("JSON ID CHECKED")

# ALL POSTS TEST
def test_get_all_posts():
    response = api.get_all_posts()

    logger.info("INITIALIZED POSTS REQUEST")


    # STATUS VALIDATION
    pcheck.equal(
        response.status_code,
        200,
        "WRONG STATUS"
    )

    logger.info("STATUS CHECKED")

    # VALIDATE JSON POSTS QUANTITY
    posts = response.json()

    pcheck.is_true(
        len(posts) > 0,
        "FAILED TO OBTAIN POSTS"
    )

    logger.info("POSTS QUANTITY CHECKED")

    # VALIDATE IF OBTAINED JSON IS LIST
    pcheck.is_true(
        isinstance(posts, list),
        "OBTAINED RESPONSE IS NOT A LIST"
    )
    
    logger.info("JSON FORMAT CHECKED")

# SEND POST TEST
def test_send_post(post_data):
    response = api.send_post(
        post_data["title"],
        post_data["body"],
        post_data["userId"]
    )

    logger.info("SENT POST REQUEST")

    # STATUS VALIDATION
    pcheck.equal(
        response.status_code,
        201,
        "POST FAILED"
    )

    logger.info("STATUS CHECKED")