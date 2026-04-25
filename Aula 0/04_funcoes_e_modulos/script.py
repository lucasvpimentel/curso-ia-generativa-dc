# script.py - Exemplos do Módulo 4

# --- 1. FUNÇÃO SIMPLES (Ação) ---
def mostrar_aviso_api():
    print("--- AVISO DO SISTEMA ---")
    print("Conectando aos servidores da IA...")
    print("------------------------\n")

# --- 2. FUNÇÃO COM PARÂMETRO (Personalização) ---
def saudar_agente(nome_ia, versao):
    print(f"Agente {nome_ia} (v{versao}) está ONLINE.\n")

# --- 3. FUNÇÃO COM RETORNO (Cálculo/Processamento) ---
def formatar_prompt(usuario, pedido):
    """
    Simula a criação de um prompt estruturado para uma API.
    """
    template = f"Usuário: {usuario}\nPedido: {pedido}\nResposta da IA: "
    return template

# --- EXECUTANDO AS FUNÇÕES ---
if __name__ == "__main__":
    # Chamando a função simples
    mostrar_aviso_api()
    
    # Chamando com argumentos
    saudar_agente("CyberMind", "2.0")
    
    # Usando o retorno da função
    meu_prompt = formatar_prompt("Ana", "Explique o que é uma função.")
    print("PROMPT GERADO:")
    print(meu_prompt)
