# script.py - Exemplos do Módulo 2

def mostrar_menu():
    print("--- Menu do Agente de IA ---")
    print("1. Analisar dados de texto")
    print("2. Gerar relatório de tokens")
    print("3. Sair")
    
    # Exemplo de Condicional (if/elif/else)
    opcao = input("Escolha uma opção (1/2/3): ")
    
    if opcao == '1':
        print("Opção 1 escolhida: Iniciando análise de sentimentos...")
    elif opcao == '2':
        print("Opção 2 escolhida: Calculando gasto de créditos da API...")
    elif opcao == '3':
        print("Opção 3 escolhida: Encerrando o agente. Até logo!")
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

def repeticao_frases():
    print("\n--- Tarefa Repetitiva de Processamento ---")
    frase = "Processando bloco de texto..."
    
    # Exemplo de Loop (for)
    # O range(3) faz o loop rodar 3 vezes
    for i in range(3):
        print(f"Ação {i+1}: {frase}")

if __name__ == "__main__":
    mostrar_menu()
    repeticao_frases()
