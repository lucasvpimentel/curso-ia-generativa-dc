# exercises.py - Exercícios do Módulo 5
import json

# DESAFIO 1: O Pacote de Envio
# Crie um dicionário chamado 'mensagem_sistema' com:
# - 'role': 'system'
# - 'content': 'Você é um poeta digital'
# Converta esse dicionário para uma string JSON e imprima.
def exercicio_enviar():
    print("--- Exercício 1: Enviar JSON ---")
    mensagem_sistema = {
        "role": "system",
        "content": "Você é um poeta digital"
    }
    json_texto = json.dumps(mensagem_sistema)
    print(json_texto)

# DESAFIO 2: Decifrando a IA
# Dada a string JSON abaixo (resposta de uma IA), converta para dicionário
# e imprima apenas o conteúdo da chave 'resposta'.
def exercicio_receber():
    print("\n--- Exercício 2: Receber JSON ---")
    resposta_json = '{"id": "chat-456", "resposta": "O sol é uma estrela.", "tokens": 12}'
    
    # Escreva o código de conversão aqui
    dados = json.loads(resposta_json)
    print(f"A IA disse: {dados['resposta']}")

if __name__ == "__main__":
    exercicio_enviar()
    exercicio_receber()
