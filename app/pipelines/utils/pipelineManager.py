from transformers import pipeline, AutoTokenizer
import torch


def get_device():
    return 0 if torch.cuda.is_available() else -1


class PipelineManager:
    def __init__(self, device: int = None, models: dict = None):
        self.device = get_device() if device is None else device
        self.models = models or {
            "summarization": "sshleifer/distilbart-cnn-12-6",
            "argumentation": "google/flan-t5-base",
            "story_points": "sshleifer/distilbart-cnn-12-6",
            "translation": "Helsinki-NLP/opus-mt-mul-en",
        }
        self._pipes = {}
        self._tokenizers = {}

    def get_tokenizer(self, task_name: str):
        model_name = self.models[task_name]
        if model_name not in self._tokenizers:
            self._tokenizers[model_name] = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        return self._tokenizers[model_name]

    def get_pipeline(self, task_name: str):
        if task_name in self._pipes:
            return self._pipes[task_name]
        model_name = self.models[task_name]

        if task_name == "summarization":
            p = pipeline("summarization", model=model_name, device=self.device)
        else:
            try:
                p = pipeline("text2text-generation", model=model_name, device=self.device)
            except Exception:
                p = pipeline("text-generation", model=model_name, device=self.device)
        self._pipes[task_name] = p
        return p