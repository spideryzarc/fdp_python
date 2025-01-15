import numpy as np
with open('zenios.mtx', 'r') as f:
    line = f.readline()
    print(line, end='')
    line = f.readline()
    lista = line.split()
    n = int(lista[0])
    m = int(lista[1])
    print(n, m)
    matriz = np.zeros((n, m))
    for line in f:
        lista = line.split()
        i = int(lista[0])
        j = int(lista[1])
        valor = float(lista[2])
        matriz[i-1, j-1] = valor
        
print(matriz)
    