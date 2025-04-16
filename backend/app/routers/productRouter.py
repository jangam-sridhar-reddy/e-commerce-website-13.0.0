
from typing import List
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.schemas.productSchema import ProductSchema, CreateProductSchema
from fastapi import Depends
from app.models.productModels import ProductModel
from app.database.database import get_db
from app.services.productServices import createProduct, getProductByID, getAllProducts, updateProduct, deleteProduct

router = APIRouter(prefix="/product", tags=['Product'])

@router.post('/add', response_model=ProductSchema) 
def create_Product(product: CreateProductSchema, db:Session = Depends(get_db)) -> ProductModel:
    return createProduct(product=product, db=db)

@router.get('/get-product/{ID}', response_model=ProductSchema)
def get_product_by_id(ID:int) -> ProductModel:
    return getProductByID(ID=ID)
    
@router.get('/get-products', response_model=List[ProductSchema])
def get_products(skip:int = 0, limit:int = 10) -> List[ProductModel]:
    return getAllProducts(skip=skip, limit=limit)

@router.put('/update/{ID}', response_model=CreateProductSchema)
def update_product(ID:int, product: CreateProductSchema, db:Session = Depends(get_db)) -> ProductModel:
    return updateProduct(ID=ID, product=product, db=db)

@router.delete('/delete/{ID}')
def delete_product(ID:int, db:Session = Depends(get_db)):
    deleteProduct(ID=ID, db=db)
    return {"message": f"Product with ID {ID} deleted successfully"}
    