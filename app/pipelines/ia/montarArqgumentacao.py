from app.pipelines.utils.pipelineManager import PipelineManager

def defend_point(claim: str,
                 context: str = None,
                 manager: PipelineManager = None,
                 n_arguments: int = 3,
                 include_counter_arguments: bool = True,
                 language: str = "pt") -> str:
    if manager is None:
        raise ValueError("Forneça um PipelineManager (manager) com um modelo para 'argumentation'.")
    pipe = manager.get_pipeline("argumentation")

    if language.startswith("pt"):
        prompt = f"Defenda a seguinte afirmação de forma clara e estruturada, providencie {n_arguments} argumentos com evidências e um exemplo prático:\n\nAfirmação: {claim}\n"
        if context:
            prompt += f"\nContexto / Evidências:\n{context}\n"
        prompt += "\nFormato: 1) Título do argumento - explicação - exemplo.\n"
        if include_counter_arguments:
            prompt += "\nAo final, liste 2 contra-argumentos possíveis e rebata-os sucintamente.\n"
    else:
        prompt = f"Defend the following claim, provide {n_arguments} structured arguments with evidence and an example:\n\nClaim: {claim}\n"
        if context:
            prompt += f"\nContext / Evidence:\n{context}\n"
        prompt += "\nFormat: 1) Argument title - explanation - example.\n"
        if include_counter_arguments:
            prompt += "\nFinally, list 2 potential counter-arguments and rebut them briefly.\n"

    out = pipe(prompt, max_length=512, truncation=True)
    text = out[0]['generated_text'] if isinstance(out, list) and 'generated_text' in out[0] else (out[0].get('generated_text') if isinstance(out[0], dict) else str(out))
    return text.strip()
