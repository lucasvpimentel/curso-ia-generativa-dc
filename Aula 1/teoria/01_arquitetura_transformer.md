# 🏗️ Arquitetura Transformer: O Motor da GenAI

A arquitetura Transformer, apresentada em 2017, revolucionou o Processamento de Linguagem Natural (NLP) ao introduzir o mecanismo de **Atenção**.

## 🧐 O Mecanismo de Self-Attention

Diferente das redes neurais antigas que liam uma frase palavra por palavra, o Transformer olha para a frase inteira de uma vez. O *Self-Attention* permite que o modelo entenda a relação entre palavras distantes.

### O Cálculo: Query, Key e Value (Q, K, V)

Imagine que você está em uma biblioteca:
*   **Query (Q):** É o que você está procurando (o termo de busca).
*   **Key (K):** É a etiqueta na lombada do livro (o índice).
*   **Value (V):** É o conteúdo dentro do livro (a informação real).

**O processo técnico:**
1.  O modelo calcula um **score de similaridade** entre o vetor `Query` de uma palavra e os vetores `Key` de todas as outras palavras da frase.
2.  Esse score passa por uma função `Softmax` para gerar pesos (probabilidades) que somam 1.
3.  O resultado final é uma soma ponderada dos vetores `Value`, onde as palavras mais "relevantes" para o contexto recebem mais peso.

## 🚀 Multi-Head Attention

Em vez de calcular a atenção apenas uma vez, o Transformer usa múltiplas "cabeças" (Multi-Head). Isso permite que o modelo aprenda diferentes tipos de relações simultaneamente: uma cabeça pode focar na gramática, outra no contexto histórico e outra no sentimento da frase.

---
*Referência Principal: Vaswani, A. et al. (2017). [Attention Is All You Need](https://arxiv.org/abs/1706.03762).*
