"""
🚀 Script: Predição do Próximo Token (Versão Comunicativa)
Demonstração de como modelos de linguagem prevêem a próxima palavra.
"""

import os
import warnings
import logging
from transformers import pipeline, set_seed

# --- Configuração para Silenciar Logs Técnicos ---
# 1. Silencia avisos do Python (como os de depreciação)
warnings.filterwarnings("ignore")
# 2. Silencia logs internos da biblioteca Transformers
logging.getLogger("transformers").setLevel(logging.ERROR)
# 3. Silencia logs do sistema de cache do Hugging Face
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3" 
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

def gerar_texto(prompt):
    print("\n" + "="*40)
    print("🤖 IA GENERATIVA EM AÇÃO")
    print("="*40)
    print(f"📌 Seu prompt: '{prompt}'")
    print("\n⏳ Pensando na continuação... (Carregando modelo)")

    try:
        # Carregamos o modelo de forma simplificada
        gerador = pipeline('text-generation', model='gpt2', device=-1) # device=-1 força uso de CPU
        
        # Semente para resultados consistentes
        set_seed(42)

        # Geração do texto:
        # Ajustamos os parâmetros para evitar conflitos de 'max_length'
        resultado = gerador(
            prompt, 
            max_new_tokens=50,    # Gera até 50 novas palavras além do seu prompt
            num_return_sequences=1, 
            pad_token_id=50256,   # Define o token de parada explicitamente (evita avisos)
            do_sample=True,       # Permite criatividade na escolha das palavras
            top_k=50,             # Filtra as 50 palavras mais prováveis
            top_p=0.95            # Melhora a coerência do texto
        )

        print("\n✨ TEXTO GERADO:")
        print("-" * 40)
        print(resultado[0]['generated_text'])
        print("-" * 40)
        print("\n✅ Processo concluído com sucesso!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    print("Bem-vindo ao Simulador de IA Generativa!")
    try:
        entrada = input("Digite o início de uma frase (em inglês): ").strip()
    except EOFError:
        entrada = ""
        
    if not entrada:
        entrada = "Artificial Intelligence is the"
    
    gerar_texto(entrada)
