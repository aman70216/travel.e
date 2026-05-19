from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db   #Create API and Serving to each Request
from app import models, schemas

router = APIRouter(
    prefix="/api/categories",  
    tags=["Categories"]
)


@router.post("/", response_model=schemas.CategoryResponse)  
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(name=category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


@router.get("/", response_model=list[schemas.CategoryResponse])
def get_categories(page: int = 1, limit: int = 5, db: Session = Depends(get_db)):
    skip = (page - 1) * limit

    categories = db.query(models.Category).offset(skip).limit(limit).all()

    return categories


@router.get("/{id}", response_model=schemas.CategoryResponse)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.put("/{id}", response_model=schemas.CategoryResponse)
def update_category(id: int, updated_category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.name = updated_category.name

    db.commit()
    db.refresh(category)

    return category


@router.delete("/{id}")
def delete_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted successfully"}