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

---

## 🏗️ Arquitetura Transformer: O Motor da GenAI

O grande diferencial do Transformer é o mecanismo de **Self-Attention** (Auto-Atenção), que permite ao modelo focar nas partes mais importantes de uma frase, independentemente da distância entre as palavras.

### O Mecanismo Q, K, V (Analogia da Biblioteca)
Para entender como o modelo "pensa" a relevância de cada termo, utilizamos a analogia de uma busca em biblioteca:
*   **Query (Q):** O que você está procurando (ex: "Qual o contexto desta palavra?").
*   **Key (K):** A etiqueta na lombada do livro (o índice que diz o que cada palavra oferece).
*   **Value (V):** O conteúdo do livro (a informação semântica real da palavra).

O modelo calcula a similaridade entre **Q** e **K** para decidir quanto de **V** ele deve "absorver" de cada palavra da frase para formar o contexto.

---

## 🛠️ Guia de Execução Passo a Passo

Siga estas instruções para configurar o ambiente e rodar os códigos de demonstração.

### 0. Clonar apenas a Aula 1 (opcional)

Se quiser baixar somente esta pasta, sem o restante do repositório, use o **sparse-checkout**:

```bash
# 1. Clone o repositório sem baixar os arquivos ainda
git clone --filter=blob:none --no-checkout https://github.com/lucasvpimentel/curso-ia-generativa-dc ia-generativa
cd ia-generativa

# 2. Ative o sparse-checkout e defina a pasta desejada
git sparse-checkout init --cone
git sparse-checkout set "Aula 1"

# 3. Finalize o checkout
git checkout main
```

### 1. Configuração do Ambiente (Setup)

No terminal, dentro da pasta raiz do projeto, execute:

```bash
# 1. Criar o ambiente virtual (isolamento de bibliotecas)
python -m venv .venv

# 2. Ativar o ambiente virtual (Windows)
.\.venv\Scripts\activate

# 3. Instalar as bibliotecas necessárias
pip install -r requirements.txt
```

---

### 2. Executando o Script de Geração (Predição de Próximo Token)

Este script demonstra como o modelo GPT-2 "completa" frases de forma probabilística.

```bash
# Com o ambiente ativado, execute:
python scripts/predicao_proximo_token.py
```

---

### 3. Executando o Notebook (Embeddings)

O notebook permite visualizar como as palavras são transformadas em vetores matemáticos usando o BERT.

**Opção A: No VS Code (Recomendado)**
1. Abra o arquivo `notebooks/01_bert_e_embeddings.ipynb`.
2. No canto superior direito, clique em **"Select Kernel"**.
3. Escolha **"Python Environments..."** e selecione o ambiente que aponta para o seu `.venv`.

**Opção B: Via Jupyter Lab (Navegador)**
```bash
jupyter lab
```

---

## 💡 Recomendações e Observações Importantes

1.  **Primeira Execução e Internet:** Tanto o script quanto o notebook fazem download de modelos da nuvem (Hugging Face) na primeira vez que são rodados.
2.  **Idioma dos Modelos:** O BERT e o GPT-2 utilizados nestes exemplos foram treinados majoritariamente em **inglês**.
3.  **Memória RAM:** Os modelos rodam tranquilamente em computadores modernos (consomem ~1.5GB de RAM) sem necessidade de GPU dedicada.

---

## 📚 Referências Teóricas e Científicas

*   **Transformer (Base):** Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762).
*   **BERT (Embeddings):** Devlin, J. et al. (2018). [*BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*](https://arxiv.org/abs/1810.04805).
*   **GPT-2 (Geração):** Radford, A. et al. (2019). [*Language Models are Unsupervised Multi-task Learners*](https://openai.com/blog/better-language-models/).
*   **Didática:** [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/).
