from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.controller import router as controller_router

app = FastAPI(
    title="API Jurídica com Hugging Face",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


# Adiciona as rotas do controller
app.include_router(controller_router)
