---
marp: true
title: "Introdução à Linguagem C"
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

# Introdução à Linguagem C

Neste módulo, vamos aprender os conceitos básicos da linguagem de programação C, sob a perspectiva de um programador iniciante Python.


![bg right:40% 80%](https://upload.wikimedia.org/wikipedia/commons/3/35/The_C_Programming_Language_logo.svg)

---

## O que é C?

- Linguagem de programação de propósito geral e estruturada
- Desenvolvida por Dennis Ritchie em 1972
- Base para diversas outras linguagens
- Muito utilizada em sistemas operacionais e aplicações de baixo nível
- Linguagem de médio nível (permite manipulação de hardware)
- Compilada
- Sintaxe simples e elegante

---

# Compilação

Ao contrário de linguagens interpretadas, como Python, C é uma linguagem compilada. Isso significa que o código fonte é traduzido para código de máquina antes de ser executado.

- **Código fonte**: código escrito pelo programador em um arquivo de texto (extensão `.c`)
- **Código objeto**: código de máquina gerado pelo compilador (extensão `.exe` no Windows)
- **Compilador**: programa que traduz o código fonte para código objeto
- **Linker**: programa que junta o código objeto com bibliotecas externas para gerar o executável

---

# Comparação entre Python e C

## Compilado vs Interpretado

- **Python**: código é executado linha a linha, sem necessidade de compilação
- **C**: código é traduzido para código de máquina antes de ser executado
- **Vantagens de C**: execução **muito mais rápida**, controle total sobre o *hardware*
- **Desvantagens de C**: menor produtividade, menor flexibilidade na sintaxe

---

## Tipos estáticos vs dinâmicos

- **Python**: tipos das variáveis são inferidos em tempo de execução
- **C**: tipos das variáveis são definidos em tempo de compilação
- **Vantagens de C**: maior eficiência, menor uso de memória
- **Desvantagens de C**: menor produtividade, código mais complexo

---

## Sintaxe 

- **Python**: Muito flexível, muitas formas de se fazer a mesma coisa, muitas bibliotecas, muitas funções embutidas, muitas palavras-chave
- **C**: Sintaxe mais rígida, menos funções embutidas, menos palavras-chave, menos bibliotecas
- **Vantagens de C**: código mais enxuto, menos ambiguidades, curva de aprendizado mais curta. Dificilmente um programador médio vai se deparar com um código C com sintaxe não familiar.
- **Desvantagens de C**: menor flexibilidade, menos recursos embutidos.

---

## Conclusão

- **Python**: linguagem de alto nível, fácil de aprender, produtividade alta, execução lenta
- **C**: linguagem de médio nível, mais difícil de aprender, produtividade baixa, execução rápida
- **Quando usar C**: aplicações de baixo nível, sistemas operacionais, drivers de dispositivos, aplicações que precisam de alta performance e controle total sobre o hardware (jogos, sistemas embarcados, etc.)
- **Quando usar Python**: aplicações de alto nível, prototipagem, aplicações web, ciência de dados, automação, etc.

---

# Estrutura de um programa C

```c
#include <stdio.h>
int main(){
    printf("Hello, World!");
    return 0;
}
```

- **`#include <stdio.h>`**: inclui a biblioteca padrão de entrada e saída
- **`int main()`**: função principal do programa
- **`printf("Hello, World!");`**: função que imprime uma mensagem na tela
- **`return 0;`**: retorna 0 para o sistema operacional
- **`{}`**: delimitam um bloco de código
- **`;`**: indica o fim de uma instrução
  

---

# Função `main`

- **`int main()`**: função principal do programa.
- *C* começa a execução pela função `main`.
- `int` indica que a função retorna um valor inteiro.
- `()` indica que a função não recebe argumentos.
- `return 0;` indica que o programa terminou com sucesso.
- `{}` delimitam o bloco de código da função.


---

# Compilando um programa C

Para compilar um programa C, você precisa de um compilador. O compilador mais comum é o `gcc` (GNU Compiler Collection).

Para compilar o programa `hello.c`:

```bash
gcc hello.c -o hello
```

Isso vai gerar um arquivo executável chamado `hello`. Para executar o programa:

```bash
./hello
```

> Neste curso usaremos o ambiente online [onlinegdb](https://www.onlinegdb.com/) para compilar e executar programas C de forma didática.

---

# Blocos de código

- *C* não se importa com a indentação do código.
- Blocos de código são delimitados por chaves `{}` quando possuem mais de uma linha.
- Bloco de código de uma única linha não precisa de chaves.
- Comandos são separados por ponto e vírgula `;`.
- Um programa *C* pode ser escrito em uma única linha.

```c
#include <stdio.h>
int main(){printf("Hello, World!");return 0;}
```

---

# Comentários

- Comentários são trechos de texto ignorados pelo compilador.
- São usados para documentar o código.
- Em *C*, comentários de uma linha são feitos com `//`.
- Comentários de múltiplas linhas são feitos com `/*` e `*/`.

```c
#include <stdio.h>
/* Este é um comentário 
de múltiplas linhas */
int main(){
    // Imprime "Hello, World!"
    printf("Hello, World!");
    return 0;
}
```

---

# Variáveis

- Variáveis são espaços de memória que armazenam valores.
- Em *C*, as variáveis precisam ser declaradas antes de serem usadas.
- A declaração de variáveis segue o padrão `tipo nome;`.
- Tipos de variáveis em *C*: `int`, `float`, `double`, `char`, `bool`, etc.

```c
    int x; // Declaração de uma variável inteira
    int a,b,c; // Declaração de múltiplas variáveis inteiras
    int d = 10; // Declaração e inicialização de uma variável inteira
    int e = 10, f = 20; // Declaração e inicialização de múltiplas variáveis inteiras    
```

> Quando um variável é declarada sem ser inicializada, ela contém um valor indefinido (lixo de memória).


---

# Tipos de variáveis

| Tipo | Tamanho | *range* | literal | conversão |
|------|---------|---------|---------|-----------|
| `char` | 1 byte | -128 a 127 | `'a'` | `%c` |
| `short` | 2 bytes | -32.768 a 32.767 | `10` | `%hd` |
| `int` | 4 bytes | -2.147.483.648 a 2.147.483.647 | `10` | `%d` |
| `long` | 8 bytes | -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807 | `10` | `%ld` |
| `float` | 4 bytes | 1.2E-38 a 3.4E+38 | `10.5` | `%f` |
| `double` | 8 bytes | 2.3E-308 a 1.7E+308 | `10.5` | `%lf` |

---

# Modificador `unsigned`

- **`unsigned`**: não permite valores negativos

```c
    unsigned int x; // Variável inteira sem sinal (0 a 4.294.967.295)
```

---

Na prática, você vai usar principalmente os tipos `int`, `double` e `char`. Os outros tipos são usados em situações específicas.

---

# Operadores aritméticos

- *C* suporta os operadores aritméticos básicos: `+`, `-`, `*`, `/`, `%`.
- *C* não suporta operações com números complexos, matrizes, vetores, etc.
- *C* não possui operadores de potenciação e radiciação.

```c
int a = 10, b = 20;
int c = a + b; // Soma
int d = a - b; // Subtração
int e = a * b; // Multiplicação
int f = a / b; // Divisão
int g = a % b; // Resto da divisão
```

---

## Divisão inteira

- Ao contrário de Python, *C* **não** possui um operador específico para divisão **inteira** (`//`).
- O tipo de divisão é determinado pelo tipo das variáveis ou literais  envolvidas.
- Se ambos os operandos são inteiros, a divisão é inteira.
- Se pelo menos um dos operandos é `float` ou `double`, a divisão é de ponto flutuante.

```c
int a = 10, b = 3;
int c = a / b; // c = 3
```

```c
float x = 10, y = 3;
float z = x / y; // z = 3.333333
```

---

# Operadores de incremento e decremento

- *C* suporta os operadores de incremento `++` e decremento `--`.
- O operador de incremento `++` adiciona 1 à variável.
- O operador de decremento `--` subtrai 1 da variável.

```c
int a = 10;
a++; // a = 11
a--; // a = 10
```

- Os operadores de incremento e decremento podem ser usados antes ou depois da variável.

```c
int a = 10;
int b = ++a; // a = 11, b = 11
int c = a--; // a = 10, c = 11
```

---

# Operadores de atribuição

- *C* suporta os operadores de atribuição `=`, `+=`, `-=`, `*=`, `/=`, `%=`.
- Os operadores de atribuição combinam uma operação com a atribuição.
- Por exemplo, `a += b` é equivalente a `a = a + b`.

```c
int a = 10;
a += 5; // a = 15
a -= 5; // a = 10
a *= 5; // a = 50
a /= 5; // a = 10
a %= 5; // a = 0
```

---

# Operadores de comparação

- *C* suporta os operadores de comparação `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Os operadores de comparação retornam um valor booleano (`true` ou `false`).

```c
int a = 10, b = 20;
if (a == b) printf("a é igual a b");
if (a != b) printf("a é diferente de b");
if (a > b) printf("a é maior que b");
if (a < b) printf("a é menor que b");
if (a >= b) printf("a é maior ou igual a b");
if (a <= b) printf("a é menor ou igual a b");    
```

> *C* não supporta o tipo `bool`. Valores booleanos são representados por `0` (falso) e `1` (verdadeiro).
> *C* não possui operadores de comparação encadeados, como `10 < x < 20`.

---

# Operadores lógicos

- *C* suporta os operadores lógicos `&&` (AND), `||` (OR) e `!` (NOT).
- Os operadores lógicos são usados para combinar expressões booleanas.

```c
int a = 10, b = 20;
if (a > 0 && b > 0) printf("a e b são positivos");
if (a > 0 || b > 0) printf("a ou b é positivo");
if (!(a > 0)) printf("a é negativo");
```

---

# Estruturas de seleção (if)


```c
int a = 10;
if (a > 0)
    printf("a é positivo");        
```

**Observações**:
- A condição é obrigatória e deve estar entre parênteses.
- O bloco de código é executado se a condição for verdadeira.
- Se o bloco de código tiver apenas uma linha, as chaves `{}` são opcionais.
- Indentação é opcional, mas recomendada para melhorar a legibilidade do código.
- Indentação não modifica o comportamento do programa.
- Não colocar `;` após o `if(a > 0)`.

---

Mais de um comando dentro de um bloco de código:

```c
int a = 10;
if (a > 0){
    printf("a é positivo");
    printf("a é maior que zero");
}
```

Indentação **não modifica** o comportamento do programa.

```c
int a = 10;
if (a > 0)
    printf("a é positivo");    
    printf("teste"); // Este comando não está dentro do 'if'
```

---

# Estruturas de seleção (if-else)

```c
int a = 10;
if (a > 0)
    printf("a é positivo");
else
    printf("a é negativo");
```


---

# Estruturas de seleção (if-else if-else)

*C* não possui a estrutura `elif` como em Python. Para encadear múltiplas condições, use `if-else if-else`.

```c
int a = 10;
if (a > 0)
    printf("a é positivo");
else if (a < 0)
    printf("a é negativo");
else
    printf("a é zero");
```

---

# Estruturas de repetição (while)

```c
int i = 0;
while (i < 10){
    printf("%d\n", i);
    i++;
}
```

---

# Estruturas de repetição (do-while)

Esta estrutura não está presente em Python. O bloco de código é executado pelo menos uma vez, mesmo que a condição seja falsa.

```c
int i = 0;
do{
    printf("%d\n", i);
    i++;
}while (i < 10);
```

---

# Estruturas de repetição (for)

Esta estrutura é bem diferente da estrutura `for` em Python. 

```c
for (int i = 0; i < 10; i++){
    printf("%d\n", i);
}
```

- **`int i = 0`**: declaração e inicialização da variável de controle
- **`i < 10`**: condição de parada, o bloco de código é executado enquanto a condição for verdadeira
- **`i++`**: incremento da variável de controle
- **Não** há range ou lista de valores como em Python.

---

# Entrada e saída de dados

- *C* possui funções específicas para entrada e saída de dados.
- A função `printf` é usada para imprimir dados na tela.
- A função `scanf` é usada para ler dados do teclado.

---

## Função `printf`

Em Python:

```python
print("Hello, World!")
```

Em C:

```c
printf("Hello, World!");
```

---
Imprimindo variáveis:

Em Python:

```python
x = 10
print(f"O valor de x é {x}")
```

Em C:

```c
int x = 10;
printf("O valor de x é %d", x);
```

- `%d`: substitui o valor de `x` na *string* usando o formato inteiro.
- As variáveis são passadas como argumentos após a *string*.
- Se o formato usado não corresponder ao tipo da variável, o resultado será imprevisível.

---

### Conversão de tipos

| Tipo | Formato |
|------|---------|
| `int` | `%d` |
| `float` | `%f` |
| `double` | `%lf` |
| `char` | `%c` |
| `string` | `%s` |

---

## Função `scanf`

Em Python:

```python
x = int(input("Digite um número: "))
```

Em C:

```c
int x;
printf("Digite um número: ");
scanf("%d", &x);
```

- `scanf` **não** imprime uma mensagem na tela. É necessário usar `printf` para isso.
- `&x` é o endereço de memória da variável `x`. 
- `%d` é o formato inteiro. 
- Se for passado um tipo diferente do esperado, o resultado será imprevisível.

---

# Exercícios
Escreva um programa em *C* que:

1. Imprime "Hello, World!" na tela.
2. Lê um número inteiro do teclado e imprime o dobro desse número.
3. Lê dois números inteiros do teclado e imprime a soma desses números.
4. Lê um número inteiro do teclado e imprime se ele é par ou ímpar.
5. Lê um inteiro e imprime de 1 até o número lido.

