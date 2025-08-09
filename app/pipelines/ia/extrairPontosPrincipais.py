from typing import List

from app.pipelines.utils.pipelineManager import PipelineManager

def extract_story_points(story_text: str,
                         manager: PipelineManager,
                         max_points: int = 8,
                         language: str = "pt") -> List[str]:
    pipe = manager.get_pipeline("story_points")
    if language.startswith("pt"):
        prompt = (f"Leia a história abaixo e extraia os principais pontos (personagens principais, eventos chave, viradas, resultado). "
                  f"Retorne como uma lista numerada ou bullets, máximo {max_points} itens.\n\nHistória:\n{story_text}")
    else:
        prompt = (f"Read the story and extract the main points (main characters, key events, turning points, outcome). "
                  f"Return as bullets, up to {max_points} items.\n\nStory:\n{story_text}")

    out = pipe(prompt, max_length=512, truncation=True)
    text = out[0].get('generated_text') if isinstance(out[0], dict) and 'generated_text' in out[0] else (out[0][0] if isinstance(out[0], list) else str(out))

    lines = [l.strip("-• \n\r\t") for l in text.splitlines() if l.strip()]

    if len(lines) == 0:
        pieces = text.split(". ")
        lines = [p.strip() for p in pieces if p.strip()][:max_points]
    return lines[:max_points]
