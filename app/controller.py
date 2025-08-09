from fastapi import APIRouter
from pydantic import BaseModel
from app.service import analise

router = APIRouter()

class InputText(BaseModel):
    texto: str
    outLanguage: str

@router.post("/processar")
def processar_texto(input_data: InputText):
    if not input_data.texto.strip():
        return {"erro": "Texto vazio fornecido."}

    result = analise(input_data)
    return {result}
