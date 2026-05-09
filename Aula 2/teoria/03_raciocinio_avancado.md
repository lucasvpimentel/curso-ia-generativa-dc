# 3. Técnicas de Raciocínio Avançado

Para problemas complexos de lógica, matemática ou raciocínio em múltiplos passos, os modelos tendem a falhar se tentarem gerar a resposta final imediatamente. Estas técnicas forçam o modelo a pensar estruturadamente.

---

## 3.1 Chain of Thought (CoT) - Cadeia de Pensamentos

O *Chain of Thought* instrui o modelo a explicitar seu raciocínio passo a passo antes de dar a resposta final. Ao gerar os tokens intermediários do raciocínio, o modelo "dá tempo a si mesmo" para computar a lógica correta.

### Zero-shot CoT
A forma mais simples, descoberta por Kojima et al. (2022). Basta adicionar a frase mágica: **"Vamos pensar passo a passo."** (Let's think step by step).

**Exemplo:**
> Fui ao mercado com R$ 100. Comprei 3 maçãs por R$ 2 cada e 1 suco por R$ 15. Depois, encontrei meu amigo que me pagou os R$ 20 que me devia. Com quanto dinheiro fiquei?
> **Vamos pensar passo a passo.**

### Few-shot CoT
Combina Few-Shot com CoT. Você fornece exemplos de perguntas e respostas, mas a resposta no exemplo inclui o passo a passo da lógica.

**Exemplo:**
> Q: João tem 5 bolas. Ele compra 2 caixas com 3 bolas cada. Quantas ele tem agora?
> A: João começou com 5 bolas. 2 caixas de 3 bolas dão 6 bolas. 5 + 6 = 11. A resposta é 11.
>
> Q: Maria tinha 12 doces. Ela deu 4 para o irmão e depois dividiu o resto igualmente com sua amiga. Quantos doces Maria tem agora?
> A:

---

## 3.2 Self-Consistency (Auto-consistência)

Evolução do CoT. Modelos de linguagem são probabilísticos e podem errar no meio do raciocínio. A Auto-consistência funciona assim:
1. Você envia o mesmo prompt com CoT várias vezes (ex: 5 vezes) usando uma Temperatura > 0.
2. O modelo gerará 5 caminhos de raciocínio diferentes.
3. Você seleciona a resposta final por **voto da maioria** (qual resposta aparece na maioria das vezes).

*Aplicações:* Problemas matemáticos difíceis, lógica formal.

---

## 3.3 Tree of Thoughts (ToT) - Árvore de Pensamentos

Para tarefas muito complexas (como planejamento estratégico, jogos, escrita criativa longa), o modelo precisa explorar alternativas, olhar para frente (lookahead) e retroceder (backtrack).

O ToT estrutura o raciocínio como uma árvore:
- O modelo gera múltiplos "pensamentos" (ramos).
- O próprio modelo (ou outro prompt) avalia cada ramo ("Isso me aproxima do objetivo?").
- Ramos ruins são podados; ramos bons são expandidos para o próximo passo.

*Na prática:* Geralmente implementado via código (Python), fazendo múltiplas chamadas à API da LLM, estruturando a árvore de decisões.

---

## 3.4 ReAct (Reasoning and Acting)

ReAct combina raciocínio interno (Chain of Thought) com ações no mundo exterior. É o coração dos **Agentes de IA**.

O modelo entra em um loop contínuo de:
1. **Thought (Pensamento):** "O que eu preciso fazer agora?"
2. **Action (Ação):** "Vou chamar a ferramenta 'Busca no Google' com o termo X."
3. **Observation (Observação):** A resposta da ferramenta volta para o modelo.

**Exemplo de log do modelo usando ReAct:**
> *Pergunta:* Qual a idade da esposa de Leonardo DiCaprio em 2024?
> *Thought:* Preciso saber quem é a namorada/esposa atual do Leonardo DiCaprio. Vou pesquisar isso.
> *Action:* Busca_Google("Leonardo DiCaprio namorada 2024")
> *Observation:* [Resultados mostram que é Vittoria Ceretti, nascida em 1998]
> *Thought:* Agora sei que é Vittoria Ceretti. Preciso calcular a idade dela em 2024. 2024 - 1998 = 26.
> *Action:* Finish("Ela tem 26 anos.")

---

## 3.5 Meta-Prompting e Prompt Chaining

**Prompt Chaining:** Quebrar uma tarefa gigante em subtarefas sequenciais. A saída do Prompt A vira a entrada do Prompt B.
*Exemplo:* 
- Prompt 1: Extrai fatos do texto longo.
- Prompt 2: Pega os fatos do Prompt 1 e escreve um rascunho de e-mail.
- Prompt 3: Revisa o rascunho do Prompt 2 procurando erros gramaticais.

**Meta-Prompting:** Usar um LLM para gerar, refinar ou melhorar um prompt para outro LLM (ou para si mesmo). "Você é um Engenheiro de Prompts especialista. Melhore este meu prompt..."
