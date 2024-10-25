---
marp: true
title: "Fundamentos de Programação em Python"
theme: default
class: lead
footer: "FdP - Albert E. F. Muritiba"
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

# Fundamentos de Programação (Python)

> **Objetivo:** Apresentar os conceitos básicos de lógica de programação e suas aplicações em **Python**.

![bg vertical right:35% 80%](empty.svg)

<!-- _backgroundImage: url('https://spideryzarc.github.io/labCD/bg/light_desk.jpg') -->
<!-- _footer: "" -->
---

# Raposa

Um fazendeiro viaja com uma **raposa**, uma **ovelha** e um pouco de **feno**. Certo momento ele precisa **atravessar um rio** utilizando um barco que somente suporta **ele e mais um animal ou item**. 

Se ele deixar a raposa junto com a ovelha, esta e comida. A ovelha, por sua vez, come o feno se for deixada sozinha com ele. 

Quais passos o fazendeiro deve fazer para conseguir atravessar o rio sem perder os
animais ou o feno?

![bg right:40%](images/raposa.jpeg)

---

# O Que é um Computador?

* É uma máquina de fazer contas ?
* É uma máquina de processar dados ?
* É uma máquina inteligente ?
* **É Mágica?**

<!-- imagem de um computador mágico -->
![bg right:53%](images/magica.jpeg)

---

# Fábrica de Bolos

Sua tarefa e projetar uma máquina que produza bolos de Maçãs.

**O que você precisa saber para projetar essa máquina?**


<!-- imagem de um bolo de maçã -->
![bg right:40%](images/bolo.jpg)

---

##### <!--fit--> Como se faz um bolo de maçã!!

---

* Você aprendeu a fazer um bolo de maçã.
* Juntou seu diploma de engenharia e, depois de algumas tentativas, conseguiu fazer sua máquina de fazer bolos de maçã.
* Sua maquina recebe maçãs açúcar, farinha, manteiga e canela. E produz bolos.     
*  **Sucesso!!**
  

![bg left:45%](images/maquina.jpeg)

---

Mas o tempo da colheita de maçãs acabou e agora você precisa fazer bolos de **abacaxi**.

**O que você faz?**

* Coloca abacaxis na máquina e vê o que acontece?
* Desmonta a máquina e tenta fazer outra?
* Projeta e constrói uma nova máquina?
* Outra coisa?

<!-- imagem de um bolos de abacaxi -->
![bg right:40%](images/bolo_abacaxi.jpeg)

---

# E se ...

Você inventasse uma máquina que pudesse receber os **ingredientes** e a **receita** e produzir o bolo seguindo a receita?

* Nesta maquina, você deve fornecer os ingredientes e a receita.
* **Não** é uma máquina de fazer bolos de maçã ou de abacaxi.

---


##### <!--fit--> É uma máquina de executar receitas!


---

# O que é um Computador?

- É uma máquina que executa **instruções**.
- As instruções são fornecidas por um **programa**.
- O programa é um conjunto de **algoritmos**.
- Um algoritmo é uma sequência de **passos** para resolver um problema.
  
---

# Metaforicamente

- A **entrada** são os ingredientes.
- A **receita** é o **algoritmo** ou **programa**.
- A **saída** é o bolo.

##### <!--fit --> Saber **programar** é saber **escrever a receita** para <br> a **máquina** que faz o **bolo**.


---

# Python

Neste curso, vamos aprender a **programar** em **Python**, em seguida, aprenderemos um pouco de **C**.


![bg right:40% 50%](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)

---

## Histórico

- **Guido Van Rossum**, criou o Python. Ele começou em **1989** no Centrum Wiskunde & Informatica (CWI), inicialmente como um projeto de *hobby* para se manter ocupado durante o **Natal**. 
- O nome da linguagem foi inspirado no programa de TV da BBC “**Monty Python’s Flying Circus**”, porque Guido Van Rossum era um grande fã do programa. 

![bg right:40% ](images/silly_walks.jpg)

---

### Principais Marcos

- **1991** - Primeira versão do código Python (versão 0.9.0) foi publicada.
- **1994** - O Python 1.0 foi lançado com novas funções para processar listas, como **mapear**, **filtrar** e **reduzir**.
- **2000** - O Python 2.0 foi lançado com novos recursos úteis, como suporte para caracteres [Unicode](https://pt.wikipedia.org/wiki/Unicode) e um modo mais rápido de percorrer uma lista.
- **2008** - foi lançado o **Python 3.0**. 

[Fonte](https://aws.amazon.com/pt/what-is/python/#:~:text=altera%C3%A7%C3%B5es%20no%20c%C3%B3digo.-,Qual%20%C3%A9%20a%20hist%C3%B3ria%20do%20Python%3F,manter%20ocupado%20durante%20o%20Natal.)

![bg right:15% fit drop-shadow 90%](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png)


---

## Popularidade e Uso

![Tiobe Index h:450 drop-shadow](images/tiobe.png)
O índice [Tiobe](https://www.tiobe.com/tiobe-index/) é uma medida da popularidade de uma linguagem de programação com base na **quantidade de pesquisas** na web.

---

###### <!-- fit --> Quanto **mais popular**, **mais fácil** de encontrar <br> **ajuda** e **recursos**!

---

## Por que Python?

* **Simples e Fácil de Aprender**
* **Versátil e Poderoso**
* **Comunidade Ativa**
* **Grande Biblioteca Padrão**
* **Open Source**
* **Multiplataforma**

---

## Qual a Grande Desvantagem do Python?

##### <!--fit--> **Python é lento!**

> Quando estivermos mais avançados, **me lembre** de falar sobre isso.

---

# Formas de Utilizar Python

- **Interativo**: **Shell** ou **Console**, os comandos são executados imediatamente.
- **Script**: Arquivo com extensão `.py` que contém um conjunto de instruções.
- **Notebook**: Ambiente interativo que permite combinar texto, código e gráficos. (Jupyter, Google Colab, etc.)

> Neste curso, vamos focar em **scripts**.

---

# Ambiente de Desenvolvimento (IDE)

- **IDE** (Integrated Development Environment) é um ambiente de desenvolvimento integrado.
- Exemplos: **PyCharm**, **VSCode**, **Jupyter Notebook**, **Google Colab**, **Spyder**, **IDLE**.

> Neste curso, vamos utilizar o **VSCode**.

---

# Instalação do Python

- **Windows**: [Python.org](https://www.python.org/downloads/windows/)
- **Linux**: `sudo apt install python3`
- **online**: [online-python](https://www.online-python.com/) entre outros.
Em caso de dúvidas, há uma infinidade de tutoriais na internet.

---

# Primeiro Programa em Python

Crie um arquivo chamado `aula1.py` e adicione o seguinte código:

```python
print("Hello, World!")
```

> **print()**: Função que exibe uma mensagem na tela. [doc](https://docs.python.org/3/library/functions.html#print)
> Os arquivos `.py` são chamados de **scripts** e são simplesmente arquivos de texto plenos.

---

Num *script* Python, você pode escrever várias instruções, uma após a outra.

```python 
print("Hello, World!")
print("Python é legal!")
print("Vamos aprender a programar!")
>>
Hello, World!
Python é legal!
Vamos aprender a programar!
```

As instruções são executadas **sequencialmente**, de cima para baixo.

---
## Regras Básicas

- As instruções devem estar **alinhadas**.

  ```python
  print("Hello, World!")
    print("Esta instrução está errada!")
  ```

- **Duas instruções** não podem estar na mesma linha.
  
  ```python
  print("Hello, World!") print("Esta instrução está errada!")
  ```
 
---

# Conceitos Básicos de Programação

* **Saída**: Exibir dados para o usuário.
* **Atribuição**: Armazenar dados em variáveis e realizar operações.
* **Entrada**: Receber dados do usuário.
* **Seleção**: Tomar decisões com base em condições.
* **Repetição**: Executar um bloco de código várias vezes.
* **Funções**: Agrupar instruções em um bloco reutilizável.

> Vamos aprender cada um desses conceitos ao longo do curso.

---

# Sintaxe vs Semântica

* **Sintaxe**: Conjunto de regras que definem a estrutura de um programa (gramática).
* **Semântica**: Significado das instruções e como elas são executadas.

Um programa com **erro de sintaxe não é executado**. 
Um programa com **erro de semântica** é executado, mas produz **resultados incorretos**.
<br>
> Embora material descreva algumas regras de sintaxe explicitamente, a maioria das regras acaba sendo aprendida de forma implícita, com a **prática**.

---

# Saída de Dados

- **print()**: Exibe uma mensagem na tela. [doc](https://docs.python.org/3/library/functions.html#print)

```python
print("Hello, World!")
>> 
Hello, World!
```


---

```python
print("Hello, World!")
```
<br>

* Essa estrutura é chamada de **comando** ou **instrução**.
* `print` é uma **função** que exibe uma mensagem na tela.
* O texto entre aspas é chamado de **string**.
* Os elementos entre parênteses são chamados de **argumentos** ou **parâmetros**.
<br><br>

> Aprenderemos a fazer nossas próprias funções mais adiante. Por enquanto, vamos aprender a reconhecê-las por seus parênteses.

---

```python
print("Hello, World!")
```
**Seja curioso!** Você **não** tem capacidade de **quebrar o computador programando. 
### Experimente!
- O que acontece se você remover as aspas?
- O que acontece se você remover os parênteses?
- O que acontece se você remover a palavra `print`?
- O que acontece se você usar a palavra `Print` ou `PRINT`?
- O que acontece se você usar aspas simples?
- O que acontece se você colocar uns espaços a mais?

> O que afeta a **sintaxe** e o que afeta a **semântica**?

---

# Atribuição de Variáveis

As variáveis são abstrações que representam valores armazenados na memória de trabalho do computador (RAM).

```python
mensagem = "Hello, World!"
x = 10
y = 3.14
print(mensagem, x, y)
>> 
Hello, World! 10 3.14
```
> No Python, basta **atribuir** um valor a um **identificador** para criar uma variável.

---

## Identificadores

- **Identificador**: Nome dado a uma variável, função, classe, módulo, etc.
- **Regras**:
  - Deve começar com uma letra ou `_`.
  - Pode conter letras, números e `_`.
  - Não pode conter espaços ou caracteres especiais.
  - **Case-sensitive** (diferencia maiúsculas de minúsculas).
<br>
> Embora seja possível usar acentos e caracteres especiais, **não é recomendado**.	

---

## Tipos de Dados

* Associado a cada variável, existe um **tipo de dado** que determina o que a variável pode armazenar.
* Na maioria das vezes, nós não precisamos nos preocupar com isso, pois o Python é uma linguagem **dinamicamente tipada**.
* Ou seja, o Python **infere** o tipo de dado automaticamente.
* Uma variável **pode mudar de tipo** ao longo do programa.
* Os tipos definem as **operações** que podem ser realizadas com os dados.

---

### Tipos Básicos

- Numéricos:
  - **int**: Números inteiros.
  - **float**: Números de ponto flutuante.
  - **complex**: Números complexos.
- **str**: Sequência de caracteres (*string*).
- **bool**: Valores lógicos (*True* ou *False*).
- **None**: Valor nulo.
<br>
>Obs.: Existem outros tipos de dados mais complexos, como listas, tuplas, dicionários, conjuntos, etc.


---

#### Inteiros

Valores inteiros, positivos ou negativos.

* Exemplo de literais inteiros:
  ```python
  x = 10
  y = -5
  z = 0
  w = int("10")
  ```
* Inteiros muito grandes podem ser representados sem problemas.
  ```python
  x = 1234567890123456789012345678901234567890
  ```
* Você pode usar `_` para separar os dígitos.
  ```python
  x = 1_000_000
  ```

---

#### Ponto Flutuante

* Ponto flutuante (*float*) é forma que o computador **emula** números reais.
* Computadores não podem representar todos os números reais, pois é uma máquina **finita**.
* Por isso, números de ponto flutuante são **aproximações**.
* Exemplo de ponto flutuante:
  ```python
  x = 3.14
  y = -0.5
  z = 35e-3
  w = float("3.14")
  ```

---

#### Complexos

* Números complexos são da forma `a + bj`, onde `a` e `b` são números reais e `j` é a unidade imaginária.
  $$ j^2 = -1 $$
* Exemplo de complexos:
  ```python
  x = 3 + 4j
  y = 1 - 2j
  z = complex(2, -3)
  w = complex("5-6j")
  ```

---

### Operações Aritméticas

- **Adição**: `+`
- **Subtração**: `-`
- **Multiplicação**: `*`
- **Divisão**: `/`
- **Divisão Inteira**: `//`
- **Resto da Divisão**: `%`
- **Exponenciação**: `**`


---

### Divisão

- A **divisão** em Python é um pouco diferente.
- O operador `/` sempre retorna um número de ponto flutuante.
- Para obter a parte inteira da divisão, use `//`.

```python
10 / 3
>> 3.3333333333333335
10 // 3
>> 3
```

---

### Resto da Divisão

- O operador `%` retorna o **resto** da divisão.
- Também conhecido como **módulo** ou **mod**.

```python
10 % 3
>> 1
-10 % 3
>> 2
```

> Quando o dividendo é negativo, o sinal do resto é o mesmo do divisor. 
> $$ -10 = 3 \times (-4) + 2 $$ 

---

### Teste Surpresa

Responda sem executar o código.

```python
x = 3
y = x % 2
z = y % 2
print(z)
>>
?????
```

---

### Exponenciação

- O operador `**` realiza a exponenciação.
  $$ 2^3 = 8 $$

```python
2 ** 3
>> 8
```
- Para raízes, use a exponenciação fracionária.
  $$ \sqrt{9} = 9^{1/2} = 3 $$

```python
9 ** 0.5
>> 3.0
```

---

### Ordem de Precedência

- **Parênteses** `()`
- **Exponenciação** `**`
- **Multiplicação** `*`, **Divisão** `/`, **Divisão Inteira** `//`, **Resto da Divisão** `%`
- **Adição** `+`, **Subtração** `-`
- **Mesma precedência**: da esquerda para a direita.
<br>
> Na dúvida, use **parênteses**!

---

### Uso dos Parênteses

* Ao contrário da algebra, as linguagens de programação costumam permitir **apenas** o uso de **parênteses**.
* Colchetes `[]` e chaves `{}` são usados para **outras finalidades**.

$$ 5 \times \frac{\frac{3}{5+3}} {2^3} $$

```python
5 * (3 / (5 + 3)) / 2 ** 3
>> 0.234375
```
Na dúvida, use **parênteses**!
```python
5 * ((3 / (5 + 3)) /(2 ** 3))
>> 0.234375
```

---

## Tipo Lógico (Booleano)

- **bool**: Tipo de dado que representa valores lógicos.
- Pode ser **True** ou **False**.

```python
x = True
y = False
z = bool("True")
w = bool(0)
```

---

### Operadores Lógicos (`not`, `and`, `or`)

- `not`: Negação lógica. Inverte o valor.

| `x` | `not x` |
|-----|---------|
| True | False |
| False | True |

```python	
x = True
y = not x
print(y)
>> False
```

---

- `and`: Conjunção lógica. Equivale a **E** da lógica proposicional.


| `x` | `y` | `x and y` |
|-----|-----|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

```python
x = True
y = False
z = x and y
print(z)
>> False
```

---

- `or`: Disjunção lógica. Equivale a **OU** da lógica proposicional.

| `x` | `y` | `x or y` |
|-----|-----|----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

```python
x = True
y = False
z = x or y
print(z)
>> True
```

---

### Operadores Relacionais

**Operadores relacionais** comparam dois valores e retornam um valor lógico.

- **Igualdade**: `==`
- **Diferença**: `!=`
- **Maior que**: `>`
- **Menor que**: `<`
- **Maior ou igual**: `>=`
- **Menor ou igual**: `<=`

```python
x = 10
y = 5
z = x > y
print(z)
>> True
```

---

### Teste Surpresa

Responda sem executar o código.

```python
x = 3
y = 5
z = x == y
w = x != y
print(z, w)
>>
?????
```

---

### Observações sobre Operadores Relacionais

- **Igualdade**: `==` (dois sinais de igual).
- **Atribuição**: `=` (um sinal de igual).

Uma boa prática é *ler* `==` como **igual a**, e `=` como **recebe**.

Exemplo:
```python
x = 10
```
Lê-se: **x recebe 10**.

---

### Outra Observação

**Não é comum em outras linguagens**, mas em Python é possível **encadear** operadores relacionais.

```python
x = 10
y = 0 < x < 20
print(y)
>> True
```

---

# Entrada de Dados

- **input()**: Recebe uma entrada do usuário.
- **Retorna** uma **string**.
- **Exemplo**:
  ```python
  nome = input("Digite seu nome: ")
  print("Olá,", nome)
  ```

---

## Conversão de Tipos

Devemos **converter** a entrada para o tipo desejado, se necessário.

- **int()**: Converte para inteiro.
- **float()**: Converte para ponto flutuante.

```python
x = input("Digite um número: ")
y = int(x)
print(y + 1)
```

---

##### O programa abaixo está correto?

O programa abaixo deve ler um número digitado pelo usuário e exibir o dobro desse número.

```python
x = input("Digite um número: ")
y = x * 2
print(y)
```
- A saída é o dobro do número digitado?
- Ou a saída é o número digitado duas vezes?
- Por que isso acontece?


--- 

# Exercícios, escreva um programa que:

1. exiba a mensagem "Hello, World!".
2. calcule e imprima a área de um círculo de raio 5.
3. leia um número inteiro e exiba o seu sucessor e antecessor.
4. leia uma temperatura em Celsius e exiba a temperatura em Fahrenheit.
5. leia um peso e uma altura e exiba o IMC.
6. leia um número e exiba o seu quadrado, cubo e raiz quadrada.
7. leia um valor inteiro e exiba a sua decomposição em centenas, dezenas e unidades (use as operações de divisão e módulo).
8. leia um quantidade de segundos e exiba o tempo em horas, minutos e segundos (use as operações de divisão e módulo).
9. leia três valores e exiba a média aritmética.
  

---

## Tipo *String*

- `str`: Sequência de caracteres.
- **Literais**:
  - Aspas duplas: `"Hello, World!"`
  - Aspas simples: `'Hello, World!'`
  - Aspas triplas: `'''Hello, World!'''` ou `"""Hello, World!"""`
- **Operações**: Concatenação `+`, Repetição `*`.

> Veremos bem mais sobre *strings* em aulas futuras, por enquanto, vamos focar em **números**.

---

# Comentários

- **Comentários** são trechos de texto ignorados pelo interpretador.
- São utilizados para **documentar** o código.
- As vezes, são utilizados para **desativar** trechos de código para **depuração**.
- Em Python, os comentários são iniciados com `#`.

```python
# Este é um comentário
print("Hello, World!")  # Este é outro comentário
```

> Tudo após o `#` é ignorado pelo interpretador.

---

## Comentários de Múltiplas Linhas

- Python não possui um **comentário de múltiplas linhas**,
- mas é possível utilizar **strings de múltiplas linhas**.

```python
"""
Este é um comentário
de múltiplas linhas.
"""
print("Hello, World!")
```

> As strings de múltiplas linhas são **ignoradas** pelo interpretador, já que não são **atribuídas** a nenhuma variável.

---

# Seleção 

- **Seleção** é a capacidade de **tomar decisões** com base em **condições**.
- **Condição**: Expressão que retorna um valor lógico.
- **Estrutura de Seleção**:
  ```python
  if condicao:
      # bloco de código
  ```

---

## Estrutura `if`

- Se a **condição** for verdadeira, o **bloco de código** é executado.
- Se a **condição** for falsa, o **bloco de código** é ignorado.

```python
x = 10
if x > 5:
    print("x é maior que 5")
print("Fim")
```

---

## Bloco de Código

Antes de continuar, vamos falar sobre **bloco de código**.

- Um **bloco de código** é um conjunto de instruções **alinhadas**.
- O **alinhamento** é feito com **espaços** ou **tabulações**. (Dê preferência a **tabulações**).
- Ao contrário de outras linguagens, Python **não** possui **delimitadores de bloco** (como `{}` nas linguagens C-like).
- Portanto, o **alinhamento** é **obrigatório** e interfere na **semântica** do código.

---

## Exemplo de Bloco de Código

```python
x = 10
if x > 5:
    print("x é maior que 5")
    print("Isso está dentro do bloco")
print("Isto não está no bloco")
```
Blocos aninhados:
```python
x = 10
if x > 5:
    print("x é maior que 5")
    if x > 8:
        print("x é maior que 8")
        if x < 15:
            print("x é menor que 15")
print("Fim")
```

---

# Exemplos Errados

```python
if x > 5:
print("x é maior que 5")
```
```python
if x > 5:
    print("x é maior que 5")
  print("Isso está errado")
```
```python
if x > 5:
print("x é maior que 5")
  print("Isso está errado")
```

---

- Um comando na mesma linha é permitido, desde que seja **uma única instrução**.

```python
if x > 5: print("x é maior que 5")
```

- Um bloco vazio pode ser representado por `pass`.

```python
if x > 5:
    pass
print("Fim")    
```

---

## Estrutura `if-else`

- Se a **condição** for verdadeira, somente o **bloco de código 1** é executado.
- Se a **condição** for falsa, somente o **bloco de código 2** é executado.

```python
if condicao:
    # bloco de código 1
else:
    # bloco de código 2
```

---

## Exemplo de `if-else`

```python
x = 10
if x > 5:
    print("x é maior que 5")
else:
    print("x é menor ou igual a 5")
print("Fim")
```

---

## Estrutura `if-elif-else`

- Devido a exigência de identação do Python, muitos se e senão aninhados podem tornar o código difícil de ler.
```python	
if condicao1:
    # bloco de código 1
else:
    if condicao2:
        # bloco de código 2
    else:
        if condicao3:
            # bloco de código 3
        else:
            if condicao4:
                # bloco de código 4
            else:
                if condicao5:
                    # bloco de código 5
                else:
                    # bloco de código 6
```

---

- Para resolver isso, o Python possui a estrutura `elif`.
- `elif` é uma abreviação de **else if**.

```python
if condicao1:
    # bloco de código 1
elif condicao2:
    # bloco de código 2
elif condicao3:
    # bloco de código 3
elif condicao4:
    # bloco de código 4
elif condicao5:
    # bloco de código 5
else:
    # bloco de código 6  
```

> Há uma outra estrutura chamada `match-case` que é mais recente e mais poderosa, mas não vamos abordá-la mais a frente.

---

## Exemplo de `if-elif-else`

```python
nota = float(input("Digite a nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

# Exercícios, escreva um programa que:

1. leia um número e exiba se ele é par ou ímpar.
2. leia um número e exiba se ele é positivo, negativo ou zero.
3. leia três números e exiba o maior e o menor.
4. leia os valores de `a`, `b` e `c` e exiba as raízes da equação de segundo grau ($ax^2+bx+c=0$).
5. leia três valores e exiba se eles podem formar um triângulo. Caso positivo, exiba o tipo de triângulo (equilátero, isósceles ou escaleno). Dica: para formar um triângulo, a soma de dois lados menores deve ser maior que o terceiro lado.
6. leia três valores e exiba a mediana.

---

6. leia o peso e a altura e exiba a classificação do IMC, conforme a tabela abaixo:

| IMC | Classificação |
|-----|---------------|
| < 18.5 | Abaixo do peso |
| 18.5 - 25 | Peso normal |
| 25 - 30 | Sobrepeso |
| 30 - 35 | Obesidade grau 1 |
| 35 - 40 | Obesidade grau 2 |
| >= 40 | Obesidade grau 3 |

---

# Repetição

- **Repetição** é a capacidade de **executar um bloco de código várias vezes**.



