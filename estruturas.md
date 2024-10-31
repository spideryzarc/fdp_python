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

# Listas

* No módulo anterior, vimos que uma variável pode armazenar um valor. Por exemplo, a variável `x` pode armazenar o valor `10`.
* Mas, e se quisermos armazenar mais de um valor?
  * Criamos duas variáveis `x` e `y`, certo?
* E se quisermos armazenar 100 valores?
  * Criamos 100 variáveis, certo?
    * `x1`, `x2`, ..., `x100`?
* E se quisermos armazenar uma quantidade indefinida de valores?

---

- Para armazenar uma quantidade indefinida de valores, usamos uma **lista**.
- Uma lista é uma coleção de valores, onde cada valor é identificado por um índice.
- Em Python, uma lista é representada por colchetes `[]`.
- Por exemplo, a lista `numeros` abaixo contém 5 valores:
```python
numeros = [1, 2, 3, 4, 5]
```
---

## Acessando elementos de uma lista

- Para acessar um elemento de uma lista, usamos o **índice** do elemento.
- O índice de uma lista **começa em 0** (*zero base index*).
- O **maior índice** de uma lista é o **tamanho da lista menos 1**.
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

- Se tentarmos acessar um índice maior ou igual ao tamanho da lista, ocorre um erro.
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[5])
>>> IndexError: list index out of range
```

- Se tentarmos acessar um índice negativo, o Python conta a partir do final da lista.
```python
numeros = [1, 2, 3, 4, 5]
print(numeros[-1])
>>> 5
```
> É bastante comum usar `-1` para acessar o último elemento de uma lista.


