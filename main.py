from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from scraper_profile import get_profile_data
from scraper_post import get_post_data
from models import Post, User


app = FastAPI()


@app.get("/u/{username}")
def get_data_username(username: str):
    """
    Get Data of user
    """
    return get_profile_data(username)


@app.get("/p/{post}")
def get_data_post(post: str):
    """
    Get Data of post
    """
    return get_post_data(f"http://www.instagram.com/p/{post}")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Unofficial Instagram Rest API",
        version="1.0",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
