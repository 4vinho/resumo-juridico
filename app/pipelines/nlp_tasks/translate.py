from app.pipelines.utils.pipelineManager import PipelineManager

def get_lang_code(lang: str) -> str:
    lang_map = {
        "pt": "por_Latn",
        "en": "eng_Latn",
        "de": "deu_Latn",
        "fr": "fra_Latn",
        "es": "spa_Latn",
    }
    return lang_map.get(lang, lang)

def translate_text(text: str, source_lang: str, target_lang: str, manager: PipelineManager) -> str:
    source_lang_code = get_lang_code(source_lang)
    target_lang_code = get_lang_code(target_lang)
    
    try:
        translator = manager.get_pipeline("translation")
        
        translated_text = translator(text, src_lang=source_lang_code, tgt_lang=target_lang_code, max_length=512, truncation=True)[0]['translation_text']
        return translated_text.strip()
    except Exception as e:
        return f"Erro na tradução: {e}. Verifique se o modelo suporta esta combinação de idiomas."