# exercises.py - Exercícios do Módulo 2

# DESAFIO 1: Validador de Tamanho de Prompt
def validar_prompt():
    """
    Peça ao usuário para digitar um prompt de IA.
    Se o prompt tiver menos de 20 caracteres, imprima: "Prompt muito vago, dê mais contexto."
    Se tiver entre 20 e 100 caracteres, imprima: "Prompt aceitável."
    Se tiver mais de 100 caracteres, imprima: "Prompt detalhado! Excelente."
    Dica: use len(prompt) para contar os caracteres.
    """
    prompt = input("Digite seu prompt para a IA: ")
    
    # Escreva sua lógica de if/elif/else aqui
    if len(prompt) < 20:
        print("Prompt muito vago, dê mais contexto.")
    elif len(prompt) <= 100:
        print("Prompt aceitável.")
    else:
        print("Prompt detalhado! Excelente.")

# DESAFIO 2: Contador de Tokens (Simulado)
def contador_regressivo():
    """
    Use um loop 'for' para imprimir uma contagem regressiva de 5 até 1.
    No final, imprima: "Processamento concluído!"
    """
    print("\nIniciando contagem de processamento:")
    # Escreva seu loop aqui
    for i in range(5, 0, -1):
        print(i)
    print("Processamento concluído!")

if __name__ == "__main__":
    print("--- Exercícios do Módulo 2 ---")
    validar_prompt()
    contador_regressivo()
