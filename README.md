# API Jurídica com Hugging Face

  Resumindo, este projeto fornece um conjunto poderoso de ferramentas para
  trabalhar com textos jurídicos. Você pode usá-lo para construir aplicações que
  ajudem os profissionais da área jurídica a serem mais eficientes e eficazes em
  seu trabalho. Com a maquina correta pode ser elevado a outro nivel utilizando melhores ML.

  Este projeto é uma API de PLN Jurídica que usa a biblioteca Hugging Face
  Transformers para realizar várias tarefas de processamento de linguagem natural
  em textos jurídicos.

  Como funciona:


   1. API Web: O projeto é uma API web construída com FastAPI. Isso significa que
      você pode interagir com ela enviando requisições HTTP.
   2. Entrada: Você fornece um texto jurídico em qualquer idioma e especifica o
      idioma de saída desejado.
   3. Processamento: A API recebe seu texto, o traduz para o inglês e, em seguida,
      executa as seguintes tarefas:
       * Resumo: Gera um resumo do texto.
       * Geração de Argumentação: Cria um argumento jurídico com base no texto.
       * Extração de Pontos Principais: Extrai os pontos mais importantes do texto.        
   4. Saída: A API então traduz os resultados dessas tarefas para o idioma de saída        
      que você especificou e os retorna para você em formato JSON.

  Usos potenciais:


   * Pesquisa Jurídica: Advogados e profissionais da área jurídica podem usar esta
     API para resumir e entender rapidamente grandes documentos legais,
     economizando tempo e esforço.
   * Análise de Casos: A API pode ajudar advogados a analisar casos, extraindo os
     pontos principais e gerando argumentos jurídicos.
   * Educação Jurídica: Estudantes de direito podem usar esta API para aprender
     sobre argumentação e análise jurídica.
   * Automação de Documentos: A API pode ser integrada a outras aplicações para
     automatizar o processo de resumo e análise de documentos jurídicos.
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
