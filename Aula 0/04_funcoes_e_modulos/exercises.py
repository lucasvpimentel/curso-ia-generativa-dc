# exercises.py - Exercícios do Módulo 4

# DESAFIO 1: A Fábrica de Nomes
# Crie uma função chamada 'gerar_nome_robo' que recebe um nome e um número.
# Ela deve retornar uma string como: "Robo-Nome-Número"
# Exemplo: gerar_nome_robo("RX", 500) -> "Robo-RX-500"
def gerar_nome_robo(nome, numero):
    return f"Robo-{nome}-{numero}"

# DESAFIO 2: Calculadora de Custo de Tokens
# Crie uma função chamada 'calcular_custo' que recebe:
# - quantidade de tokens (int)
# - preço por token (float)
# A função deve retornar o valor total (tokens * preço).
def calcular_custo(tokens, preco):
    return tokens * preco

if __name__ == "__main__":
    print("--- Exercício 1: Fábrica de Nomes ---")
    resultado_nome = gerar_nome_robo("Alpha", 7)
    print(f"Nome gerado: {resultado_nome}")
    
    print("\n--- Exercício 2: Custo de Tokens ---")
    custo_total = calcular_custo(1000, 0.002)
    print(f"O custo total foi de: R$ {custo_total:.2f}")
