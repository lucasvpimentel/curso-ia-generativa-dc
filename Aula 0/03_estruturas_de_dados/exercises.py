# exercises.py - Exercícios do Módulo 3

# DESAFIO 1: Organizando sua Mochila de IA
# 1. Crie uma lista chamada 'meus_modelos' com 3 nomes de IAs.
# 2. Adicione uma nova IA à lista.
# 3. Remova a primeira IA da lista.
# 4. Imprima a lista final.
def exercicio_listas():
    print("--- Exercício 1: Listas ---")
    # Escreva seu código aqui
    meus_modelos = ["GPT-3.5", "Llama 2", "Stable Diffusion"]
    meus_modelos.append("Gemini Pro")
    meus_modelos.pop(0) # Remove o primeiro item
    print(meus_modelos)

# DESAFIO 2: O Perfil do Robô
# 1. Crie um dicionário chamado 'robo' com: nome, função e bateria (0 a 100).
# 2. Imprima apenas a função do robô.
# 3. Atualize a bateria para 100.
# 4. Imprima o dicionário completo.
def exercicio_dicionarios():
    print("\n--- Exercício 2: Dicionários ---")
    # Escreva seu código aqui
    robo = {
        "nome": "Alpha",
        "funcao": "Exploração espacial",
        "bateria": 75
    }
    print(f"Função do robô: {robo['funcao']}")
    robo["bateria"] = 100
    print(robo)

if __name__ == "__main__":
    exercicio_listas()
    exercicio_dicionarios()
