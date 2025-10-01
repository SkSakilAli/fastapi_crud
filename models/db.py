
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
DATABASEURL = os.getenv("DATABASE_URL_SQLITE")


engine = create_engine(DATABASEURL)
SessionLocal = sessionmaker(bind = engine, expire_on_commit = False)