from .db import engine
from sqlalchemy import Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

metadata = MetaData()

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, primary_key= True, nullable = False)
    email: Mapped[str] = mapped_column(String, nullable = False, unique= True)

    posts: Mapped[list["Posts"]] = relationship("Posts", back_populates="users", cascade="all, delete")

    

class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    user_name: Mapped[str] = mapped_column(String, ForeignKey("users.name", ondelete="CASCADE"))
    title: Mapped[str] = mapped_column(String, nullable = False)
    content: Mapped[str] = mapped_column(String, nullable= False)
    
    users: Mapped[Users] = relationship("Users", back_populates="posts")

    


#Database Creation and Deletion
def create_database():
    Base.metadata.create_all(engine)

def delete_database():
    Base.metadata.drop_all(engine)

if __name__ == "__main__":
       create_database()