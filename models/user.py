from .db import SessionLocal
from .schema import Users
from sqlalchemy import select

def check_user(user_name: str):
    with SessionLocal() as session:
      try:
         statement = select(Users).where(Users.name == user_name)
         user = session.scalars(statement).one()
         return user
      
      except:
         return False
      
def create_user(user_name: str, user_email: str):
   with SessionLocal() as session:
      user = Users(name = user_name, email = user_email)
      session.add(user)
      session.commit()
      session.refresh(user)
      return user
   