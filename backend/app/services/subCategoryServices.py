
from typing import List
from app.schemas.subCategoriesSchema import SubCategoriesCreateSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.subCategoriesModels import SubCategoriesModel


def getSubCategoryById(id:int) -> SubCategoriesModel:
    subCategory: SubCategoriesModel =  SubCategoriesModel.query.filter(SubCategoriesModel.ID == id).first() 
    
    if subCategory is None:
        raise HTTPException(status_code=404, detail=f'Sub category with that ID: {id} not found.')

    if not subCategory.is_active:
        raise HTTPException(status_code=400, detail=f'Sub category with that ID: {id} is inactive.')
    
    return subCategory

def checkSubCategoryByName(subCname:str)  -> SubCategoriesModel:
    return SubCategoriesModel.query.filter(SubCategoriesModel.subCname == subCname).first()

def createSubCategory(sub:SubCategoriesCreateSchema, db:Session):
    subCategory: SubCategoriesModel = checkSubCategoryByName(subCname=sub.subCname)
    if subCategory:
        raise HTTPException(status_code=400,  detail=f"Woops the {sub.subCname} is in use")
        
    createSub = SubCategoriesModel(subCname = sub.subCname, is_active = sub.is_active)
    db.add(createSub)
    db.commit()
    db.refresh(createSub)
    return createSub
    

def getSubCategories(skip:int, limit:int) -> List[SubCategoriesModel]:
    return SubCategoriesModel.query.filter(SubCategoriesModel.is_active == True).order_by(SubCategoriesModel.ID).offset(skip).limit(limit).all()

def updateSubCategory(id:int, sub:SubCategoriesCreateSchema, db:Session) -> SubCategoriesModel:
    subCategory: SubCategoriesModel = getSubCategoryById(id=id)
    subCategory.subCname = sub.subCname
    subCategory.is_active = sub.is_active
    db.commit()
    db.refresh(subCategory)
    return subCategory

def deleteSubCategory(id:int, db:Session):
    subCategory: SubCategoriesModel = getSubCategoryById(id)
    subCategory.is_active = 0
    db.commit()
    db.refresh(subCategory)