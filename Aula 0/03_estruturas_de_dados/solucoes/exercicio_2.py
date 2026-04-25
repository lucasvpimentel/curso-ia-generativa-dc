# SOLUÇÃO - EXERCÍCIO 2: Criando a Persona da IA (Dicionários)

# 1. Criando o dicionário
persona_ia = {
    "nome": "Sábio",
    "funcao": "Tirar dúvidas de Python",
    "temperatura": 0.5
}

# 2. Imprimindo apenas o nome
print(f"Nome da IA: {persona_ia['nome']}")

# 3. Alterando a temperatura
persona_ia["temperatura"] = 0.9

# 4. Adicionando nova chave
persona_ia["modelo"] = "gpt2"

# 5. Imprimindo dicionário completo
print("Perfil atualizado:", persona_ia)
