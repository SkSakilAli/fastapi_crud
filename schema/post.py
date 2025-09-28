from pydantic import BaseModel, Field, EmailStr

class Post_request(BaseModel):
    user_name:str= Field(
        title = "User's Name",
        min_length =1,
        max_length = 50,
    )
    user_email: EmailStr
    post_title: str = Field(
        title = "Post's Title",
        max_length = 200,
    )
    post_content: str = Field(
        title= "Post Content",
    )