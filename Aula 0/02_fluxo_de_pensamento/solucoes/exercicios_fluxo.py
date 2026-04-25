# SOLUÇÃO - Módulo 2

# Exercício 1
prompt = input("Digite seu prompt: ")
if len(prompt) == 0:
    print("Prompt inválido")
elif len(prompt) < 10:
    print("Prompt muito curto")
else:
    print("Prompt enviado!")

# Exercício 2
for i in range(5):
    print(f"({i+1}) Gerando resposta IA...")
