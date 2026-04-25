# 🏋️ Lista de Exercícios: Organizando o Caos (Módulo 3)

Bem-vindo ao laboratório de prática do **Módulo 3: Estruturas de Dados**! 

Agora que você aprendeu sobre **Listas** (nossas prateleiras ordenadas) e **Dicionários** (nossos arquivos etiquetados), é hora de colocar a mão na massa. Tente resolver os desafios abaixo no seu próprio ambiente.

Caso fique travado, consulte a pasta `solucoes/` para ver como o Mestre Alquimista resolveria. Mas lembre-se: tente fazer sozinho primeiro!

---

## 🧪 Exercício 1: O Inventário do Alquimista (Listas)
Você está preparando sua mochila para uma jornada de programação.

1. Crie uma lista chamada `inventario` contendo as seguintes *strings*: `"Teclado"`, `"Café"`, `"Mouse"`.
2. Você percebeu que esqueceu algo crucial. Adicione `"Fones de Ouvido"` ao final da lista usando o comando `.append()`.
3. O `"Mouse"` quebrou. Remova o `"Mouse"` da lista usando o comando `.remove()`.
4. Imprima na tela: `"Meu inventário atualizado tem X itens"`. (Dica: use a função `len(inventario)` para descobrir o tamanho da lista).
5. Imprima a lista completa na tela.

---

## 🤖 Exercício 2: Criando a Persona da IA (Dicionários)
Para que uma IA saiba como agir, precisamos passar instruções em formato de Dicionário (chave e valor).

1. Crie um dicionário chamado `persona_ia` com as seguintes chaves e valores:
   - Chave `"nome"` com o valor `"Sábio"` (string).
   - Chave `"funcao"` com o valor `"Tirar dúvidas de Python"` (string).
   - Chave `"temperatura"` com o valor `0.5` (float).
2. Imprima na tela apenas o nome da IA acessando a chave `"nome"`.
3. A IA está muito robótica! Altere o valor da `"temperatura"` no dicionário para `0.9` (isso a deixará mais criativa).
4. Adicione uma **nova chave** ao dicionário chamada `"modelo"` com o valor `"gpt2"`.
5. Imprima o dicionário completo na tela.

---

## 💬 Exercício 3: O Histórico de Conversa (Lista de Dicionários)
Este é o formato exato que usamos para conversar com modelos do **Hugging Face** usando código!

1. Crie uma lista **vazia** chamada `historico_chat`.
2. Adicione a essa lista (`.append()`) um **dicionário** representando a primeira mensagem do sistema. O dicionário deve ter:
   - `"role"`: `"system"`
   - `"content"`: `"Você é um assistente prestativo."`
3. Adicione um **segundo dicionário** à lista, representando a mensagem do usuário:
   - `"role"`: `"user"`
   - `"content"`: `"Qual é a capital do Brasil?"`
4. Use um loop `for` para percorrer a lista `historico_chat`. Para cada mensagem, imprima na tela de forma amigável no formato `ROLE diz: CONTENT`.
