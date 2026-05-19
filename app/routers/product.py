from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    category = db.query(models.Category).filter(
        models.Category.id == product.category_id
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    new_product = models.Product(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(page: int = 1, limit: int = 5, db: Session = Depends(get_db)):

    skip = (page - 1) * limit

    products = db.query(models.Product).offset(skip).limit(limit).all()

    return products


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


@router.put("/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, updated_product: schemas.ProductCreate, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated_product.name
    product.price = updated_product.price
    product.category_id = updated_product.category_id

    db.commit()
    db.refresh(product)

    return product


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(
        models.Product.id == id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}