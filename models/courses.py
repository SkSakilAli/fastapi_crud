from .db import SessionLocal
from sqlalchemy import String, Integer, select, update
from .schema import Users, Courses

def check_course_by_id(course_id: int):
    with SessionLocal() as session:
       try:
        course = session.get_one(Courses, course_id)
        return True
       except:
           return False
        

def check_course_by_title(course_title: str):
     
      with SessionLocal() as session:
        statement = select(Courses).where(Courses.title == course_title) 
        course =session.scalars(statement).all()
        session.commit()
        return course
      
        
    
def create_course(course_title: str, course_description: str):
     with SessionLocal() as session:
        course = Courses(title = course_title, description = course_description)
        session.add(course)
        session.commit()
        session.refresh(course)
        return {"id":course.id}
   

def enroll_course_by_username(course_id: int, user_name: str):
   with SessionLocal() as session:
      course = session.get_one(Courses, course_id)
      user = session.get_one(Users, user_name)
      user.courses.append(course)
      session.commit()
      session.refresh(course)
      return_course = user.courses
      return return_course
    
def get_courses_by_user(user_name: str):
     with SessionLocal() as session:
        user = session.get(Users, user_name)
        return user.courses
      
      
def get_courses_all():
   with SessionLocal() as session:
         statement = select(Courses)
         courses= session.scalars(statement).all()
         return courses
   
def get_users_enrolled_in_course(course_id: int):
    with SessionLocal() as session:
        courses =session.get(Courses, course_id)
        users = courses.users
        return users
    
