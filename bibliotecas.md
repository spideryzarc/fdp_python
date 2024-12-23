---
marp: true
title: "Bibliotecas básicas"	
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

# Bibliotecas básicas

Python oferece inúmeras bibliotecas para facilitar o desenvolvimento de programas, neste módulo vamos estudar algumas das mais básicas e úteis.

![bg right:40% 80%](empty.svg)


---
# Importação de bibliotecas

Uma biblioteca é um conjunto de funções e métodos que podem ser utilizados em um programa. Para utilizar uma biblioteca, é necessário importá-la. 

- `import` é o comando utilizado para **importar** uma biblioteca por **completo**.

```python
import math

print(math.sqrt(25)) 
>>> 5.0
```

- Podemos acessar as funções da biblioteca utilizando o nome da biblioteca seguido de um ponto e o nome da função.

---

Podemos importar apenas uma função específica de uma biblioteca, utilizando o comando `from`:

```python
from math import sqrt

print(sqrt(25))
>>> 5.0
```

- Nestes casos, não é necessário utilizar o nome da biblioteca para chamar a função.


---

Podemos importar uma biblioteca com um nome diferente, utilizando o comando `as`:

```python
import math as m

print(m.sqrt(25))
>>> 5.0
```
ou
```python
from math import sqrt as raiz

print(raiz(25))
>>> 5.0
```

- Este recurso é útil para bibliotecas com nomes longos.

---


## Bibliotecas básicas

### `math`

Oferece funções e constantes matemáticas [doc](https://docs.python.org/3/library/math.html)

- Constantes:
```python
import math
print(math.pi) # 3.141592653589793
print(math.tau) # 6.283185307179586 (2*pi)
print(math.e)  # 2.718281828459045 (número de Euler)
print(math.inf) # infinito positivo
print(math.nan) # Not a Number (NaN)
```

---

- Matemática finita:
```python
print(math.comb(5, 2)) # 10 (combinação de 5 elementos tomados 2 a 2)
print(math.perm(5, 2)) # 20 (permutação/arranjo de 5 elementos tomados 2 a 2) 
print(math.factorial(5)) # 120 (fatorial de 5)
print(math.gcd(12, 15)) # 3 (MDC de 12 e 15)
print(math.lcm(12, 15)) # 60 (MMC de 12 e 15)
```

---

- Manipulação de números reais:
```python
print(math.ceil(3.14)) # 4 (arredonda para cima)
print(math.floor(3.14)) # 3 (arredonda para baixo)
print(math.trunc(3.14)) # 3 (trunca a parte decimal)
print(math.fabs(-3.14)) # 3.14 (valor absoluto/módulo)
```
- A diferença entre `floor` e `trunc` aparece quando o número é **negativo**.

- `round` é uma função embutida que arredonda para o inteiro mais próximo, não é necessário importar a biblioteca `math`.

---

- Testes:
```python
print(math.isfinite(3.14)) # True (é um número finito)
print(math.isinf(math.inf)) # True (é infinito)
print(math.isnan(math.nan)) # True (não é um número)
print(math.isclose(3.14, 3.14159)) # False (não são próximos)
``` 

A função `isclose` é bastante útil para comparar números reais, pois quando comparamos valores de ponto flutuante oriundos de **cálculos matemáticos** diferentes, é comum que haja uma **pequena diferença** entre eles.

---

- Funções trigonométricas: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`, `hypot`, `degrees`, `radians`

- Funções hiperbólicas: `sinh`, `cosh`, `tanh`, `asinh`, `acosh`, `atanh`
- Funções exponenciais e logarítmicas: `exp`, `expm1`, `log`, `log1p`, `log2`, `log10`, `pow`, `sqrt`

- Funções especiais: `erf`, `erfc`, `gamma`, `lgamma`, `beta`


---

# Exercícios de fixação

1. Calcule o valor de $\sqrt{2}$ utilizando a função `sqrt` da biblioteca `math`.
2. Calcule o valor de $\sin(\pi/4)$ utilizando a função `sin` da bibli library `math`.
3. Leia duas coordenadas no formato **latitude** e **longitude** e calcule a distância entre elas utilizando a formula de [Haversine](https://en.wikipedia.org/wiki/Haversine_formula).
4. Calcule o n-ésimo termo da sequência de Fibonacci utilizando a  fórmula de Binet: $F(n) = \frac{\phi^n - \psi^n}{\sqrt{5}}$, onde $\phi = \frac{1 + \sqrt{5}}{2}$ e $\psi = \frac{1 - \sqrt{5}}{2}$.
5. De quantos modos diferentes podemos escolher 3 pratos em um cardápio de 10 pratos?
6. Qual é o MDC de 12 e 15?

---

# `random`

Oferece funções para geração de números aleatórios [doc](https://docs.python.org/3/library/random.html)