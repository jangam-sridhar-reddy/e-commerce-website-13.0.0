from typing import List
from fastapi import HTTPException
from app.schemas.productSchema import CreateProductSchema
from app.models.productModels import ProductModel
from sqlalchemy.orm import Session

def checkProductName(pName:str):
    product =  ProductModel.query.filter(ProductModel.productName == pName).first()
    return product

def getProductByID(ID:int) -> ProductModel:
   product: ProductModel =  ProductModel.query.filter(ProductModel.ID == ID).first()

   if product is None:
       raise HTTPException(status_code=404, detail=f'Product with that ID : {ID} is not found.')
   
   return product


def getAllProducts(skip:int, limit:int)-> List[ProductModel]:
    return ProductModel.query.order_by(ProductModel.ID).offset(skip).limit(limit).all()


def updateProduct(ID:int, product:CreateProductSchema, db:Session) -> ProductModel:
    db_product: ProductModel = getProductByID(ID=ID)
    db_product.productName = product.productName
    db_product.imageURL = product.imageURL
    db_product.product_price = product.product_price
    db_product.stock_id = product.stock_id
    db_product.category_id = product.category_id
    db_product.sub_category_id = product.sub_category_id
    db.commit()
    db.refresh(db_product)
    return db_product


def createProduct(product:CreateProductSchema, db:Session) -> ProductModel:
    productCheck = checkProductName(pName=product.productName)
    p: CreateProductSchema = product
    if productCheck:
        raise HTTPException(status_code=400, detail=f'Woops the {p.productName} is in use.')
    
    db_product = ProductModel(productName = p.productName, imageURL = p.imageURL, product_price = p.product_price, stock_id = p.stock_id, category_id = p.category_id, sub_category_id = p.sub_category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
    

def deleteProduct(ID:int, db:Session) -> None:
    db_product:ProductModel = getProductByID(ID=ID)
    db.delete(db_product)
    db.commit()
