---
marp: true
title: "Matrizes"
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
# Guarda-me ó Deus, porque em ti confio. 

---

# Matrizes

Uma **matriz** é uma tabela de números dispostos em **linhas** e **colunas**.


---

Podemos manipular matrizes de várias formas em Python, por exemplo:

- Usando listas de listas : Recomentado para matrizes pequenas e simples ou para quem está aprendendo a programar.
- Usando a biblioteca NumPy : Recomendado para matrizes grandes ou para quem precisa de funções matemáticas avançadas e **eficientes**.

--- 

# Listas de Listas

Uma matriz pode ser representada em Python como uma lista de listas. Por exemplo, a matriz:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

pode ser representada em Python como:

```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

---

## Observação sobre a sintaxe de Python

Em Python, elementos que são delimitados por chaves, parênteses ou colchetes podem ser divididos em várias linhas sem a necessidade de usar o caractere de continuação de linha `\`.

Por exemplo, a lista de listas acima pode ser escrita como:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

# Acessando elementos de uma matriz

Para acessar um elemento de uma matriz, usamos a notação `matriz[i][j]`, onde `i` é o índice da linha e `j` é o índice da coluna.

Por exemplo, para acessar o elemento da segunda linha e terceira coluna da matriz acima, fazemos:

```python
matriz[1][2] # 6
```

---

# Exercício



