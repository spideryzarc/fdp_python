---
marp: true
title: "Coleções em Python"
theme: default
class: lead
footer: "F.P. - Albert E. F. Muritiba"
paginate: true
backgroundColor: #d6e0e1
#backgroundImage: url('https://marp.app/assets/hero-background.svg')
#backgroundImage: url('https://spideryzarc.github.io/labCD/bg/light_wall4.jpg')
style: |
  .small{
    font-size: 0.75rem;
  }
  .big{
    font-size: 1.5rem;
  }
# Deus é bom o tempo todo

---

# Coleções em Python

Neste módulo, vamos estudar as **coleções** em Python. As coleções são estruturas de dados que permitem armazenar **múltiplos valores** em uma única variável.

   
![bg right:40%](empty.svg)

---

# E se ...?

* No módulo anterior, vimos que uma variável pode armazenar **um valor**. Por exemplo, a variável `x` pode armazenar o valor `10`.
* Mas, e se quisermos armazenar dois valores?
  * Criamos duas variáveis `x` e `y`, certo?
* E se quisermos armazenar 100 valores?
  * Criamos 100 variáveis, `x1`, `x2`, ..., `x100` , certo?
* E se quisermos armazenar uma quantidade **indefinida** de valores?

---

# Coleções

Obviamente, criar uma variável para cada valor não é prático. Para armazenar uma quantidade grande ou indefinida de valores, usamos uma **coleção**.

* Em Python, existem **quatro tipos** de coleções:
  * **Listas** (`list`)
  * **Tuplas** (`tuple`)
  * **Conjuntos** (`set`)
  * **Dicionários** (`dict`)

---
# Listas

* Para armazenar uma quantidade indefinida de valores, usamos uma **lista**.
* Uma lista é uma coleção de valores, onde cada valor é identificado por um **índice** correspondente à sua **posição** na lista.
* Uma lista é representada por colchetes `[]` e os valores são separados por **vírgula**.
* Por exemplo, a lista `numeros` abaixo contém 5 valores:
```python
numeros = [1, 2, 3, 4, 5]
```

---

## Características gerais de uma lista

- Uma lista pode conter **qualquer tipo de valor**.
- Uma mesma lista pode conter **valores de tipos diferentes** (heterogênea).
- Uma lista **não é um conjunto**, ou seja, 
  - **os valores podem se repetir**.
  - **a ordem dos valores é importante**.
  - **os valores são acessados por índices**.

---

## Acessando elementos de uma lista

- Para acessar um elemento de uma lista, usamos o **índice** do elemento.
- Python é ***zero based***, ou seja, os índices começam **sempre** em 0.
- Portanto, o maior indice de uma lista com `n` elementos é `n-1`.
- Por exemplo, para acessar o primeiro elemento da lista `numeros`, fazemos:

```python
numeros = [1, 2, 3, 4, 5]
print(numeros[0]) 
>>> 1
```

---

## Modificando elementos de uma lista

- Para modificar um elemento de uma lista, usamos o índice do elemento.
- Por exemplo, para modificar o segundo elemento da lista `numeros`, fazemos:

```python
numeros = [1, 2, 3, 4, 5]
numeros[1] = 10
print(numeros)
>>> [1, 10, 3, 4, 5]
```

---

## Índices fora do intervalo

- Se tentarmos acessar um índice **maior ou igual** ao tamanho da lista, ocorre um erro.
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[5])
>>> IndexError: list index out of range
```

- Se tentarmos acessar um índice **negativo**, o Python conta a partir do final da lista.
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[-1])
>>> 5
```
> É **bastante comum** usar `-1` para acessar o último elemento de uma lista.

---

### Observações sobre índices negativos

* O índice `-1` acessa o último elemento da lista.
* O índice `-k` acessa o k-ésimo elemento a partir do final da lista.
* O maior índice negativo é `-n`, onde `n` é o tamanho da lista.
  ```python
  numeros = [1, 2, 3, 4, 5]
  print(numeros[-6])
  >>> IndexError: list index out of range
  ```
* Índices negativos são uma **particularidade** do Python e **não são comuns** em outras linguagens.

---
## Atribuição com listas

Observer o seguinte código:

```python
A = [1, 2, 3]
B = [4, 5, 6]
A = B
B[0] = 10
print(A)
>>> [10, 2, 3]
print(B)
>>> [10, 5, 6]
```

> O que aconteceu?

---

* Quando trabalhamos com variáveis de tipos primitivos, como `int`, `float`, `str`, etc., a atribuição de uma variável a outra **copia** o valor da variável original para a nova variável.

* Porém, quando trabalhamos com **listas**, a atribuição de uma lista a outra **copia a referência** da lista original para a nova variável.

* Em outras palavras, `A = B` faz com que `A` e `B` **apontem para a mesma lista** na memória.

---

## Copiando listas

Se desejamos **copiar** o conteúdo de uma lista para outra, sem que as listas sejam **referências** da mesma lista, podemos usar a função `copy` ou o operador `[:]`.
- A função `copy`  *aloca* um **novo espaço** de memória e **copia** os elementos da lista original para esse novo espaço.

```python
A = [1, 2, 3]
B = A.copy() # ou B = A[:]
B[0] = 10
print(A)
>>> [1, 2, 3]
print(B)
>>> [10, 2, 3]
```

> Vamos aprender sobre `[:]` mais adiante.

---
## Comprimento de uma lista

- Para saber o **tamanho** de uma lista, usamos a função `len`.
```python
numeros = [1, 2, 3, 4, 5]
print(len(numeros))
>>> 5
```

---
## Operações com listas

* Além de acessar e modificar elementos, podemos realizar diversas operações com listas, como:
  * **Adicionar** elementos
  * **Remover** elementos
  * **Concatenar** listas
  * **Multiplicar** listas
  * **Ordenar** listas
  * **Inverter** listas
  * **Buscar** elementos
---

### Adicionando elementos

- Para adicionar um elemento ao final de uma lista, usamos o método `append`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
>>> [1, 2, 3, 4, 5, 6]
```

--- 

- Para adicionar um elemento em uma posição específica, usamos o método `insert`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.insert(2, 10) # Adiciona o valor 10 na posição 2
print(numeros)
>>> [1, 2, 10, 3, 4, 5]
```

> A **posição** deve ser entre `0` e o tamanho da lista.
> Os valores **após a posição** são **deslocados** para a direita.
> Portanto, o método `insert` é **menos eficiente** que o `append`.

---

- Para adicionar **todos os elementos** de uma lista `l2` ao final de uma lista `l1`, usamos o método `extend`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
outros_numeros = [6, 7, 8]
numeros.extend(outros_numeros)
print(numeros)
>>> [1, 2, 3, 4, 5, 6, 7, 8]
```

<br>

> **Experimente**, usar `append` no lugar de `extend` e veja o que acontece, o resultado é o mesmo?

---

### Removendo elementos

- Para remover um elemento de uma lista, usamos o método `remove`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
- O método `remove` remove **apenas** primeira ocorrência do valor na lista.

```python
numeros = [1, 2, 3, 4, 5]
numeros.remove(3) # Remove o valor 3
print(numeros)
>>> [1, 2, 4, 5]
```

<br>
<br>

> **Atenção**: O parâmetro do método `remove` é o **valor** a ser removido, **não** a **posição**.


---

- Para remover uma elemento em uma dado **índice**, usamos o método `pop`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
x = numeros.pop(2) # Remove o valor na posição 2
print(numeros)
>>> [1, 2, 4, 5]
print(x)
>>> 3
```

- O método `pop(i)` remove o elemento na posição `i` e **retorna** o valor removido.
- Se não for passado nenhum argumento, o método `pop` remove o **último** elemento da lista.
- Valores **retornados** por funções **não precisam** ser necessariamente atribuídos a uma variável.
- Se a lista estiver vazia, o método `pop` gera um erro.

---

- Outra forma de remover um elemento de uma lista é usando o comando `del`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
del numeros[2] # Remove o valor na posição 2
print(numeros)
>>> [1, 2, 4, 5]
```
<br>
<br>

> Mais adiante, vamos ver que o comando `del` pode ser usado para remover vários elementos de uma lista de uma só vez.
---

- Para remover **todos os elementos** de uma lista, usamos o método `clear`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)
>>> []
```

---

### Concatenando listas

- Para concatenar duas listas, usamos o operador `+`.
```python
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
resultado = numeros + letras
print(resultado)
>>> [1, 2, 3, 'a', 'b', 'c']
```
- O operador de acunulação `+=` também pode ser usado para concatenar listas.
```python
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
numeros += letras
print(numeros)
>>> [1, 2, 3, 'a', 'b', 'c']
```

---

### Multiplicando listas

- Para multiplicar uma lista por um número `n`, usamos o operador `*`.
```python
numeros = [1, 2, 3]
resultado = numeros * 3
print(resultado)
>>> [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

```python
zeros = [0] * 5
print(zeros)
>>> [0, 0, 0, 0, 0]
```

---

### Ordenando listas

- Para ordenar uma lista, usamos o método `sort`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
- O método `sort` **modifica** a lista original.
- O método `sort` **não** funciona para listas com elementos de tipos diferentes.

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort()
print(numeros)
>>> [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

---

- Para ordenar uma lista **sem modificá-la**, usamos a função `sorted`. [doc](https://docs.python.org/3/library/functions.html#sorted)
- A função `sorted` **não** modifica a lista original.
- A função `sorted` **funciona** para listas com elementos de tipos diferentes.

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
ordenados = sorted(numeros)
print(ordenados)
>>> [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(numeros)
>>> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
```

<br>

> Observe que `sorted` é uma **função** *livre*, enquanto `.sort` é um **método** que está **atrelado** a um objeto.

---

### Invertendo listas

- Para inverter uma lista, usamos o método `reverse`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
- O método `reverse` **modifica** a lista original.

```python
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)
>>> [5, 4, 3, 2, 1]
```

---

### Buscando elementos

- Para checar se um elemento está em uma lista, usamos o operador `in`.
```python
numeros = [1, 2, 3, 4, 5]
if 3 in numeros:
    print('3 está na lista')
else:
    print('3 não está na lista')
```

- Para buscar a **posição** de um elemento, usamos o método `index`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
print(numeros.index(3))
>>> 2
```
- `.index` levanta um erro se o elemento não está na lista.

---

## Iterando sobre listas

- Para **iterar** sobre os **elementos** de uma lista, usamos um **laço** `for`.
```python
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
```

- Para **iterar** sobre os **índices** de uma lista, usamos a função `range`.
```python
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    print(numeros[i])
```

---

- Também podemos usar o laço `while` para **iterar** sobre os elementos de uma lista, mas é bem menos prático.
```python
numeros = [1, 2, 3, 4, 5]
i = 0
while i < len(numeros):
    print(numeros[i])
    i += 1
```

---


## Exercícios de fixação

1. Crie uma lista `numeros` com os valores `1, 2, 3, 4, 5`.
2. Adicione o valor `6` ao final da lista.
3. Remova o valor `3` da lista.
4. Adicione o valor `10` na posição `2`.
5. Inverta a lista.
6. Ordene a lista.
7. Imprima o tamanho da lista.
8. Imprima o dobro de cada elemento da lista.

---

## Listas (*modo hacker*)

- Para se exibir para os amigos. você precisa dominar os conceitos de:
  - ***List Comprehension***
  - ***Slicing***


---

### *List Comprehension*

- É uma forma **concisa** de criar listas em Python.
- A sintaxe é:
  ```python
  [expressao for item in lista]
  ```

---
#### Exemplos

- Modo careta:
  ```python
  quadrados = []
  for i in range(1, 6):
      quadrados.append(i**2)
  ```
- Modo descolado:
  ```python
  quadrados = [i**2 for i in range(1, 6)]
  ```

![bg right:40%](images/buscemi.jpg)

---

- Modo careta:
  ```python
  pares = []
  for i in range(1, 11):
      if i % 2 == 0:
          pares.append(i)
  ```
- Modo descolado:
  ```python
  pares = [i for i in range(1, 11) if i % 2 == 0]
  ```

<br>

> **Dica**: Use *List Comprehension* sempre que possível, pois é mais **rápido** e **conciso**, além de ser **mais descolado** (elegante).  

---

### *Slicing*

- É uma forma de **acessar** partes de uma lista através de **índices**.
- Também conhecido como *fancy indexing*.
- A sintaxe é:
  ```python
  lista[inicio:fim:passo]
  ```
  - `inicio`: índice de início (inclusivo).
  - `fim`: índice de fim (exclusivo).
  - `passo`: intervalo entre os índices.
  - São os mesmos parâmetros da função `range`.


![bg right:35% 90%](images/sir.png)

---

- `lista[:]`: toda a lista.
- `lista[a:]`: da posição `a` até o final.
- `lista[:b]`: do início até a posição `b` (exclusivo).
- `lista[a:b]`: da posição `a` até a posição `b` (exclusivo).
- `lista[::2]`: elementos de dois em dois.
- `lista[::-1]`: lista invertida.
- `lista[-3:]`: os três últimos elementos.
- `lista[:-3]`: todos os elementos, exceto os três últimos.
- `lista[6:2:-1]`: elementos da posição 6 até a posição 2 (exclusivo), de trás para frente.

---

#### Exemplos

##### Imprimindo uma fatia de uma lista:
```python
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
- Modo plebeu:
  ```python  
  for i in range(2, 7):
      print(numeros[i])
  ```

- Modo aristocrático:
  ```python
  print(numeros[2:7])
  ``` 

---

##### Copiando uma lista:
```python
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- Modo plebeu:
  ```python
  copia = []
  for i in numeros:
      copia.append(i)
  ```
- Modo burguês:
  ```python
  copia = numeros.copy()
  ```
- Modo aristocrático:
  ```python
  copia = numeros[:]
  ```
---

##### Invertendo uma lista:
```python
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- Modo plebeu:
  ```python
  for i in range(len(numeros)//2):
      aux = numeros[i]
      numeros[i] = numeros[-i-1]
      numeros[-i-1] = aux      
  ```
- Modo burguês:
  ```python
  numeros.reverse()
  ```
- Modo aristocrático:
  ```python
  numeros = numeros[::-1]
  ```

---










