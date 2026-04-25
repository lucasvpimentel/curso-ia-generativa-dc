# IA Generativa — Digital College

Repositório de estudos do curso **IA Generativa** da Digital College.  
Cada aula possui sua própria pasta com notebooks, scripts, teoria e dependências.

---

## Índice de Aulas

| # | Aula | Tópicos Principais | Status |
|---|------|--------------------|--------|
| 1 | [Fundamentos de LLMs](./Aula%201/README.md) | Arquitetura Transformer, BERT, Embeddings, Self-Attention | Concluída |

> **Novas aulas serão adicionadas aqui à medida que o curso avança.**

---

## Estrutura do Repositório

```
IA Generativa/
│
├── Aula 1/
│   ├── notebooks/          # Notebooks Jupyter práticos
│   ├── scripts/            # Scripts Python standalone
│   ├── teoria/             # Resumos teóricos em Markdown
│   ├── requirements.txt    # Dependências da aula
│   └── README.md           # Detalhes da aula
│
└── README.md               # Este arquivo
```

---

## Como Usar

### Pré-requisitos

- Python 3.9+
- Git

### Setup do Ambiente

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd "IA Generativa"

# 2. Entre na pasta da aula desejada
cd "Aula 1"

# 3. Crie e ative o ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Abra o Jupyter
jupyter notebook
```

---

## Conceitos Abordados

### Aula 1 — Fundamentos de LLMs
- Diferença entre **IA Tradicional (Discriminativa)** e **IA Generativa**
- Linha do tempo: ELIZA → LSTMs → **Transformer (2017)** → LLMs modernos
- Mecanismo de **Self-Attention** (Query, Key, Value)
- **Multi-Head Attention** e codificação posicional
- **BERT** e geração de embeddings
- Predição do próximo token na prática

---

## Stack Tecnológica

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace_Transformers-4.30+-FFD21E?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter&logoColor=white)

---

## Referências

- Vaswani, A. et al. (2017). [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762)
- [HuggingFace Transformers Docs](https://huggingface.co/docs/transformers)
- [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)

---

*Repositório atualizado continuamente durante o curso.*
