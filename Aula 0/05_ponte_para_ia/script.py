# script.py - Exemplos do Módulo 5
import json # Importamos a ferramenta nativa do Python

# --- 1. CONVERTENDO PYTHON PARA JSON (Enviando dados) ---
dados_usuario = {
    "nome": "Bia",
    "interesses": ["IA", "Artes", "Cozinha"],
    "assinante": True
}

# dumps = Dump String (Despejar como texto)
texto_json = json.dumps(dados_usuario, indent=4, ensure_ascii=False)

print("--- OBJETO CONVERTIDO PARA JSON (TEXTO) ---")
print(texto_json)
print(f"Tipo da variável: {type(texto_json)}\n")


# --- 2. CONVERTENDO JSON PARA PYTHON (Recebendo dados) ---
# Imagine que este texto veio da API de uma IA
resposta_ia_texto = '{"status": "ok", "mensagem": "Receita de bolo gerada!", "id": 123}'

# loads = Load String (Carregar texto)
dados_recebidos = json.loads(resposta_ia_texto)

print("--- JSON CONVERTIDO PARA DICIONÁRIO PYTHON ---")
print(f"Mensagem da IA: {dados_recebidos['mensagem']}")
print(f"ID da resposta: {dados_recebidos['id']}")
print(f"Tipo da variável: {type(dados_recebidos)}")
