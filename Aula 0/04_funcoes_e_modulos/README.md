# Módulo 4: O Poder da Reutilização (Funções) ⚙️

Na programação, se você precisa fazer a mesma coisa mais de duas vezes, você deve automatizar. As **Funções** são blocos de código que podemos "salvar" e "chamar" pelo nome sempre que precisarmos.

Pense nelas como receitas de cozinha: você define os passos uma vez e pode segui-los sempre que quiser cozinhar aquele prato.

---

## 1. Como criar uma Função? (`def`)

Usamos a palavra-chave `def` (do inglês *define*).

```python
def saudar_usuario(nome):
    print(f"Olá, {nome}! Preparado para criar sua IA?")
```

Para usar a função, basta chamá-la pelo nome:
```python
saudar_usuario("Carlos")
```

---

## 2. Ingredientes e Resultado (Parâmetros e Retorno) 🧪

*   **Parâmetros**: São os "ingredientes" que a função recebe (como o `nome` no exemplo acima).
*   **Return**: É o resultado final que a função entrega de volta para o programa.

```python
def calcular_area_prompt(largura, altura):
    area = largura * altura
    return area # Devolve o valor para quem chamou
```

---

## 3. Por que usar Funções na IA?

Em projetos de IA, usamos funções para:
*   Limpar o texto recebido do usuário.
*   Formatar o prompt antes de enviar para a API.
*   Processar a resposta que a IA nos devolve.

Isso deixa o código organizado, fácil de ler e fácil de corrigir!

---

### Vamos Praticar?
Abra o arquivo `script.py` para ver exemplos reais de funções de formatação e resolva os desafios no `exercises.py`!
