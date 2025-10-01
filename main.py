from fastapi import FastAPI
from schema.course import Course_request, Enroll_request
from schema.post import Post_request
from controllers.post import *
from controllers.courses import get_courses_user, get_users, create_a_course, enroll_course

app = FastAPI()

@app.post("/create_post")
def create_post_request(post_data: Post_request):
      return create_post(post_data)

@app.get("/post")
def view_post_request(user_name: str | None = None):
      posts = view_post(user_name)
      return {
            "status":"success",
            "posts": posts
      }


@app.post("/course/create")
def create_course_request(course_data: Course_request):
     return create_a_course(course_data.title, course_data.description)

@app.post("/course/enroll")
def enroll_course_request(course_user_data: Enroll_request):
     return enroll_course(course_user_data.user_name, course_user_data.course_id)

@app.get("/course")
def get_course(user_name: str | None = None):
  courses = get_courses_user(user_name)
  return courses

@app.get("/course/users")
def get_users_by_course(course_id: int):
     return get_users(course_id)