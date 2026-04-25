# Módulo 2: O Fluxo de Pensamento (Condicionais e Loops) 🧠

Bem-vindo ao Módulo 2! Aqui vamos aprender como dar "inteligência" e autonomia aos nossos scripts.

Na programação, o "fluxo de pensamento" refere-se a como o código toma decisões e executa tarefas repetitivas. Isso é essencial para controlar agentes de IA, permitindo que eles reajam a diferentes situações e processem grandes volumes de dados (textos).

---

## 1. Condicionais (`if`/`elif`/`else`): Bifurcações no Caminho 🛤️

Imagine que você está caminhando e chega a uma bifurcação. Se o caminho da direita parecer seguro, você vai por ele. Se não, você verifica o da esquerda. Se ambos parecerem ruins, você volta.

Em Python, fazemos isso com condicionais:

- `if` (Se): Avalia uma condição. Se for verdadeira (`True`), o bloco de código recuado (com espaço antes) é executado.
- `elif` (Ou se): Testa uma nova condição caso a anterior seja falsa (`False`).
- `else` (Senão): O que fazer se nenhuma das condições anteriores for verdadeira.

```python
tamanho_prompt = 500

if tamanho_prompt > 1000:
    print("Aviso: O prompt está muito longo, a IA pode se perder.")
elif tamanho_prompt < 10:
    print("Aviso: O prompt está muito curto, seja mais específico.")
else:
    print("O tamanho do prompt está ideal!")
```

---

## 2. Loops (`for` e `while`): Tarefas Repetitivas 🔄

Muitas vezes, precisamos fazer a mesma coisa várias vezes. Imagine ter que enviar a mesma mensagem para 100 usuários. Fazer isso manualmente seria entediante. Os loops automatizam essas tarefas repetitivas.

### O Loop `for` (Para cada)

Usado quando você quer passar por cada item de uma coleção (veremos listas no próximo módulo!) ou repetir algo um número exato de vezes usando `range()`.

```python
# Repete 3 vezes
for i in range(3):
    print(f"Gerando resposta número {i + 1}...")
```

### O Loop `while` (Enquanto)

Usado quando você quer que uma ação se repita *enquanto* uma condição for verdadeira. O número de repetições pode não ser conhecido no início.

```python
tentativas = 3

while tentativas > 0:
    print(f"Tentando conectar na API... Restam {tentativas} tentativas.")
    tentativas = tentativas - 1

print("Conexão falhou.")
```

---

### Vamos Praticar?
Abra o arquivo `script.py` para ver um menu interativo e depois resolva os desafios no `exercises.py`!
