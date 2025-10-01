from pydantic import BaseModel, Field

class Course_request(BaseModel):
   title: str = Field(
      title = "Course Title",
      max_length= 250
   )
   description: str = Field(
      title = "Description",
      max_length= 100
   )                   

class Enroll_request(BaseModel):
      user_name: str = Field(
         title= "User Name to be enrolled"
      )
      course_id: int = Field(
         title = "Course ID to be enrolled"
      )