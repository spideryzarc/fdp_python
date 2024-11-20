---
marp: true
title: "Funções em Python"
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

# Funções em Python

Quando nos deparamos com um problema complexo, é comum quebrá-lo em partes menores. Cada parte é resolvida separadamente e, ao final, as soluções são combinadas para resolver o problema original.

Chamamos essas partes menores de **funções**, sub-rotinas ou procedimentos.

![bg right:40%](empty.svg)

---

## Definição de Função

* Uma função é um bloco de código que executa uma tarefa específica. 
* Possui um **nome**, que é usado para chamá-la.
* Pode receber **parâmetros** de entrada.
* Pode **retornar** um valor de **saída**.
* Sintaxe da definição de uma função básica:
    ```python
    def nome_da_funcao(parametro1, parametro2):
        # bloco de código
        return valor_de_saida
    ```
* Sintaxe da chamada de uma função:
    ```python
    nome_da_funcao(valor1, valor2)
    ```

---

## Semântica de Funções

- A definição de uma função não executa imediatamente, o código dentro da função é executado somente quando a função é chamada.
- O programa segue o fluxo de execução normal até encontrar uma chamada de função.
- A execução do programa é transferida para a função chamada.
- Após a execução da função, o controle é retornado ao ponto de chamada.
- Se a função retorna um valor, este **'substitui'** a chamada da função.


![bg right:30%](empty.svg)

---

## Uso mais comum de funções

* **Reutilização de código**: evita repetição de código.
* **Organização**: facilita a leitura e manutenção do código.
* **Abstração**: esconde detalhes de implementação.

---

### Exemplo de Reutilização de Código
O código abaixo ler a nota de um aluno e uma pontuação extra, e imprime a situação do aluno (aprovado, recuperação ou reprovado) sem e com a pontuação extra.

```python
def status(nota):
    if nota >= 7:
        return 'Aprovado'
    elif nota >= 5:
        return 'Recuperação'
    else:
        return 'Reprovado'
# fluxo principal
nota = float(input('Digite a nota: '))
ponto_extra = float(input('Digite o ponto extra: '))
print('Situação sem ponto extra: ', status(nota))
print('Situação com ponto extra: ', status(nota+ponto_extra))
```
Observer que o programador teria que **repetir** o código de decisão para cada caso, sem a função `status`.

---

### Exemplo de Organização
O código abaixo lê um número e imprime se ele é par ou ímpar.

```python
def par_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
# fluxo principal
numero = int(input('Digite um número: '))
print('O número é', par_impar(numero))
```
A função `par_impar` organiza o código de decisão, facilitando a leitura e manutenção do código.
- Quando lemos a **definição da função**, fica **fácil entender** o que ela faz.
- Quando lemos o **fluxo principal**, fica **fácil entende**r o que o programa como um todo faz.

---

### Exemplo de Abstração
O código abaixo lê dois números e imprime a fração simplificada.
```python
def mdc(a, b):
    # Algortimo de Euclides para calcular o MDC
    while b != 0:
        a, b = b, a % b
    return a
# fluxo principal
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador: '))
mdc = mdc(numerador, denominador)
print('Fracao simplificada:', numerador//mdc, '/', denominador//mdc)
```
- Compreender como o algoritmo de Euclides funciona **não** é uma tarefa **trivial**.
- Mas, uma vez que você "**aceita**" que a função `mdc` faz o que promete, você pode usá-la sem se preocupar com os **detalhes** de implementação.

---

#### <!-- fit --> Quem vê as árvores não vê a floresta

Na programação, o conceito de abstração é essencial para lidar com a complexidade. Abstrair significa ocultar os detalhes de implementação, destacando apenas os aspectos mais relevantes. Essa abordagem permite ao programador focar no problema principal, em vez de se perder nos intricados detalhes técnicos, promovendo soluções mais claras e eficientes.

---

## Definindo Funções

Já usamos funções desde o início do curso, como `print`, `input`, `int`, `float`, `str`, `len`, `range`, etc. É hora de aprender a criar nossas próprias funções.

```python
def seja_educado():
    print('Como você está?')
    print('Tenha um bom dia!')
# fluxo principal
seja_educado()
seja_educado()
```
- A função `seja_educado` é bastante simples, não recebe parâmetros e não retorna valores. Ela apenas imprime duas mensagens educadas.
- A função é chamada duas vezes no **fluxo principal**. Por isso, as mensagens são impressas duas vezes.
- Ela sempre faz a mesma coisa.

---

### Parâmetros

Podemos passar informações para uma função através de parâmetros. Os parâmetros são variáveis que recebem valores quando a função é chamada.

```python
def seja_educado(nome):
    print(f'Como você está, {nome}?')
    print('Tenha um bom dia!')
# fluxo principal
seja_educado('Maria')
seja_educado('João')
```
- A função `seja_educado` agora recebe um parâmetro `nome`. Esse parâmetro é usado para personalizar a mensagem.
- A função é chamada duas vezes no **fluxo principal**, passando nomes diferentes. Por isso, as mensagens são personalizadas.
- A função agora é mais **genérica** e **reutilizável**.

---

### Retorno

Uma função pode retornar um valor de saída. O valor de retorno é especificado com a palavra-chave `return`. Ao encontrar um `return`, a função é encerrada e o valor "**substitui**" a chamada da função.

```python
def fat(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
# fluxo principal
resultado = fat(5) + fat(3) + fat(4)
print('5! + 3! + 4! =', resultado)
```
- A função é chamada três vezes no **fluxo principal**, passando números diferentes. O retorno é somado e impresso.
- A função é **reutilizável** e **abstrai** o cálculo do fatorial. 

---

- `return` encerra a função e retorna um valor.
- `return` pode ser usado em qualquer lugar da função.
- `return` pode aparecer mais de uma vez em uma função.
- `return` pode ser usado para encerrar a função sem retornar um valor.
- Se você retornar uma tupla, é como se você estivesse **retornando vários valores**, o que é uma vantagem do Python em relação a outras linguagens.

---

### Exemplo de Retorno de Múltiplos Valores

```python
def min_max(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo
# fluxo principal
numeros = [10, 5, 7, 3, 8]
menor, maior = min_max(numeros)
print('Menor:', menor)
print('Maior:', maior)
```
- A função `min_max` retorna o menor e o maior valor de uma lista.
- No **fluxo principal**, os valores de retorno são atribuídos a duas variáveis, que são impressas.
- O Python permite **desempacotar** os valores de retorno em variáveis separadas.

---

### Exemplo de `return` em Qualquer Lugar

```python
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# fluxo principal
numero = int(input('Digite um número: '))
if eh_primo(numero):
    print('É primo')
else:
    print('Não é primo')
```

Observe que não há necessidade de vários `else` pois `return` encerra a função.

---

### Exemplo de `return` sem Valor

```python
def seja_educado(nome):
    if nome == 'Albert':
        return
    print(f'Como você está, {nome}?')
    print('Tenha um bom dia!')
# fluxo principal
seja_educado('Maria')
seja_educado('Albert')
seja_educado('João')
```
- A função `seja_educado` não imprime nada se o nome for 'Albert'.
- O `return` sem valor encerra a função imediatamente, mesmo retornando nada.

---

## Escopo de Variáveis

O **escopo** de uma variável é a região do programa onde a variável é visível e pode ser usada. Em Python, existem dois tipos de escopo:

- **Escopo Local**: variáveis definidas dentro de uma função são visíveis apenas dentro da função.
- **Escopo Global**: variáveis definidas fora de qualquer função são visíveis em todo o programa.

Imagine que, para usar uma função, você precisasse saber **o nome de todas as variáveis** que ela usa internamente. O conceito de **escopo** permite que você use funções sem **se preocupar** com as variáveis internas.

---

```python
def funcao():
    x = 10
    print(x)
# fluxo principal
funcao()
print(x)
```
- A variável `x` é definida dentro da função `funcao`, portanto, é uma variável local.
- A variável `x` não é visível fora da função, causando um erro ao tentar imprimi-la.
- Variáveis locais são **destruídas** quando a função termina.
- Variáveis globais são **destruídas** quando o programa termina.
 