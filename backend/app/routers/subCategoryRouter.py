

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.subCategoriesSchema import SubCategoriesSchema, SubCategoriesCreateSchema
from app.database.database import get_db
from app.services.subCategoryServices import createSubCategory, getSubCategories, getSubCategoryById, updateSubCategory, deleteSubCategory
from app.models.subCategoriesModels import SubCategoriesModel


router = APIRouter(prefix='/categories', tags=['Sub Category'])



@router.post('/sub', response_model= SubCategoriesSchema)
def create_sub(sub: SubCategoriesCreateSchema, db:Session=Depends(get_db)) -> SubCategoriesModel:
    return createSubCategory(sub=sub, db=db)

@router.get('/sub/{ID}', response_model= SubCategoriesSchema)
def get_sub_category_by_id(ID:int) -> SubCategoriesModel: 
    subCategory: SubCategoriesModel = getSubCategoryById(id=ID)
    return  subCategory


@router.get('/sub', response_model=List[SubCategoriesSchema])
def get_sub_categories(skip:int= 0, limit:int = 10) -> List[SubCategoriesModel]:
    return getSubCategories(skip=skip, limit=limit)


@router.put('/sub/{ID}', response_model=SubCategoriesSchema)
def update_sub_category(ID:int, sub: SubCategoriesCreateSchema, db:Session= Depends(get_db)) -> SubCategoriesModel:
    return updateSubCategory(id=ID, sub=sub, db=db)

@router.delete('/sub/{ID}')
def delete_sub_category(ID:int, db:Session = Depends(get_db)):
    deleteSubCategory(id=ID, db=db)
    return {'Message': f"successfully deleted Sub Category with ID : {ID}"}