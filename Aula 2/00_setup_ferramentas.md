# Guia de Instalação: Ambiente de IA Generativa (2026)

Para configurar seu ambiente de desenvolvimento de agentes e engenharia de prompt, siga as instruções abaixo para instalar o Python, o Antigravity IDE e a Gemini CLI.

---

## 1. Instalando o Python

O Python é essencial para rodar scripts de automação e utilizar bibliotecas de IA.

1.  **Download:** Acesse [python.org](https://www.python.org/downloads/) e baixe a versão estável mais recente.
2.  **Instalação (Windows):**
    *   Execute o instalador `.exe`.
    *   **IMPORTANTE:** Marque a opção **"Add Python to PATH"**.
3.  **Verificação:** No terminal, digite `python --version`.

---

## 2. Instalando o Antigravity IDE (.exe)

O Antigravity é o ambiente de desenvolvimento (IDE) oficial focado em agentes autônomos e integração profunda com o ecossistema Gemini.

1.  **Download:** Acesse o portal oficial [antigravity.google/download](https://antigravity.google/download).
2.  **Instalador:** Baixe o arquivo `AntigravitySetup.exe` para Windows.
3.  **Execução:** Siga o assistente de instalação. Certifique-se de permitir que o instalador adicione os binários (`agy`) ao seu PATH.
4.  **Autenticação:** Ao abrir o Antigravity pela primeira vez, faça login com sua conta Google para habilitar os recursos de "Cérebro" (Brain) e sincronização de tarefas.

---

## 3. Instalando o Node.js e npm

O **npm** (Node Package Manager) é necessário para instalar a Gemini CLI e outras ferramentas de automação. Ele vem incluído no instalador do Node.js.

1.  **Download:** Acesse [nodejs.org](https://nodejs.org/) e baixe a versão **LTS** (Long Term Support).
2.  **Instalação:**
    *   Execute o instalador `.msi`.
    *   Aceite as configurações padrão, garantindo que a opção de adicionar ao PATH esteja marcada.
3.  **Verificação:** No terminal, digite:
    ```bash
    node -v
    npm -v
    ```

---

## 4. Instalando a Gemini CLI (npm)

A Gemini CLI permite orquestrar tarefas diretamente do terminal e integrar-se ao Antigravity.

1.  **Pré-requisito:** Node.js e npm instalados (passo anterior).
2.  **Comando de Instalação:**
    ```bash
    npm install -g @google/gemini-cli
    ```
3.  **Sincronização:** Para conectar a CLI ao seu Antigravity IDE, use:
    ```bash
    gemini auth login
    ```

---

## Resumo dos Comandos e Ferramentas

| Ferramenta | Método | Comando de Verificação |
| :--- | :--- | :--- |
| **Python** | Instalador .exe | `python --version` |
| **Antigravity IDE** | Instalador .exe | `agy --version` |
| **Node.js / npm** | Instalador .msi | `node -v` / `npm -v` |
| **Gemini CLI** | `npm` | `gemini --version` |

---
**Nota:** Se o comando `agy` não funcionar após a instalação, reinicie seu terminal para atualizar as variáveis de ambiente.
