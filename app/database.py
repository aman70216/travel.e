from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:992Aman*@localhost:3306/ProductAndCategory" #Url of ProductAndCategory DB Use Here for Connection If You Want TO Run Locally Replace Root with Your UserName and 992Aman with your Password

Connect= create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=Connect
)

Base = declarative_base()

def get_db():     #I use this Because FastAPI dependency that provides a database session to My API
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
