from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import categoryRouter, subCategoryRouter, productRouter, userRouter
app = FastAPI()
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userRouter.router, prefix='/api')
app.include_router(categoryRouter.router, prefix='/api')
app.include_router(subCategoryRouter.router, prefix='/api')
app.include_router(productRouter.router, prefix='/api')