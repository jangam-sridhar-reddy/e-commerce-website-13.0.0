from typing import List
from fastapi import File, Form, HTTPException, UploadFile
from app.schemas.productSchema import CreateProductSchema
from app.models.productModels import ProductModel
from sqlalchemy.orm import Session, joinedload
from app.services.productImageServices import upload_image_to_cloudinary
from app.models.subCategoriesModels import SubCategoriesModel
from app.models.mainCategoriesModels import MainCategoryModel

def checkProductName(pName:str):
    product =  ProductModel.query.filter(ProductModel.productName == pName).first()
    return product

def getProductByID(ID:int) -> ProductModel:
   product: ProductModel =  ProductModel.query.filter(ProductModel.ID == ID).first()

   if product is None:
       raise HTTPException(status_code=404, detail=f'Product with that ID : {ID} is not found.')
   
   return product


def getAllProducts(skip:int, limit:int, db: Session)-> List[dict]:

    products: List[ProductModel] =(
        db.query(ProductModel)
        .options(
            joinedload(ProductModel.category),
            joinedload(ProductModel.subCategory),
            joinedload(ProductModel.stock)
        )
        .order_by(ProductModel.ID)
        .offset(skip)
        .limit(limit)
        .all()
    )
    
    productResults: List = []

    for product in products:
        productResults.append({
            "ID" : product.ID,
            "productName": product.productName,
            "product_price": product.product_price,
            "imageURL": product.imageURL,
            "created_at": product.created_at,
            "updated_at": product.updated_at,
            "category_id": product.category_id,
            "sub_category_id": product.sub_category_id,
            "stock_id": product.stock_id,
            "category_name": product.category.cName if product.category else None,
            "subCategory_name": product.subCategory.subCname if product.subCategory else None,
            "stockStatus": product.stock.statusName if product.stock else None
        })
    return productResults


async def updateProduct(
        ID:int, 
        productName: str, 
        product_price:str, 
        stock_id:int, 
        category_id:int, 
        sub_category_id:int, 
        image: UploadFile, 
        db:Session
        ) -> ProductModel:

        try:

            db_product: ProductModel =  db.query(ProductModel).filter(ProductModel.ID == ID).first()

            if db_product is None:
                raise HTTPException(status_code=404, detail=f'Product with that ID : {ID} is not found.')
            
            # upload image
            image_urls = await upload_image_to_cloudinary(image=image,product_name=productName)  
            db_product.productName = productName
            db_product.imageURL = image_urls['cropped_url']
            db_product.product_price = product_price
            db_product.stock_id = stock_id
            db_product.category_id = category_id
            db_product.sub_category_id = sub_category_id
            db.commit()
            db.refresh(db_product)
            return db_product
        
        except HTTPException as http_exc:
            raise http_exc
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        


async def createProduct(
        productName: str, 
        product_price:str, 
        stock_id:int, 
        category_id:int, 
        sub_category_id:int, 
        image: UploadFile, 
        db:Session
        ) -> ProductModel:
    
    try:
        productCheck = checkProductName(pName=productName)
        if productCheck:
            raise HTTPException(status_code=400, detail=f'Woops the product name: {productName} is in use. ')
        
        # upload image
        image_urls = await upload_image_to_cloudinary(image=image,product_name=productName)  
        db_product: ProductModel = ProductModel(
            productName = productName,
            imageURL = image_urls['cropped_url'],
            product_price = product_price,
            stock_id = stock_id,
            category_id = category_id,
            sub_category_id = sub_category_id
        )

        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    
    except HTTPException as http_exc:
        raise http_exc 
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

def deleteProduct(ID:int, db:Session) -> None:
    db_product:ProductModel = getProductByID(ID=ID)
    db.delete(db_product)
    db.commit()
