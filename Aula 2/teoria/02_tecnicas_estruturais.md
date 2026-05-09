# 2. Técnicas Estruturais Básicas

Aqui exploramos como estruturar o prompt para ensinar o modelo a resolver o problema, indo além de simples perguntas e respostas.

## 2.1 Role Prompting (Atribuição de Papel)

O Role Prompting define uma "persona" para a IA. Ao assumir um papel, o modelo ajusta seu vocabulário, tom, nível de profundidade e conhecimento inferido.

**Exemplo:**
> **Prompt:** Explique o que é um buraco negro.
> *Saída provável:* Uma explicação enciclopédica padrão.

> **Prompt com Role:** Você é um professor do ensino fundamental apaixonado por astronomia. Explique o que é um buraco negro para uma criança de 8 anos, usando metáforas divertidas com objetos do dia a dia.
> *Saída provável:* Vai usar exemplos como "ralos de banheira" ou "aspiradores de pó invisíveis" no espaço, com linguagem simples e empolgante.

**Dica:** Sempre defina a expertise da persona (ex: "Você é um Engenheiro de Software Sênior especialista em Python").

---

## 2.2 Zero-Shot Prompting

É a técnica mais comum. Você dá a instrução sem fornecer nenhum exemplo prévio de como a resposta deve ser. O modelo depende inteiramente do seu treinamento prévio.

**Exemplo Zero-Shot:**
> Classifique o sentimento da frase abaixo como Positivo, Negativo ou Neutro.
> Frase: "Eu achei o filme um pouco longo, mas a atuação salvou a experiência."
> Sentimento:

*Quando usar:* Para tarefas comuns e bem conhecidas (resumo, tradução, classificação básica). Modelos modernos (como GPT-4, Claude 3.5) são excelentes em zero-shot.

---

## 2.3 Few-Shot Prompting (One-Shot e Few-Shot)

Quando a tarefa é muito específica, requer um formato de saída peculiar, ou o modelo falha no Zero-Shot, usamos o **Few-Shot Prompting**. Consiste em passar 1 (One-shot) ou mais (Few-shot) exemplos de "Entrada -> Saída desejada" no próprio prompt.

Isso serve para "treinar em tempo de inferência" (In-Context Learning), ajustando o modelo sem alterar seus pesos internos.

**Exemplo One-Shot:**
> Extraia entidades (Nome, Empresa) do texto.
> 
> Texto: "João trabalha na Microsoft."
> Entidades: Nome: João | Empresa: Microsoft
> 
> Texto: "A Apple anunciou ontem que Tim Cook fará uma palestra."
> Entidades:

**Exemplo Few-Shot:**
> Esta é uma ferramenta que traduz gírias da internet para linguagem formal corporativa.
> 
> Entrada: O projeto deu ruim, fml.
> Saída: O projeto encontrou obstáculos críticos, equipe.
> 
> Entrada: Essa task é mamão com açúcar.
> Saída: Esta tarefa possui baixa complexidade.
> 
> Entrada: O cliente tiltou na reunião.
> Saída:

**Dicas de Ouro para Few-Shot:**
1. **Formato consistente:** O formato dos exemplos deve ser exatamente igual ao que você espera no final.
2. **Diversidade:** Mostre exemplos que cubram diferentes casos (ex: um positivo, um negativo e um neutro em classificação de texto).
3. **Ordem importa:** Em alguns modelos, o último exemplo influencia mais a resposta (Recency Bias).
