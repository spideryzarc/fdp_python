# 1
# print('hellow world!')

# 2
# a = 3.14159 * 5 ** 2
# print('A área de um círculo de raio 5 é', a)

# 3
# x = int(input('Digite um número: '))
# antecessor = x - 1
# sucessor = x + 1
# print('O antecessor de', x, 'é', antecessor, 'e o sucessor é', sucessor)

#4
# celcius = float(input('Digite a temperatura em graus Celcius: '))
# fahrenheit = celcius * 9/5 + 32
# print('A temperatura em Fahrenheit é', fahrenheit)

#5
# peso = float(input('Digite o peso em kg: '))
# altura = float(input('Digite a altura em metros: '))
# imc = peso / altura ** 2
# print('O IMC é', imc)

#6
# x = float(input('Digite um número: '))
# quadrado = x ** 2
# cubo = x ** 3
# raiz = x ** 0.5
# raiz_cubica = x ** (1/3)
# print('O quadrado de', x, 'é', quadrado)
# print('O cubo de', x, 'é', cubo)
# print('A raiz quadrada de', x, 'é', raiz)
# print('A raiz cúbica de', x, 'é', raiz_cubica)

#7
# n = int(input('Digite um número inteiro: ')) #1234
# unidades = n % 10
# dezenas = (n % 100) // 10  
# centenas = (n % 1000) // 100
# milhares = n // 1000
# print('Unidades:', unidades)
# print('Dezenas:', dezenas)
# print('Centenas:', centenas)
# print('Milhares:', milhares)

#8
# n = int(input('Digite um número de segundos: '))
# segundos = n % 60
# n = n // 60
# minutos = n % 60
# horas = n // 60
# print('Horas:', horas)
# print('Minutos:', minutos)
# print('Segundos:', segundos)

9#
# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
# c = int(input('Digite o terceiro número: '))
# media = (a + b + c) / 3
# print('A média é', media)

# módulo 2
# 1
# n = int(input('Digite um número inteiro: '))
# if n % 2 == 0:
#     print('O número', n, 'é par')
# else:
#     print('O número', n, 'é ímpar')

# 2
# x = float(input('Digite um número: '))
# if x > 0:
#     print('O número', x, 'é positivo')
# elif x < 0:
#     print('O número', x, 'é negativo')  
# else:
#     print('O número', x, 'é zero')

#3
# a = float(input('Digite o primeiro número: '))
# b = float(input('Digite o segundo número: '))
# c = float(input('Digite o terceiro número: '))

# if a > b:
#     aux = a
#     a = b
#     b = aux
# if a > c:
#     aux = a
#     a = c
#     c = aux
# if b > c:  
#     aux = b
#     b = c
#     c = aux
# print('O menor número é', a)
# print('O maior número é', c)
## resolução alternativa
# if a >= b and a >= c:
#     print('O maior número é', a)
# elif b >= a and b >= c:
#     print('O maior número é', b)
# else:
#     print('O maior número é', c)
    
# if a <= b and a <= c:
#     print('O menor número é', a)
# elif b <= a and b <= c: 
#     print('O menor número é', b)
# else:
#     print('O menor número é', c)

#4
# a = float(input('Digite o valor para a: '))
# b = float(input('Digite o valor para b: '))
# c = float(input('Digite o valor para c: '))
# delta = b ** 2 - 4 * a * c
# if delta < 0:
#     print('A equação não possui raízes reais')
# elif delta == 0:
#     x = -b / (2 * a)
#     print('A equação possui uma raiz real:', x)
# else:
#     x1 = (-b + delta ** 0.5) / (2 * a)
#     x2 = (-b - delta ** 0.5) / (2 * a)
#     print('A equação possui duas raízes reais:', x1, 'e', x2)
    
#5
# lado1 = float(input('Digite o valor do primeiro lado: '))
# lado2 = float(input('Digite o valor do segundo lado: '))
# lado3 = float(input('Digite o valor do terceiro lado: '))

# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
#     print('Os lados formam um triângulo')
#     if lado1 == lado2 and lado1 == lado3:
#         print('O triângulo é equilátero')
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print('O triângulo é isósceles')
#     else:
#         print('O triângulo é escaleno')
# else:
#     print('Os lados não formam um triângulo')
  
#6
# a = float(input('Digite o primeiro número: '))
# b = float(input('Digite o segundo número: '))
# c = float(input('Digite o terceiro número: '))

# if b<=a<=c or c<=a<=b:
#     print('Mediana: ', a)
# elif a<=b<=c or c<=b<=a:
#     print('Mediana: ', b)
# else:
#     print('Mediana: ', c)

#7
ano = int(input('Digite um ano: '))
if ano % 4 != 0:
    print('O ano', ano, 'não é bissexto')
else:
    if ano % 100 == 0 and ano % 400 != 0:
        print('O ano', ano, 'não é bissexto')
    else:
        print('O ano', ano, 'é bissexto')