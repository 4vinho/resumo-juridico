# API Jurídica com Hugging Face

Esta é uma API de processamento de linguagem natural (PLN) para textos jurídicos. A API recebe um texto em qualquer idioma, o traduz para o inglês, realiza uma série de tarefas de PLN e, em seguida, traduz os resultados para o idioma de saída desejado.

## Funcionalidades

A API oferece as seguintes funcionalidades:

* **Resumo de texto:** Gera um resumo do texto de entrada.
* **Geração de argumentação:** Cria uma argumentação com base no texto de entrada.
* **Extração de pontos principais:** Extrai os pontos mais importantes do texto de entrada.
* **Tradução:** Traduz o texto de entrada e os resultados para o idioma desejado.

## Como usar

Para usar a API, envie uma requisição POST para o endpoint `/processar` com o seguinte corpo JSON:

```json
{
  "texto": "O seu texto jurídico aqui.",
  "outLanguage": "pt"
}
```

* `texto`: O texto jurídico a ser processado.
* `outLanguage`: O idioma de saída desejado para os resultados (por exemplo, "pt" para português, "es" para espanhol, etc.).

## Exemplo de resposta

A API retornará um objeto JSON com os resultados do processamento:

```json
{
  "resumo": "O resumo do seu texto.",
  "argumentacao": "A argumentação gerada a partir do seu texto.",
  "pontos_principais": [
    "Ponto principal 1.",
    "Ponto principal 2.",
    "Ponto principal 3."
  ],
  "resumo_traduzido": "O resumo do seu texto no idioma de saída."
}
```

## Tecnologias utilizadas

* **FastAPI:** Framework web para a construção da API.
* **Hugging Face Transformers:** Biblioteca para as tarefas de PLN.
* **Uvicorn:** Servidor ASGI para a execução da API.
