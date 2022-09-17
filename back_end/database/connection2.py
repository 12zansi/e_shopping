from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "mysql+pymysql://root:1234@localhost:3366/e_shopping"
connection = create_engine(database_url)
session_local = sessionmaker(bind = connection)

Base = declarative_base()

