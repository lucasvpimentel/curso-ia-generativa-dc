import os
from openai import OpenAI

# Exemplo Prático 1: Parâmetros e Estruturas Básicas
# Requer: pip install openai
# Exige configuração de variável de ambiente: export OPENAI_API_KEY="sk-..."

# Inicializa o cliente (ele busca a chave na variável de ambiente automaticamente)
client = OpenAI()

def testar_temperatura(prompt_usuario, temperatura):
    print(f"\n--- Testando com Temperatura: {temperatura} ---")
    
    # 1. Estruturando o Prompt com Role Prompting via 'system'
    mensagens = [
        {
            "role": "system", 
            "content": "Você é um poeta renascentista extremamente dramático e prolixo."
        },
        {
            "role": "user", 
            "content": prompt_usuario
        }
    ]
    
    # 2. Chamada à API controlando Parâmetros
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        temperature=temperatura,
        max_tokens=150, # Limitando o uso de tokens de saída
    )
    
    resposta_texto = response.choices[0].message.content
    uso_tokens = response.usage
    
    print(f"Resposta:\n{resposta_texto}\n")
    print(f"Tokens Usados: {uso_tokens.total_tokens} (Entrada: {uso_tokens.prompt_tokens}, Saída: {uso_tokens.completion_tokens})")

if __name__ == "__main__":
    prompt = "Diga que está chovendo lá fora."
    
    # Temperatura baixa = Resposta direta, previsível (mesmo com a persona dramática)
    testar_temperatura(prompt, temperatura=0.1)
    
    # Temperatura alta = Resposta extremamente criativa e variada
    testar_temperatura(prompt, temperatura=1.2)
