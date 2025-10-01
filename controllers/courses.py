from models.user import check_user
from models.courses import get_courses_by_user, get_courses_all, get_users_enrolled_in_course, create_course, check_course_by_title, check_course_by_id,enroll_course_by_username
from fastapi import HTTPException

def create_a_course(course_title: str, course_description: str):
    if not check_course_by_title(course_title):
        course_id = create_course(course_title, course_description)
        return course_id
    else:
        raise HTTPException(status_code=409, detail="Course with same title exist")

def get_courses_user(user_name: str | None):
  if user_name:
    if not check_user(user_name):
         raise  HTTPException(status_code=404, detail="User Does Not exist")
    else:
         try:
              courses = get_courses_by_user(user_name)
              return courses
         except:
           raise  HTTPException(status_code=500, detail="Database Error")
  else:
      try:
          courses =get_courses_all()
          return courses
      except:
          raise HTTPException(status_code=500, detail="Database Error")
      
def get_users(course_id: int):
      return get_users_enrolled_in_course(course_id)


def enroll_course(user_name: str, course_id: int):
    if not check_user(user_name):
        raise HTTPException(status_code=404, detail="User Does not exist")
    elif not check_course_by_id(course_id):
        raise HTTPException(status_code = 404, detail = "Course Does Not Exist")
    else:
        try:
           courses = enroll_course_by_username(course_id, user_name)
           return courses
        except:
            raise HTTPException(status_code = 500, detail="Database Error")
            