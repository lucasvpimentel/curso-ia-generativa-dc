"""
🚀 Script: Predição do Próximo Token
Este script demonstra o conceito de Causal Language Modeling (LLMs auto-regressivas).
O objetivo é mostrar como modelos como o GPT-2 prevêem a próxima palavra com base na probabilidade.
"""

from transformers import pipeline, set_seed

def gerar_texto(prompt, max_tokens=30):
    """
    Função que carrega o modelo e gera a continuação de um texto.
    """
    print(f"\n--- Iniciando Geração ---")
    print(f"Prompt Inicial: '{prompt}'\n")

    # O 'pipeline' é a forma mais simples de usar modelos do Hugging Face.
    # 'text-generation' configura o modelo para prever tokens subsequentes.
    # O modelo 'gpt2' é leve (aprox. 500MB) e ideal para demonstrações rápidas.
    print("Aguarde: Carregando modelo GPT-2...")
    gerador = pipeline('text-generation', model='gpt2')
    
    # Definimos uma seed (semente) para que o resultado seja o mesmo em todas as execuções.
    # Isso é importante em contextos educacionais para garantir reprodutibilidade.
    set_seed(42)

    # Execução da geração:
    # - max_length: tamanho máximo total da sequência (prompt + geração).
    # - num_return_sequences: quantas variantes de resposta o modelo deve criar.
    # - truncation=True: garante que o texto não ultrapasse os limites do modelo.
    resultado = gerador(prompt, max_length=max_tokens, num_return_sequences=1, truncation=True)

    print("Texto Gerado:")
    # O resultado vem como uma lista de dicionários. Acessamos a chave 'generated_text'.
    print(resultado[0]['generated_text'])
    print(f"-------------------------\n")

if __name__ == "__main__":
    # Interface simples via terminal para interação do aluno.
    # Se o usuário apenas der Enter, usamos uma frase padrão.
    try:
        entrada = input("Digite o início de uma frase em inglês (ou Enter para o padrão): ")
    except EOFError:
        entrada = ""
        
    if not entrada:
        entrada = "The future of Artificial Intelligence is"
    
    gerar_texto(entrada)
