---
marp: true
title: "Strings em Python"
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

# *Strings* em Python

*Strings* são sequências de caracteres. Em Python, são objetos do tipo `str` e possuem a propriedade de serem **imutáveis**.


![bg right:40% 80%](empty.svg)

---

# Criando *strings*

Podemos criar *strings* de várias formas:
```python
# Usando aspas simples
s1 = 'Olá'
# Usando aspas duplas
s2 = "mundo!"
# Usando aspas triplas
s3 = '''Python'''
# String vazia
s4 = ''
s5 = str()
```

> Na programação, chamamos de **literal** uma sequência de caracteres que representa um valor.

---

# *Strings*  longas

Podemos criar *strings* longas usando aspas triplas:
```python
s = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
```
Ou usando a barra invertida:
```python
s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
```

- A barra invertida é chamada de **caractere de escape**. E neste caso, ela serve para indicar que a *string* continua na linha seguinte.
- Quando usamos aspas triplas, a **quebra de linha** é considerada parte da *string*.
- *Strings* longas são úteis para documentar o código.

---

# Caracteres de escape

Os caracteres de escape são usados para representar caracteres especiais em *strings*. Principais caracteres de escape:

| Caractere | Significado     |
| --------- | --------------- |
| `\'`      | Aspas simples   |
| `\"`      | Aspas duplas    |
| `\n`      | Quebra de linha |
| `\t`      | Tabulação       |
| `\\`      | Barra invertida |


---

```python
print("meu nome é \"Fulano\"")
>>> meu nome é "Fulano"
print('meu nome é\nFulano')
>>> meu nome é
>>> Fulano
print('meu nome é\tFulano')
>>> meu nome é    Fulano
print('meu nome é\\Fulano')
>>> meu nome é\Fulano
``` 

---

# *Strings* cruas (*raw*)

*Strings* cruas são *strings* que não interpretam caracteres de escape. São criadas colocando um `r` antes das aspas:

- Modo *careta*:
```python
s = 'C:\\Users\\fulano\\Documents'
```
- Modo *descolado*:
```python
s = r'C:\Users\fulano\Documents'
```

> *Strings* cruas são úteis para representar caminhos de arquivos, expressões regulares, trechos de código, etc.


---

# *Strings* formatadas

*Strings* formatadas permitem a inserção de valores de variáveis. São criadas usando `f` antes das aspas.

Seja:
```python
nome = 'Fulano'
idade = 30
```

- Modo *careta*:
```python
s = 'Meu nome é '+nome+' e tenho '+str(idade)+' anos.'
```
- Modo *descolado*:
```python
s = f'Meu nome é {nome} e tenho {idade} anos.'
```

---

## Formatação de inteiros
```python
n = 10
print(f'O valor de n é {n:4d}.') # pelo menos 4 dígitos
>>> O valor de n é   10.
print(f'O valor de n é {n:04d}.') # pelo menos 4 dígitos, preenchendo com zeros
>>> O valor de n é 0010.
print(f'O valor de n é {n:<4d}.') # alinhado à esquerda
>>> O valor de n é 10  .
print(f'O valor de n é {n:^4d}.') # centralizado
>>> O valor de n é  10  .
print(f'O valor de n é {n:+}.') # mostrar sinal sempre
>>> O valor de n é  +10.
```
---

## Formatação de *floats*
```python
pi = 3.14159265359
print(f'O valor de pi é {pi:.2f}.') # duas casas decimais
>>> O valor de pi é 3.14.
print(f'O valor de pi é {pi:5.2f}.') # pelo menos 5 dígitos, duas casas decimais
>>> O valor de pi é  3.14.
```

Os operadores `0`, `+`, `>`, `<` e `^` também funcionam com `float`.

---

## Formatação de *strings*
```python
s = 'Python'
print(f'Estou aprendendo {s}.')
>>> Estou aprendendo Python.
print(f'Estou aprendendo {s:10}.') # pelo menos 10 caracteres
>>> Estou aprendendo Python    .
print(f'Estou aprendendo {s:>10}.') # alinhado à direita
>>> Estou aprendendo     Python.
print(f'Estou aprendendo {s:^10}.') # centralizado
>>> Estou aprendendo   Python  .
```

---

# Indexação e fatiamento

Podemos acessar os caracteres de uma *string* usando **índices**, exatamente como fazemos com listas ou tuplas.

```python
s = 'Python'
print(s[0])
>>> P
print(s[:3])
>>> Pyt
print(s[2:5])
>>> tho
print(s[-1])
>>> n
```

---

# Tipo caracteres

Ao contrário de outras linguagens, em Python **não existe** um tipo `char`. Em Python, um caractere é uma *string* de tamanho 1.

```python
c = 'a'
print(type(c))
>>> <class 'str'>
```
<br>

> `type()` é uma função que retorna o tipo de um objeto.


---

# Lidando com a imutabilidade

- Por serem imutáveis, *strings* não podem ser modificadas. 
```python
s = 'Python'
s[0] = 'p'
>>> TypeError: 'str' object does not support item assignment
```
- Quando operamos com *strings*, estamos criando novas *strings*.
- Devemos ter cuidado com a criação de muitas *strings* em um loop, pois isso pode interferir na **performance** do programa.

<br>

> Se seu problema exige a manipulação de muitas *strings*, considere estudar uma biblioteca especializada, como [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO) por exemplo.
 
---

# Métodos de *strings*

*Strings* não são um tipo primitivo em Python, mas sim um objeto. Por isso, possuem **métodos** que podem ser usados para realizar diversas operações. Exemplos:

```python
s = 'Python'
print(s.upper()) # converte para maiúsculas
>>> PYTHON
print(s.lower()) # converte para minúsculas
>>> python
print(s.capitalize()) # converte a primeira letra para maiúscula
>>> Python
print(s.title()) # converte a primeira letra de cada palavra para maiúscula
>>> Python
print(s.replace('P', 'J')) # substitui caracteres
>>> Jython
print(s.find('t')) # retorna a primeira ocorrência de 't'
>>> 2
```

---

Pode causar estranheza, mas os métodos pode ser chamados diretamente de um literal de *string*:

```python
print('Python'.upper())
>>> PYTHON
```

Os métodos que retornam novas *strings* podem ser usados para chamar outros métodos:

```python
s = 'Python'
print(s.upper().replace('P', 'J'))
>>> JYTHON
```

Chamamos isso de **encadeamento de métodos**.

---












