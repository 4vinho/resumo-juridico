from transformers import pipeline
from app.pipelines.utils.pipelineManager import PipelineManager

def translate_text(text: str, source_lang: str, target_lang: str, manager: PipelineManager) -> str:
    """
    Traduz texto de uma língua para outra.
    source_lang: código da língua de origem (ex: 'en', 'pt', 'fr')
    target_lang: código da língua de destino (ex: 'en', 'pt', 'fr')
    """
    # Modelos Helsinki-NLP/opus-mt são nomeados como opus-mt-{source}-{target}
    # Ex: Helsinki-NLP/opus-mt-pt-en para Português para Inglês
    # Ex: Helsinki-NLP/opus-mt-en-pt para Inglês para Português
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    
    # O PipelineManager não gerencia modelos de tradução dinamicamente por nome de tarefa
    # Então, vamos criar o pipeline diretamente aqui, mas usando o device do manager
    try:
        translator = pipeline("translation", model=model_name, device=manager.device)
        translated_text = translator(text)[0]['translation_text']
        return translated_text
    except Exception as e:
        return f"Erro na tradução: {e}. Verifique se o modelo {model_name} existe para esta combinação de idiomas."
