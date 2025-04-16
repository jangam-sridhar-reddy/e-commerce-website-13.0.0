
from app.database.database import engine
from app.models.baseModel import Base
from app.models.mainCategoriesModels import MainCategoryModel
from app.models.subCategoriesModels import SubCategoriesModel

Base.metadata.create_all(bind=engine)
