# 01_fundamentos/script.py

# --- 1. DECLARANDO VARIÁVEIS ---
# Python é inteligente: ele descobre o tipo do dado sozinho!
nome_do_curso = "Python para IA Generativa"  # str (string/texto)
versao = 1                                  # int (inteiro)
preco = 0.0                                 # float (decimal)
gratuito = True                             # bool (booleano)

print("--- Variáveis Iniciais ---")
print(f"Curso: {nome_do_curso}")
print(f"Versão: {versao}")
print(f"É gratuito? {gratuito}")

# --- 2. CONVERSÃO DE TIPOS ---
# Às vezes precisamos mudar o tipo do "ingrediente"
numero_em_texto = "42"
numero_real = int(numero_em_texto)  # Transforma texto em número inteiro
texto_novamente = str(numero_real)  # Transforma número em texto novamente

print("\n--- Conversão ---")
print(f"O dobro de {numero_real} é {numero_real * 2}")

# --- 3. F-STRINGS (O segredo dos Prompts) ---
# f-strings permitem colocar variáveis dentro de um texto de forma fácil
usuario = "Explorador"
tema_interesse = "Arquitetura Barroca"
estilo_ia = "Poeta"

# Montando um prompt dinâmico!
prompt_base = f"Atue como um {estilo_ia} e descreva o que você sabe sobre {tema_interesse}."

print("\n--- Prompt Gerado ---")
print(prompt_base)

# Dica: Note o 'f' antes das aspas iniciais. Isso avisa ao Python 
# que o que estiver entre chaves { } deve ser substituído pelo valor da variável.
