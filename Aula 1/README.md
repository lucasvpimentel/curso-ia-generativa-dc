# 🚀 Fundamentos de IA Generativa e LLMs

Bem-vindo ao repositório de estudos práticos sobre IA Generativa! Este projeto foi criado para servir como um guia sólido para desenvolvedores e entusiastas que desejam entender o que acontece "sob o capô" dos grandes modelos de linguagem (LLMs).

## 🧠 IA Tradicional vs. IA Generativa

Para entender a revolução atual, precisamos distinguir dois paradigmas:

*   **IA Tradicional (Discriminativa):** Focada em **classificar** ou **prever**. Ela olha para os dados e diz: "Isto é um gato" ou "Este imóvel custará X". Ela aprende as fronteiras de decisão entre categorias.
*   **IA Generativa:** Focada em **criar**. Em vez de apenas rotular, ela aprende a distribuição estatística dos dados para gerar novos exemplos que poderiam pertencer ao conjunto original. Ela não diz apenas se é um gato; ela cria a imagem de um gato que nunca existiu.

## ⏳ Linha do Tempo Evolutiva

1.  **1966 - ELIZA:** O primeiro chatbot, baseado em regras rígidas de substituição de palavras e busca de padrões.
2.  **Anos 90 - LSTMs (Long Short-Term Memory):** Introdução de redes neurais recorrentes capazes de "lembrar" sequências mais longas, fundamentais para tradução e fala.
3.  **2017 - O Marco (Transformer):** Publicação do artigo *"Attention Is All You Need"*. Surge a arquitetura que eliminou a necessidade de recorrência, permitindo o processamento paralelo e o mecanismo de **Self-Attention**.
4.  **Hoje - A Era dos LLMs:** Modelos com bilhões de parâmetros (GPT-4, Llama 3, Claude) que demonstram capacidades emergentes de raciocínio e síntese de conhecimento.

## 🛠️ Setup do Projeto

Para rodar os exemplos deste repositório, recomendamos o uso de um ambiente virtual Python (Conda ou venv).

```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente (Windows)
.\.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```
