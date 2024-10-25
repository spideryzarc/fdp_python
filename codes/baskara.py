#leitura dos valores
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

#calcular o delta
delta = b**2-4*a*c
#calcular raizes
if delta < 0:
    print('não há raizes reais')
elif delta==0:
    x = -b/(2*a)
    print('única raiz:', x)
else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print('raizes:',x1,x2)
    
    


