# script.py - Exemplos do Módulo 3

# --- 1. TRABALHANDO COM LISTAS ---
print("--- Manipulando Listas ---")
ferramentas_ia = ["ChatGPT", "Gemini", "Claude"]

# Adicionando um item
ferramentas_ia.append("Midjourney")

# Removendo um item
ferramentas_ia.remove("ChatGPT")

# Acessando por índice
print(f"Segunda ferramenta na lista: {ferramentas_ia[1]}")
print(f"Lista completa: {ferramentas_ia}\n")


# --- 2. TRABALHANDO COM DICIONÁRIOS ---
print("--- Manipulando Dicionários ---")
# Estrutura típica de uma mensagem de IA
mensagem = {
    "usuario": "Carlos",
    "prompt": "Crie um resumo sobre Python.",
    "tokens": 45
}

# Acessando valores pela chave
print(f"Usuário: {mensagem['usuario']}")
print(f"Mensagem enviada: {mensagem['prompt']}")

# Alterando um valor
mensagem["tokens"] = 50
print(f"Dicionário atualizado: {mensagem}\n")


# --- 3. LISTA DE DICIONÁRIOS (O Coração da IA) ---
print("--- Histórico de Conversa (Contexto) ---")
conversa = [
    {"role": "system", "content": "Você é um assistente de código."},
    {"role": "user", "content": "Como fazer um loop em Python?"},
    {"role": "assistant", "content": "Você pode usar o comando 'for'..."}
]

# Percorrendo a conversa
for msg in conversa:
    print(f"[{msg['role'].upper()}]: {msg['content']}")
