from fastapi import FastAPI

from app.routers import categoryRouter, subCategoryRouter
app = FastAPI()

app.include_router(categoryRouter.router, prefix='/api')
app.include_router(subCategoryRouter.router, prefix='/api')