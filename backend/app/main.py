from fastapi import FastAPI

from app.routers import categoryRouter, subCategoryRouter, productRouter
app = FastAPI()

app.include_router(categoryRouter.router, prefix='/api')
app.include_router(subCategoryRouter.router, prefix='/api')
app.include_router(productRouter.router, prefix='/api')