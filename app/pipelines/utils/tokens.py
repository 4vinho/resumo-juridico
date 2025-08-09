from transformers import AutoTokenizer
from typing import List

#Class responsável por tokenizar algum texto, criado para casos onde precisa-se trabalhar com modelos de linguagem que têm limite de tokens

def chunk_text_by_tokens(
        text: str,
        tokenizer: AutoTokenizer,
        max_tokens: int,
        overlap: int = 50) -> List[str]:

    if max_tokens <= 0:
        return [text]

    tokens = tokenizer.encode(text, add_special_tokens=False)
    chunks = []
    i = 0
    L = len(tokens)

    while i < L:
        chunk_tokens = tokens[i: i + max_tokens]
        chunk = tokenizer.decode(chunk_tokens, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        chunks.append(chunk.strip())
        i += max_tokens - overlap

    return chunks