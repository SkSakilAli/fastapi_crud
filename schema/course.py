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