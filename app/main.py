from fastapi import FastAPI

from app.database import Connect, Base
from app.routers import category, product

Base.metadata.create_all(bind=Connect) # Connecting to Database ProductAndCategory Of Mysql 

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)
