
  
from typing import List, Dict
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import mainCategoriesSchema
from app.database.database import get_db
from app.services import mainCategoryServices
from app.models import mainCategoriesModels

router = APIRouter(prefix='/categories', tags=['Categories'])

@router.post('/main', response_model= mainCategoriesSchema.MainCategorySchema)
def create_main_category(category: mainCategoriesSchema.CreateMainCategory, db:Session = Depends(get_db)) -> mainCategoryServices.MainCategoryModel:
    
    check_category = mainCategoryServices.checkCategory(cName=category.cName)
    if check_category:
        raise HTTPException(status_code=400, detail=f"Woops the {category.cName} is in use")
    categoryModel:mainCategoriesModels.MainCategoryModel = mainCategoryServices.createCategory(db=db, category=category)
    return categoryModel

@router.get('/main', response_model= List[mainCategoriesSchema.MainCategorySchema])
def get_main_categories(db:Session = Depends(get_db)) -> List[mainCategoriesModels.MainCategoryModel]:
    categories: mainCategoriesModels.MainCategoryModel = mainCategoryServices.getCategories()
    return categories

@router.get('/main/{categoryId}', response_model=mainCategoriesSchema.MainCategorySchema)
def get_main_category_by_id(categoryId:int, db:Session = Depends(get_db)) -> mainCategoriesModels.MainCategoryModel |  Dict[str, str]:
    category: mainCategoriesModels.MainCategoryModel = mainCategoryServices.getCategoryById(id=categoryId)
    return category

@router.put('/main/{categoryId}', response_model= mainCategoriesSchema.MainCategorySchema )
def update_main_category(categoryId: int, category: mainCategoriesSchema.CreateMainCategory, db:Session = Depends(get_db)) ->  mainCategoriesModels.MainCategoryModel:
    return mainCategoryServices.updateCategory(db=db, id=categoryId, category=category)
    
    
@router.delete('/main/{categoryId}')
def delete_main_category(categoryId:int, db:Session =  Depends(get_db)) -> Dict[str, str]:
    mainCategoryServices.deleteCategory(db=db, id=categoryId)
    return {"message": f"successfully deleted category with id : {categoryId}"}
