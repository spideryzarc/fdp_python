---
marp: true
title: "Estruturas em Python"
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

# Estruturas de Dados

Neste módulo, vamos estudar as estruturas de dados nativas em Python. São elas:

1. Listas
2. Tuplas
3. Conjuntos
4. Dicionários

---

# E se ...?

* No módulo anterior, vimos que uma variável pode armazenar **um valor**. Por exemplo, a variável `x` pode armazenar o valor `10`.
* Mas, e se quisermos armazenar dois valores?
  * Criamos duas variáveis `x` e `y`, certo?
* E se quisermos armazenar 100 valores?
  * Criamos 100 variáveis, certo?
    * `x1`, `x2`, ..., `x100`?
* E se quisermos armazenar uma quantidade **indefinida** de valores?

---
# Listas

* Para armazenar uma quantidade indefinida de valores, usamos uma **lista**.
* Uma lista é uma coleção de valores, onde cada valor é identificado por um **índice**.
* Em Python, uma lista é representada por colchetes `[]` e os valores são separados por **vírgula**.
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
- Python é ***zero based***, ou seja, os índices começam sempre em 0.
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

## Indices fora do intervalo

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

## Operações com listas

- Podemos realizar diversas operações com listas, como:
  * Adicionar elementos
  * Remover elementos
  * Concatenar listas
  * Multiplicar listas
  * Ordenar listas
  * Inverter listas
  * Etc.

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

> A **posição** deve ser um **índice válido** da lista.
> Os valores **após a posição** são **deslocados** para a direita.
> Portanto, o método `insert` é **menos eficiente** que o `append`.

---

- Para adicionar **todos os elementos** de uma lista `l2` ao final de uma lista `l1`, usamos o método `extend`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.extend([6, 7, 8])
print(numeros)
>>> [1, 2, 3, 4, 5, 6, 7, 8]
```

<br>

> **Experimente**, usar `append` no lugar de `extend` e veja o que acontece.

---

### Removendo elementos

- Para remover um elemento de uma lista, usamos o método `remove`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.remove(3) # Remove o valor 3
print(numeros)
>>> [1, 2, 4, 5]
```
- O método `remove` remove **apenas** primeira ocorrência do valor na lista.


---

- Para remover um elemento de uma lista, usamos o método `pop`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
x = numeros.pop(2) # Remove o valor na posição 2
print(numeros)
>>> [1, 2, 4, 5]
print(x)
>>> 3
```

- O método `pop` remove o elemento na posição `i` e **retorna** o valor removido.
- Se não for passado nenhum argumento, o método `pop` remove o **último** elemento da lista.
- Se a lista estiver vazia, o método `pop` gera um erro.

---

- Para remover um elemento de uma lista, usamos o método `del`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
del numeros[2] # Remove o valor na posição 2
print(numeros)
>>> [1, 2, 4, 5]
```

---

- Para remover **todos os elementos** de uma lista, usamos o método `clear`. [doc](https://docs.python.org/3/tutorial/datastructures.html)
```python
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)
>>> []
```



