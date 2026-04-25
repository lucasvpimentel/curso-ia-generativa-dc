# SOLUÇÃO - EXERCÍCIO 3: O Histórico de Conversa (Listas de Dicionários)

# 1. Criando a lista vazia
historico_chat = []

# 2. Adicionando mensagem do sistema
historico_chat.append({
    "role": "system",
    "content": "Você é um assistente prestativo."
})

# 3. Adicionando mensagem do usuário
historico_chat.append({
    "role": "user",
    "content": "Qual é a capital do Brasil?"
})

# 4. Percorrendo com loop for
print("--- Histórico de Conversa ---")
for mensagem in historico_chat:
    print(f"{mensagem['role']} diz: {mensagem['content']}")

print("\n💡 Dica Mestra: Quando você for aprender a conectar com modelos do Hugging Face,")
print("é exatamente essa lista 'historico_chat' que você enviará para eles!")
