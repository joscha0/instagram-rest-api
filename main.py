from fastapi import FastAPI
from scraper_profile import get_profile_data
from scraper_post import get_post_data
from models import Post, User


app = FastAPI()


@app.get("/")
def read_root():
    return {0: "Instagram REST API"}


@app.get("/u/{username}", response_model=User)
def get_data_username(username: str):
    return get_profile_data(username)


@app.get("/p/{post}", response_model=Post)
def get_data_post(post: str):
    return get_post_data(f"https://www.instagram.com/p/{post}")
