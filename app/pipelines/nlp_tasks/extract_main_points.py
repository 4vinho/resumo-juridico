from typing import List

from app.pipelines.utils.pipelineManager import PipelineManager


def extract_main_points(story_text: str,
                         manager: PipelineManager,
                         max_points: int = 8) -> List[str]:
    pipe = manager.get_pipeline("story_points")

    prompt = (f"Read the story and extract the main points (main characters, key events, turning points, outcome). "
              f"Return as bullets, up to {max_points} items.\n\nStory:\n{story_text}")

    out = pipe(prompt, max_length=512, truncation=True)
    text = out[0].get('generated_text') if isinstance(out[0], dict) and 'generated_text' in out[0] else (
        out[0][0] if isinstance(out[0], list) else str(out))

    # Split the text into lines and remove any leading/trailing whitespace or bullet point characters
    lines = [l.strip("-•* \n\r\t") for l in text.splitlines() if l.strip()]

    # If splitting by lines doesn't work, try splitting by sentences.
    if len(lines) <= 1:
        lines = [p.strip() for p in text.split(". ") if p.strip()]    

    return lines[:max_points]