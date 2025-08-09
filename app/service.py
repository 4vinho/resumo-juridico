from app.pipelines.utils.pipelineManager import PipelineManager
from app.pipelines.ia.resumir import summarize_text
from app.pipelines.ia.montarArqgumentacao import defend_point
from app.pipelines.ia.extrairPontosPrincipais import extract_story_points
from app.pipelines.ia.translate import translate_text

def juridicoCompleto(input_data):
    manager = PipelineManager()
    text = input_data.texto
    source_language = input_data.outLanguage # Assuming outLanguage is the source language
    target_language = input_data.targetLanguage

    # Exemplo de uso das funções refatoradas
    summary = summarize_text(text, manager)
    argumentation = defend_point("A tese jurídica é válida.", context=text, manager=manager, language=source_language)
    story_points = extract_story_points(text, manager, language=source_language)
    
    # Tradução do resumo para o inglês
    translated_summary = translate_text(summary, source_language, target_language, manager)

    return {
        "resumo": summary,
        "argumentacao": argumentation,
        "pontos_principais": story_points,
        "resumo_traduzido_para_ingles": translated_summary
    }