from .db import engine
from sqlalchemy import Integer, String, MetaData, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

metadata = MetaData()

class Base(DeclarativeBase):
    pass

# Asscociation Table for Users and Courses Relationship  
users_courses_table = Table(
     "users_courses",
     Base.metadata,
     Column("users", ForeignKey("users.name"), primary_key= True),
     Column("courses", ForeignKey("courses.id"), primary_key = True)
)

class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, primary_key= True, nullable = False)
    email: Mapped[str] = mapped_column(String, nullable = False, unique= True)

    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="users", cascade="all, delete")
    courses: Mapped[list["Courses"]]= relationship("Courses", back_populates="users", secondary = users_courses_table)

    

class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    user_name: Mapped[str] = mapped_column(String, ForeignKey("users.name", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String, nullable = False)
    content: Mapped[str] = mapped_column(String, nullable= False)
    
    users: Mapped[Users] = relationship("Users", back_populates="posts")


     

class Courses(Base):
     __tablename__ = "courses"
     
     id: Mapped[int] = mapped_column(Integer, primary_key = True)
     title: Mapped[str] = mapped_column(String, nullable = False)
     description: Mapped[str] = mapped_column(String, nullable = False)
     users: Mapped[list[Users]]= relationship("Users", back_populates="courses", secondary = users_courses_table)

#Database Creation and Deletion
def create_database():
    Base.metadata.create_all(engine)

def delete_database():
    Base.metadata.drop_all(engine)

if __name__ == "__main__":
       delete_database()