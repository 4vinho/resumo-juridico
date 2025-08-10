from app.pipelines.utils.pipelineManager import PipelineManager
from app.pipelines.nlp_tasks.summarize import summarize_text
from app.pipelines.nlp_tasks.generate_argumentation import generate_argumentation
from app.pipelines.nlp_tasks.extract_main_points import extract_main_points
from app.pipelines.nlp_tasks.translate import translate_text

manager = PipelineManager()

def  analise(input_data):
    text = input_data.texto
    language = input_data.language.split("-")[0].lower()

    text_en = translate_text(text, language, "en", manager)

    summary_en = summarize_text(text_en, manager)
    argumentation_en = generate_argumentation(text_en, context=text_en, manager=manager)
    story_points_en = extract_main_points(text_en, manager, 5)

    if language == "en":
        summary = summary_en
        argumentation = argumentation_en
        story_points = story_points_en
    else:
        summary = translate_text(summary_en, "en", language, manager)
        argumentation = translate_text(argumentation_en, "en", language, manager)
        story_points = [translate_text(p, "en", language, manager) for p in story_points_en]

    return {
        "resumo": summary,
        "argumentacao": argumentation,
        "pontos_principais": story_points,
    }