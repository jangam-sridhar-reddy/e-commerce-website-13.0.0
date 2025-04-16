from sqlalchemy.orm import Session
from fastapi import HTTPException 

from app.models.mainCategoriesModels import MainCategoryModel
from app.schemas.mainCategoriesSchema import CreateMainCategory


def checkCategory(cName:str) -> MainCategoryModel:
    category_model: MainCategoryModel =  MainCategoryModel.query.filter(MainCategoryModel.cName == cName).first()
    return category_model

def getCategoryById(id:int) -> MainCategoryModel:
    category: MainCategoryModel =  MainCategoryModel.query.filter(MainCategoryModel.ID == id).first()

    if category is None:
        raise HTTPException(status_code=404, detail=f'Category with that ID: {id} not found.')
    
    if not category.is_active:
        raise HTTPException(status_code=400, detail=f'Category with that ID: {id} is inactive.')
    
    return category


def createCategory(db:Session,  category: CreateMainCategory):
    category_model = MainCategoryModel(cName = category.cName, is_active = category.is_active)

    db.add(category_model)
    db.commit()
    db.refresh(category_model)
    return category_model

def getCategories() -> MainCategoryModel:
    return MainCategoryModel.query.filter(MainCategoryModel.is_active == True).all()

def updateCategory(db:Session, id:int,  category: MainCategoryModel) -> MainCategoryModel:

    categoryModel: MainCategoryModel = getCategoryById(id)
    
    
    categoryModel.cName =  category.cName
    categoryModel.is_active = category.is_active
    db.commit()
    db.refresh(categoryModel)
    return categoryModel


def deleteCategory(db:Session, id:int) -> None:
    categoryModel: MainCategoryModel = getCategoryById(id)
    categoryModel.is_active = 0
    db.commit()
    db.refresh(categoryModel)
   
    



    