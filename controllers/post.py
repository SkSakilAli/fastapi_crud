from schema.post import Post_request
from models.user import check_user, create_user
from models.posts import create_a_post, view_post

def create_post(post_data):
      try:
        if not check_user(post_data.user_name):
              create_user(post_data.user_name, post_data.user_email)
        
        post = create_a_post(post_data.user_name, post_data.post_title, post_data.post_content) 
        return{"staus":"success",
         "post_id": post.id}         
      except:
         return {"status": "something went wrong"}
    
def view_post_by_username(username: str):
     try:
        return view_post()
     except:
         return {"status": "Something Went Wrong"}
     

    