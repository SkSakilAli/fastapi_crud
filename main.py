from fastapi import FastAPI
from schema.post import Post_request
from models.user import check_user, create_user
from models.posts import create_a_post
from controllers.post import *

app = FastAPI()

@app.post("/create_post")
def create_post_request(post_data: Post_request):
      return create_post(post_data)

@app.get("/post/")
def view_post_request(user_name: str | None = None):
      posts = view_post(user_name)

      return {
            "status":"success",
            "posts": posts
      }