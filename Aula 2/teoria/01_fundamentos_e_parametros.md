# 1. Fundamentos da Engenharia de Prompt e Parâmetros

A Engenharia de Prompt não é apenas sobre "fazer boas perguntas". É o processo iterativo de desenhar, refinar e otimizar entradas para que o modelo produza a saída mais precisa, relevante e segura possível.

## 1.1 Componentes de um Prompt

Um prompt bem construído não é apenas uma pergunta, mas um conjunto de informações. Os componentes fundamentais são:

1. **Instrução:** A tarefa ou ação específica.
2. **Contexto:** Informação de fundo.
3. **Dados de Entrada:** O objeto a ser processado.
4. **Indicador de Saída:** O formato esperado.

---

## 1.2 A Estrutura "Ideal" de um Prompt (P.C.T.C.F)

Para obter resultados consistentes e profissionais, recomenda-se seguir uma estrutura lógica e sequencial. Começar pela "Persona" ajuda o modelo a filtrar o seu "espaço de conhecimento" para o domínio correto.

### 1. **Persona (Quem?)**
Defina quem o modelo deve ser. Isso estabelece o tom, o nível de expertise e o estilo de linguagem.
*   *Exemplo:* "Você é um Engenheiro de Prompt Sênior com 10 anos de experiência em arquitetura de LLMs."

### 2. **Contexto (Onde/Por que?)**
Explique o cenário. Por que você está pedindo isso? Para quem é o resultado final?
*   *Exemplo:* "Estou preparando um workshop técnico para desenvolvedores que nunca usaram a API da OpenAI."

### 3. **Tarefa / Task (O quê?)**
A ação principal de forma clara e direta, preferencialmente usando verbos de ação (Crie, Resuma, Analise, Codifique).
*   *Exemplo:* "Escreva um guia de boas práticas para o uso de parâmetros de temperatura em produção."

### 4. **Restrições e Regras / Constraints (Como?)**
O que o modelo **não** deve fazer, ou regras específicas de negócio que deve seguir.
*   *Exemplo:* "Não utilize jargões excessivamente complexos. Mantenha o texto com no máximo 500 palavras. Não cite modelos obsoletos."

### 5. **Formato de Saída / Output (Resultado)**
Como você quer receber a informação? Markdown, JSON, Tabela, Lista de tópicos, Código?
*   *Exemplo:* "Formate a resposta em Markdown, utilizando subtítulos claros e uma tabela comparativa no final."

---

## 1.3 O Poder dos Delimitadores

Delimitadores são símbolos que ajudam a IA a separar claramente o que é instrução do que é dado. Isso previne confusão e ataques de injeção de prompt (Prompt Injection).

**Delimitadores comuns:**
- Aspas triplas: `"""texto"""`
- Crases triplas (Markdown): ` ```texto``` `
- Tags XML/HTML: `<artigo>texto</artigo>`
- Símbolos: `###`, `---`

**Exemplo:**
> Resuma o texto delimitado por tags <texto> em uma única frase.
>
> <texto>
> A inteligência artificial generativa tem avançado rapidamente. Modelos de linguagem...
> </texto>

## 1.3 Entendendo Parâmetros: Temperatura e Top-P

Ao usar APIs de LLMs (e em algumas interfaces de chat avançadas), você pode ajustar parâmetros que controlam a "aleatoriedade" das respostas.

### Temperature (Temperatura)
Controla a aleatoriedade das previsões. Varia geralmente de 0.0 a 2.0 (ou 1.0 em alguns modelos).
- **Baixa (0.0 - 0.3):** Respostas determinísticas, focadas e repetitivas. Ideal para código, extração de dados, tradução exata e matemática.
- **Média (0.4 - 0.7):** Um bom equilíbrio. O modelo é coerente, mas com um pouco de variação de vocabulário. Ideal para redação geral e chat.
- **Alta (0.8 - 1.0+):** Respostas criativas, variadas e, às vezes, imprevisíveis (podendo alucinar mais). Ideal para brainstorming, poesia ou escrita criativa.

### Top-p (Nucleus Sampling)
Uma alternativa (ou complemento) à Temperatura. Se você definir Top-p como 0.1, o modelo considerará apenas os tokens que compõem os 10% do topo da massa de probabilidade.
*Regra de ouro:* Geralmente, altera-se a Temperatura **OU** o Top-p, não ambos ao mesmo tempo.

## 1.4 O que são Tokens?

LLMs não leem palavras, leem **tokens**. Um token pode ser uma palavra inteira, uma sílaba ou apenas uma letra.
- Em inglês, 1 token ≈ 4 caracteres ou 0,75 palavras.
- Em português ou linguagens de programação, uma palavra pode ser dividida em 2, 3 ou mais tokens.

**Por que isso importa?**
1. **Custos:** As APIs cobram por token (entrada e saída).
2. **Limites de Contexto (Context Window):** Todo modelo tem um limite de tokens que pode "lembrar" de uma vez (ex: 8K, 128K, 1M tokens). Se você passar o limite, o modelo esquece o início da conversa.
3. **Eficiência:** Prompts concisos e bem delimitados economizam tokens de entrada e geram processamento mais rápido.
