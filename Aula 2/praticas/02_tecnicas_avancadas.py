from openai import OpenAI

# Exemplo Prático 2: Few-Shot e Chain of Thought
client = OpenAI()

def executar_prompt(mensagens):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        temperature=0.0 # Para lógica, usamos temp baixa
    )
    return response.choices[0].message.content

print("=== 1. Few-Shot Prompting ===")
# Ensinando o modelo a extrair informações em um formato JSON específico
prompt_few_shot = [
    {"role": "system", "content": "Você é um extrator de dados. Retorne apenas o formato solicitado."},
    # Exemplo 1
    {"role": "user", "content": "Texto: A Maria comprou um carro da Ford."},
    {"role": "assistant", "content": "Nome: Maria | Marca: Ford"},
    # Exemplo 2
    {"role": "user", "content": "Texto: Carlos foi trabalhar na filial da Microsoft em Seattle."},
    {"role": "assistant", "content": "Nome: Carlos | Empresa: Microsoft"},
    # Tarefa real
    {"role": "user", "content": "Texto: Ontem o Elon Musk anunciou novidades na Tesla."}
]

print("Saída Few-Shot:")
print(executar_prompt(prompt_few_shot))


print("\n=== 2. Zero-Shot Chain of Thought (CoT) ===")
# Forçando o raciocínio
pergunta_logica = """
João tem 3 maçãs. Ele ganha mais 2 da mãe. 
Depois ele corta cada maçã que tem pela metade. 
Ele come 3 metades. Quantas metades de maçã sobram?
"""

# Prompt sem CoT
prompt_sem_cot = [
    {"role": "user", "content": pergunta_logica}
]

# Prompt com CoT mágico
prompt_com_cot = [
    {"role": "user", "content": pergunta_logica + "\nVamos pensar passo a passo."}
]

print("\nResposta SEM CoT explícito (pode errar ou acertar por sorte):")
print(executar_prompt(prompt_sem_cot))

print("\nResposta COM CoT ('Vamos pensar passo a passo'):")
print(executar_prompt(prompt_com_cot))
