from transformers import AutoTokenizer
from typing import List

from app.pipelines.utils.pipelineManager import PipelineManager
from app.pipelines.utils.tokens import chunk_text_by_tokens

def summarize_text(text: str,
                   manager: PipelineManager,
                   max_length: int = 150,
                   min_length: int = 40,
                   chunk_overlap: int = 64,
                   final_compress: bool = True) -> str:

    pipe = manager.get_pipeline("summarization")
    tokenizer = manager.get_tokenizer("summarization")
    model_max = getattr(tokenizer, "model_max_length", 1024)
    chunk_size = min(model_max - 50, 1024)
    chunks = chunk_text_by_tokens(text, tokenizer, chunk_size, overlap=chunk_overlap)

    summaries = []
    for c in chunks:
        try:
            out = pipe(c, max_length=max_length, min_length=min_length, truncation=True)
            # pipeline retorna lista de dicts em geral
            txt = out[0]['summary_text'] if isinstance(out, list) and isinstance(out[0], dict) else str(out)
            summaries.append(txt.strip())
        except Exception as e:
            # fallback: truncar e tentar de novo
            truncated = c[:model_max * 4]  # fallback simples
            out = pipe(truncated, max_length=max_length, min_length=min_length, truncation=True)
            summaries.append(out[0]['summary_text'])

    if len(summaries) == 1 or not final_compress:
        return "\n\n".join(summaries)

    combined = " ".join(summaries)
    try:
        final = pipe(combined, max_length=max_length, min_length=min_length, truncation=True)
        return final[0]['summary_text'].strip()
    except Exception:
        return "\n\n".join(summaries)
