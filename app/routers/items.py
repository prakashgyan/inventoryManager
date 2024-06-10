from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, database, dependencies

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(dependencies.get_current_user)]
)

@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(dependencies.get_current_user)):
    return crud.create_item(db=db, item=item, user_id=current_user.id)
