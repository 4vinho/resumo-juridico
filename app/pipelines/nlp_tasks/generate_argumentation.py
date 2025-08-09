from app.pipelines.utils.pipelineManager import PipelineManager


def generate_argumentation(claim: str,
                 context: str = None,
                 manager: PipelineManager = None,
                 n_arguments: int = 3,
                 include_counter_arguments: bool = True) -> str:
    if manager is None:
        raise ValueError("Forneça um PipelineManager (manager) com um modelo para 'argumentation'.")
    pipe = manager.get_pipeline("argumentation")

    prompt = f"Defend the following claim, provide {n_arguments} structured arguments with evidence and an example:\n\nClaim: {claim}\n"
    if context:
        prompt += f"\nContext / Evidence:\n{context}\n"
    prompt += "\nFormat: 1) Argument title - explanation - example.\n"
    if include_counter_arguments:
        prompt += "\nFinally, list 2 potential counter-arguments and rebut them briefly.\n"

    out = pipe(prompt, max_length=512, truncation=True)
    text = out[0]['generated_text'] if isinstance(out, list) and 'generated_text' in out[0] else (
        out[0].get('generated_text') if isinstance(out[0], dict) else str(out))

    return text.strip()


