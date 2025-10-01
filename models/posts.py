from .db import SessionLocal
from sqlalchemy import String, Integer, select, update
from .schema import Posts, Users
from .user import create_user, check_user
import json

def create_a_post(user_name: str, post_title: str, post_content: str):
    with SessionLocal() as session:
       
        post = Posts(user_name = user_name, title = post_title, content= post_content)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post        
      
        
def view_post(user_name: str | None = None):
     with SessionLocal() as session:
        if user_name:
          try:
            statement = select(Posts).where(Posts.user_name == user_name)
            posts = session.scalars(statement).all()
            result = {}
            for post in posts:
              result[post.id] ={
              'id': post.id,
              'user_name': post.user_name,
              'title': post.title,
              'content': post.content
              }

            return result
        
          except:
            return {"status": "check username"}
        else:
            statement = select(Posts)
            posts = session.scalars(statement).all()

            result = {}
            for post in posts:
              result[post.id] ={
              'id': post.id,
              'user_name': post.user_name,
              'title': post.title,
              'content': post.content
              }

            return result

        