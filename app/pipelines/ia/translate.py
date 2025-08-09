from transformers import pipeline
from app.pipelines.utils.pipelineManager import PipelineManager


def translate_text(text: str, source_lang: str, target_lang: str, manager: PipelineManager) -> str:
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

    try:
        translator = pipeline("translation", model=model_name, device=manager.device)
        translated_text = translator(text)[0]['translation_text']
        return translated_text
    except Exception as e:
        return f"Erro na tradução: {e}. Verifique se o modelo {model_name} existe para esta combinação de idiomas."
