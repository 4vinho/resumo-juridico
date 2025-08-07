from fastapi import FastAPI
from app.controller import router as controller_router

app = FastAPI(
    title="API Jurídica com Hugging Face",
    version="1.0.0"
)

# Adiciona as rotas do controller
app.include_router(controller_router)
