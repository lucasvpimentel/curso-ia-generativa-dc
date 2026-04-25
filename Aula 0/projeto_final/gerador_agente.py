import json

def construir_agente():
    """
    Função principal que integra todos os conhecimentos do curso.
    """
    print("="*40)
    print("🤖 BEM-VINDO AO FORJADOR DE AGENTES de IA 🤖")
    print("="*40)
    print("Vamos criar a identidade do seu novo assistente digital.\n")

    # 1. Coletando dados básicos (Input e Variáveis)
    nome = input("Qual será o nome do agente? ")
    especialidade = input(f"No que o {nome} será especialista? ")
    
    # 2. Lógica de Decisão (Condicionais)
    print("\nEscolha o Tom de Voz do seu agente:")
    print("1. Formal e Profissional")
    print("2. Descontraído e Amigável")
    escolha = input("Sua escolha (1 ou 2): ")

    if escolha == '1':
        tom = "Formal e Profissional"
        temperatura = 0.2
    else:
        tom = "Descontraído e Amigável"
        temperatura = 0.8 # Mais criatividade
    
    # 3. Construção do Prompt (F-Strings e Manipulação de Texto)
    system_prompt = (
        f"Você é {nome}, um especialista em {especialidade}. "
        f"Sua comunicação deve ser sempre {tom}. "
        "Responda de forma clara e objetiva."
    )

    # 4. Organizando a Estrutura (Dicionário)
    configuracao_agente = {
        "agente_nome": nome,
        "modelo_base": "gpt2",
        "parametros": {
            "temperature": temperatura,
            "top_p": 0.95
        },
        "instrucoes": {
            "role": "system",
            "content": system_prompt
        }
    }

    # 5. Exportando para o Mundo Real (JSON)
    pacote_json = json.dumps(configuracao_agente, indent=4, ensure_ascii=False)

    print("\n" + "-"*40)
    print("✨ AGENTE FORJADO COM SUCESSO! ✨")
    print("-"*40)
    print("\nEste é o pacote JSON pronto para sua API:")
    print(pacote_json)
    print("\n" + "="*40)

if __name__ == "__main__":
    construir_agente()
