# part of built in os python module
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus as urlquote # need to include password this way because it contains '@'

load_dotenv()

password = getenv('DB_PASSWORD')

# connect to database using env variable
engine = create_engine('mysql+pymysql://root:%s@localhost/python_news_db' % urlquote(password), echo=True, pool_size=20, max_overflow=0) # manages the overall connection to the database
Session = sessionmaker(bind=engine) # generates temporary connections for performing CRUD operations
Base = declarative_base() # helps us map the models to real MySQL tables