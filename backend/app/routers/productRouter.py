
from typing import List
from fastapi import APIRouter, Depends, File,  Form, UploadFile
from sqlalchemy.orm import Session
from app.schemas.productSchema import ProductSchema, CreateProductSchema 
from app.models.productModels import ProductModel
from app.database.database import get_db
from app.services.productServices import createProduct, getProductByID, getAllProducts, updateProduct, deleteProduct

router = APIRouter(prefix="/product", tags=['Product'])

@router.post('/add', response_model=CreateProductSchema) 
async def create_Product(
    productName: str = Form(...), 
    product_price:str = Form(...), 
    stock_id:int = Form(...), 
    category_id:int = Form(...), 
    sub_category_id:int = Form(...), 
    image: UploadFile = File(...),  
    db:Session = Depends(get_db)
    )  -> ProductModel:

    db_product: ProductModel =  await createProduct(
        productName=productName, 
        product_price=product_price, 
        stock_id=stock_id, 
        category_id= category_id, 
        sub_category_id=sub_category_id, 
        image=image, 
        db=db
        )
    return db_product

@router.get('/get-product/{ID}', response_model=ProductSchema)
def get_product_by_id(ID:int) -> ProductModel:
    return getProductByID(ID=ID)
    
@router.get('/get-products', response_model=List[ProductSchema])
def get_products(skip:int = 0, limit:int = 10) -> List[ProductModel]:
    return getAllProducts(skip=skip, limit=limit)

@router.put('/update/{ID}', response_model=CreateProductSchema)
async def update_product(
    ID:int, 
    productName: str = Form(...), 
    product_price:str = Form(...), 
    stock_id:int = Form(...), 
    category_id:int = Form(...), 
    sub_category_id:int = Form(...), 
    image: UploadFile = File(...),  
    db:Session = Depends(get_db)
    ) -> ProductModel:

    db_product: ProductModel = await updateProduct(
        ID=ID, 
        productName=productName, 
        product_price=product_price, 
        stock_id=stock_id, 
        category_id= category_id, 
        sub_category_id=sub_category_id, 
        image=image, 
        db=db
        )
    return db_product

@router.delete('/delete/{ID}')
def delete_product(ID:int, db:Session = Depends(get_db)):
    deleteProduct(ID=ID, db=db)
    return {"message": f"Product with ID {ID} deleted successfully"}
    