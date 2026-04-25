# Setup Base Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar a estrutura inicial do curso e o módulo de setup com tom de alquimia para iniciantes em Python para GenAI.

**Architecture:** Estrutura de pastas simples com arquivos README didáticos e scripts Python básicos comentados.

**Tech Stack:** Python 3, Markdown.

---

### Task 1: README Principal (O Mapa da Jornada)

**Files:**
- Create: `README.md`

- [ ] **Step 1: Escrever o README.md principal**

Conteúdo:
```markdown
# 🧙‍♂️ Python: Do Zero ao Prompt

Bem-vindo à **Jornada do Alquimista de Dados**! 

Este curso foi desenhado para quem nunca escreveu uma linha de código, mas deseja dominar o Python para criar o futuro com a Inteligência Artificial Generativa. Aqui, não apenas "programamos", mas transformamos lógica em magia.

## 🗺️ O Mapa da Jornada

Cada pasta neste repositório representa um novo nível de conhecimento no seu Grimório:

*   **[00_setup](./00_setup/)**: Preparando o seu Laboratório (Instalação e Primeiros Passos).
*   **01_fundamentos**: As Substâncias Básicas (Variáveis e Tipos).
*   **02_fluxo**: O Controle do Fogo (Condicionais e Laços).
*   **03_dados**: Os Caldeirões (Listas e Dicionários).
*   **04_funções**: As Fórmulas Sagradas (Reutilização de Código).
*   **05_ia_e_automacao**: A Grande Obra (Conectando com APIs de IA).

## 🧭 Como Navegar

1. Comece sempre pelo `README.md` de cada pasta.
2. Leia os comentários nos arquivos `.py` - eles são as explicações dos mestres.
3. Pratique os desafios propostos em `exercises.py`.

---
"O código é a matéria-prima. A lógica é a sua vontade. A IA é a centelha da criação."
```

### Task 2: README do Módulo 0 (O Setup)

**Files:**
- Create: `00_setup/README.md`

- [ ] **Step 1: Criar a pasta 00_setup**

Run: `mkdir 00_setup`

- [ ] **Step 2: Escrever o README.md do setup**

Conteúdo:
```markdown
# 🧪 Módulo 0: O Setup do Alquimista

Antes de criarmos poções complexas, precisamos preparar o nosso laboratório.

## 🛠️ Instalando o Python

O Python será a sua ferramenta principal. Siga os passos conforme o seu sistema:

### Windows
1. Vá para [python.org](https://www.python.org/downloads/windows/).
2. Baixe a versão estável mais recente.
3. **IMPORTANTE:** Durante a instalação, marque a caixa **"Add Python to PATH"**.

### Mac/Linux
1. Geralmente o Python já vem instalado.
2. Abra o terminal e digite `python3 --version`. Se aparecer uma versão (ex: 3.10.x), você está pronto!

## 🖥️ O Terminal (O Portal de Comandos)

O terminal é onde você falará diretamente com o computador.

1. No Windows, pesquise por **PowerShell** ou **Prompt de Comando**.
2. No Mac/Linux, abra o **Terminal**.

## 🚀 Rodando o Seu Primeiro Script

Para testar se o seu laboratório está pronto:
1. Abra o terminal na pasta deste módulo.
2. Digite: `python script.py` (ou `python3 script.py` no Mac/Linux).
```

### Task 3: O Primeiro Script (O Feitiço)

**Files:**
- Create: `00_setup/script.py`

- [ ] **Step 1: Criar o script.py**

Conteúdo:
```python
# Este é o seu primeiro comentário! Comentários começam com '#' e não são lidos pela máquina.
# Eles servem como notas para o Alquimista (você).

# A função 'print' é como o computador "fala".
# Tudo o que está dentro dos parênteses e entre aspas será mostrado na tela.
print("Olá, Mundo!")

# Explicação:
# print -> O comando para exibir algo.
# ( )   -> Os parênteses guardam o que será exibido.
# " "   -> As aspas dizem que isso é um texto puro (String).
```

- [ ] **Step 2: Verificar o script**

Run: `python "00_setup/script.py"`
Expected: `Olá, Mundo!`

### Task 4: Exercícios do Módulo 0

**Files:**
- Create: `00_setup/exercises.py`

- [ ] **Step 1: Criar o exercises.py**

Conteúdo:
```python
# 📜 DESAFIO DO APRENDIZ
# Agora é a sua vez de usar o caldeirão!

# 1. Altere a mensagem abaixo para: "Eu sou um Alquimista de Python!"
# 2. Salve o arquivo.
# 3. No terminal, rode o comando: python exercises.py

print("Mude este texto aqui!")

# DICA: Lembre-se de manter as aspas e os parênteses!
```

- [ ] **Step 2: Verificar o exercício**

Run: `python "00_setup/exercises.py"`
Output esperado após alteração: `Eu sou um Alquimista de Python!`
