# 4. Ferramentas e Frameworks para Engenharia de Prompt

À medida que passamos de "brincar no ChatGPT" para "construir sistemas em produção", gerenciar prompts no código como simples strings não escala. Ferramentas foram criadas para orquestrar LLMs.

---

## 4.1 LangChain

[LangChain](https://www.langchain.com/) é o framework mais famoso do ecossistema. Desenvolvido inicialmente em Python (e com versão em JS/TS), ele padroniza o uso de LLMs.

**Principais conceitos no contexto de Prompts:**
- **PromptTemplates:** Classes que permitem inserir variáveis dinâmicas em prompts com segurança.
  ```python
  from langchain_core.prompts import PromptTemplate
  
  template = "Traduza a palavra '{palavra}' do inglês para o {idioma}."
  prompt = PromptTemplate.from_template(template)
  prompt.format(palavra="Apple", idioma="Espanhol")
  ```
- **Chains (Cadeias):** Une um PromptTemplate a um LLM e a um OutputParser (formatador de saída) em um fluxo único.
- **Agents:** Implementam lógicas como o **ReAct** de forma nativa, permitindo dar "ferramentas" (calculadoras, busca web, acesso a banco de dados) para o LLM.

---

## 4.2 PromptLayer

[PromptLayer](https://promptlayer.com/) atua como um middleware. Você faz as chamadas de API passando pelo servidor deles, que atua como uma camada de **Observabilidade e Versionamento**.

**Por que usar?**
1. **Histórico Visual:** Guarda o log de todas as chamadas de API feitas, mostrando o prompt exato, a resposta, latência e custo em tokens.
2. **Versionamento de Prompt:** Em vez de fazer hardcode do prompt no seu código Python, você o escreve na interface web do PromptLayer. Seu código apenas "puxa" a versão mais recente. Se precisar alterar o prompt em produção, não precisa fazer deploy do código, basta alterar no painel.
3. **Avaliação (Evals):** Permite avaliar se as respostas estão boas ou ruins.

---

## 4.3 OpenPrompt

[OpenPrompt](https://github.com/thunlp/OpenPrompt) é mais focado em pesquisa e no conceito de **Prompt-Learning** para modelos open-source (Hugging Face).

Diferente do LangChain que é orientado a API/Engenharia de Software, o OpenPrompt é voltado para adaptar modelos pré-treinados (PLMs) para tarefas de NLP específicas usando *template-based learning* e *verbalizers* (mapeando a saída do modelo de volta para labels de classificação).

---

## Conclusão: Escolhendo a Ferramenta

- **Vai criar Agentes, RAG ou pipelines complexos em código?** Vá de *LangChain* (ou LlamaIndex).
- **Precisa gerenciar dezenas de prompts com um time e monitorar custos em produção?** Vá de *PromptLayer* (ou LangSmith).
- **Está fazendo pesquisa avançada em NLP com modelos abertos e fine-tuning de prompts?** Vá de *OpenPrompt*.
