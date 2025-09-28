
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASEURL = "sqlite:///./models/sqlite.db"
#DATABASEURL = "sqlite:///.sqlite.db"

engine = create_engine(DATABASEURL)
SessionLocal = sessionmaker(bind = engine, expire_on_commit = False)