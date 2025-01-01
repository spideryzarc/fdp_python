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

# Inicializando uma matriz de zeros

Para inicializar uma matriz de zeros, podemos usar uma lista de listas com todos os elementos iguais a zero.

Por exemplo, para criar uma matriz 3x3 de zeros, fazemos:

```python
matriz_zeros = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```
ou
```python
n = 3 # número de linhas
m = 3 # número de colunas
matriz_zeros = [[0]*m for _ in range(n)]
```

---

# Iterando sobre os elementos de uma matriz

```python
n = len(matriz) # número de linhas
m = len(matriz[0]) # número de colunas
for i in range(n):
    for j in range(m):
        print(matriz[i][j])
```
ou
```python
for linha in matriz:
    for elemento in linha:
        print(elemento)
```

---
# Algoritmos elementares com matrizes

## Obtendo o número de linhas e colunas de uma matriz

```python
n = len(matriz) # número de linhas
m = len(matriz[0]) # número de colunas
```

## Transposta de uma matriz

```python
transposta = [[matriz[j][i] for j in range(n)] for i in range(m)]
```

---

## Adição de matrizes

```python
# A e B são matrizes de mesma dimensão
def soma_matrizes(A, B): 
    n = len(A)
    m = len(A[0])
    C = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
    return C
```

## Multiplicação matrizes por um escalar

```python
def mult_escalar(A, k):
    n = len(A)
    m = len(A[0])
    B = [[A[i][j] * k for j in range(m)] for i in range(n)]
    return B
```

---

## Multiplicação de matrizes

- **Definição**: Sejam $A$ uma matriz $n \times m$ e $B$ uma matriz $m \times p$. O produto $C = A \cdot B$ é uma matriz $n \times p$ tal que $C[i][j] = \sum_{k=1}^{m} A[i][k] \cdot B[k][j]$.

```python
# A é uma matriz nxm e B é uma matriz mxp
def mult_matrizes(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    C = [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
    return C
```

---

## Achatando uma matriz

Achatamento (ou *flattening*) de uma matriz é a operação de transformar uma matriz em uma lista de seus elementos.

```python
def achatar(matriz):
    return [elemento for linha in matriz for elemento in linha]
```

## Verificando se duas matrizes são iguais

```python
def sao_iguais(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
      return False
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0]))  
```

> `all` é uma função que retorna `True` **se e somente se** todos os elementos de um iterável são **verdadeiros**.

---

## Copiando uma matriz

Cria uma nova matriz que é uma cópia da matriz original.

```python
def copiar_matriz(A):
    return [linha.copy() for linha in A]
```

---

# Exercícios

1. Escreva uma função que receba uma matriz e retorne a soma de todos os seus elementos.
2. Escreva uma função que receba uma matriz e retorne a média de todos os seus elementos.
3. Escreva uma função que receba uma matriz e retorne o maior elemento da matriz.
4. Usando as funções de soma e multiplicação por escalar na nota de aula, escreva uma função que receba duas matrizes de mesma dimensão e retorne a diferença entre elas ($A - B$).
5. Escreva uma função que receba uma matriz e retorne verdadeiro se  a **matriz** é simétrica e falso caso contrário ($A = A^T$).
6. Escreva uma função que receba uma matriz e retorne verdadeiro se a matriz é a **identidade** e falso caso contrário.

---

# NumPy

NumPy é uma biblioteca para computação científica em Python. Dentre outras coisas, ela fornece suporte para operações com matrizes.

```python
import numpy as np
```

> Renomear a biblioteca para `np` é uma convenção comum.


![bg right:40% 80%](https://numpy.org/doc/stable/_static/numpylogo.svg)

---

## Criando matrizes com NumPy

### Matriz de zeros

```python
matriz = np.zeros((3, 3))
```

### Matriz de uns

```python
matriz = np.ones((3, 3))
```

### Matriz identidade

```python
matriz = np.eye(3)
```

---

### Matriz aleatória
Cria uma matriz de dimensão 3x3 com valores aleatórios entre 0 e 1.
```python
matriz = np.random.rand(3, 3)
```

### Matriz sem valor inicial
Não inicializa os valores da matriz, podendo conter qualquer valor.
```python
matriz = np.empty((3, 3))
```

### Matriz com valores específicos
Basta passar uma lista de listas com os valores desejados.
```python
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

---

## Acessando elementos de uma matriz

Preferenialmente, use a notação `matriz[i, j]` para acessar um elemento de uma matriz:
```python
elemento = matriz[1, 2]
```
mas também é possível usar a notação `matriz[i][j]`:
```python
elemento = matriz[1][2]
```

---

##  *Slice* de matrizes

É possível obter submatrizes de uma matriz usando a notação de *slicing*  para cada dimensão.

```python
# Obtém a primeira linha da matriz
linha = matriz[0, :]
```

```python
# Obtém a primeira coluna da matriz
coluna = matriz[:, 0]
```

```python
# Obtém a submatriz formada pelas duas primeiras linhas e duas primeiras colunas
submatriz = matriz[:2, :2]
```

---

## Operações

### Transposta

```python
transposta = matriz.T
```

### Adição de matrizes

```python
C = A + B
```

### Subtração de matrizes

```python
C = A - B
```

---


### Multiplicação por escalar (`*`)

```python
B = A * 3
```

### Multiplicação de matrizes (`@`)
```python
C = A @ B
```

### Multiplicação elemento a elemento (`*`)
```python
C = A * B
```

---

### Inversa de uma matriz

```python
A_inv = np.linalg.inv(A)
``` 

### Determinante de uma matriz

```python
det_A = np.linalg.det(A)
```

### Autovalores e autovetores

```python
autovalores, autovetores = np.linalg.eig(A)
```

---

## Funções comuns 

```python
soma = matriz.sum() # Soma de todos os elementos
media = matriz.mean() # Média de todos os elementos
maximo = matriz.max() # Maior elemento
minimo = matriz.min() # Menor elemento
indice_maximo = matriz.argmax() # Índice do maior elemento
indice_minimo = matriz.argmin() # Índice do menor elemento
```

---

## Exercícios

1. Escreva uma função que receba uma matriz e retorne a soma de todos os seus elementos.
2. Escreva uma função que receba uma matriz e retorne a média de todos os seus elementos.
3. Escreva uma função que receba uma matriz e retorne o maior elemento da matriz.
4. Escreva uma função que receba duas matrizes de mesma dimensão e retorne a diferença entre elas ($A - B$).
5. Escreva uma função que receba uma matriz e retorne verdadeiro se a matriz é simétrica e falso caso contrário ($A = A^T$).
6. Escreva uma função que receba uma matriz e retorne verdadeiro se a matriz é a identidade e falso caso contrário.








