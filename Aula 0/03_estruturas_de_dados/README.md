# Módulo 3: Organizando o Caos (Estruturas de Dados) 🗃️

Até agora, guardamos um valor por "caixa" (variável). Mas e se precisarmos guardar o histórico de uma conversa inteira ou uma lista de centenas de nomes? Para isso, usamos coleções de dados.

Em Python, as duas estruturas mais importantes para quem trabalha com IA são as **Listas** e os **Dicionários**.

---

## 1. Listas (`list`): A Prateleira Ordenada 📋

Uma lista é uma coleção de itens em uma ordem específica. Imagine uma prateleira de livros onde cada posição tem um número (índice).

*   **Importante**: Em programação, começamos a contar do **zero (0)**!
*   Usamos colchetes `[]` para criar listas.

```python
historico = ["Olá", "Quem é você?", "Sou uma IA"]
print(historico[0]) # Imprime "Olá"
```

---

## 2. Dicionários (`dict`): O Arquivo Etiquetado 🗂️

O dicionário é a estrutura **mais poderosa** para IA. Ele guarda informações em pares de **Chave** e **Valor**. 
É exatamente assim que os modelos abertos (como os do **Hugging Face**) recebem os dados.

*   Usamos chaves `{}` para criar dicionários.
*   Formato: `{"chave": "valor"}`.

```python
mensagem = {
    "role": "user",
    "content": "Me conte uma piada."
}
print(mensagem["content"]) # Imprime a mensagem
```

---

## 3. Por que isso importa para IA? 🤖

Quando conversamos com um modelo de linguagem (LLM), enviamos uma **Lista de Dicionários**. Cada dicionário é uma mensagem, e a lista é o contexto da conversa.

Dominar essas estruturas é o que separa um iniciante de alguém que realmente constrói sistemas inteligentes.

---

### Vamos Praticar?
Abra o arquivo `script.py` para ver como manipular esses dados e resolva os desafios no `exercises.py`!
