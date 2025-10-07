
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine

from sqlalchemy.orm import Session

import database_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://lolcalhost:3000'],
    allow_methods =['*']
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome MB !"
    

products = [
    Product(id=1,name="Phone",description="iPhone 17 new launch",price=199.9,quantity=12),
    Product(id=2,name="Desktop",description="iPhone 17 new launch",price=199.9,quantity=12),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        
    db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products
    
@app.get("/product/{id}")
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_products:
        return db_products
    return "product not found"

@app.post("/product")
def add_product(product: Product,db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/product/{id}")
def update_product(id: int, product: Product,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db_product.quantity = product.quantity
            db.commit()
            return "Product Updated Successfully"
    else:   
        return "No product Updated"

@app.delete("/product/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully"
    else:
        return "product not found"