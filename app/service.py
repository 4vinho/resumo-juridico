from app.pipelines.utils.pipelineManager import PipelineManager
from app.pipelines.nlp_tasks.summarize import summarize_text
from app.pipelines.nlp_tasks.generate_argumentation import generate_argumentation
from app.pipelines.nlp_tasks.extract_main_points import extract_main_points
from app.pipelines.nlp_tasks.translate import translate_text

manager = PipelineManager()

def  analise(input_data):
    text = input_data.texto
    source_language = "pt"
    target_language = input_data.outLanguage

    # Translate the input text to English for better processing
    text_en = translate_text(text, source_language, "en", manager)

    # Perform NLP tasks in English
    summary_en = summarize_text(text_en, manager)
    argumentation_en = generate_argumentation(text_en, context=text_en, manager=manager)
    story_points_en = extract_main_points(text_en, manager, 5)

    # Translate the results to the target language if it's not English
    if target_language == "en":
        summary = summary_en
        argumentation = argumentation_en
        story_points = story_points_en
        translated_summary = summary_en # The English summary is the translated summary
    else:
        summary = translate_text(summary_en, "en", target_language, manager)
        argumentation = translate_text(argumentation_en, "en", target_language, manager)
        story_points = [translate_text(p, "en", target_language, manager) for p in story_points_en]
        translated_summary = summary # The summary is already translated

    return {
        "resumo": summary,
        "argumentacao": argumentation,
        "pontos_principais": story_points,
        "resumo_traduzido": translated_summary,
    }