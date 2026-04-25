# Módulo 1: Fundamentos Sólidos (A Alquimia do Código) 🧪

Bem-vindo ao primeiro passo real da sua jornada! Se o Módulo 0 foi sobre preparar a bancada de trabalho, o Módulo 1 é sobre conhecer os ingredientes básicos da nossa "alquimia digital".

Em Python, tudo o que fazemos envolve manipular informações. Para lidar com essas informações, precisamos de **Variáveis**.

---

## 1. O que são Variáveis? (As Caixas Etiquetadas) 📦

Imagine que você está na cozinha e tem vários potes. Para não se confundir, você coloca uma etiqueta em cada um: "Sal", "Açúcar", "Farinha".

No Python, uma **variável** é exatamente isso: uma caixa onde guardamos um valor e colocamos uma etiqueta (o nome da variável) para encontrá-lo depois.

```python
ingrediente = "Farinha"
quantidade_gramas = 500
```

Aqui, `ingrediente` é a etiqueta da caixa que guarda o texto "Farinha".

---

## 2. Nossos Ingredientes (Tipos de Dados) 🧊

Nem toda informação é igual. Na nossa cozinha digital, temos quatro tipos principais de "ingredientes":

1.  **Strings (`str`)**: São textos. Sempre ficam entre aspas. Ex: `"Olá, IA!"`. Elas são a base dos **prompts** que enviamos para as IAs.
2.  **Inteiros (`int`)**: Números inteiros, sem vírgula. Ex: `10`, `-5`, `2024`.
3.  **Floats (`float`)**: Números com \"ponto flutuante\" (decimais). Ex: `3.14`, `1.99`.  
    *⚠️ Nota Importante: Em Python, usamos o **ponto (.)** como separador decimal, nunca a vírgula!*
4.  **Booleanos (`bool`)**: Valores de sim ou não, verdadeiro ou falso. Em Python: `True` ou `False`.

---

## 3. Misturando Ingredientes (Operações) 🥣

Podemos fazer operações simples com esses dados:

*   **Matemática**: `+`, `-`, `*`, `/`.
*   **Concatenação**: Podemos "somar" textos! `"Bom" + " " + "dia"` vira `"Bom dia"`.

---

## 4. O Coração da IA: Strings e Prompts ✍️

Para uma IA Generativa, a forma como você escreve é tudo. No Python, usamos as **f-strings** para montar mensagens dinâmicas de forma elegante:

```python
nome = "Gemini"
print(f"Olá, {nome}! Você é minha IA favorita.")
```

Dominar como guardar textos em variáveis e montá-los é o primeiro passo para criar sistemas que conversam com IAs automaticamente!

---

### Vamos Praticar?
Abra o arquivo `script.py` para ver os exemplos em ação e depois tente resolver os desafios no `exercises.py`!
