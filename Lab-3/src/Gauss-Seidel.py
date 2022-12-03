import numpy as np
from Dados2 import *

def GaussSeidel(C, b, erro):
    if Sassenfeld(C):
        cont = 0
        x = np.zeros(n)
        while True:
            y = x.copy()
            for i in range(0,n):
                m = b[i]
                for j in range(0,n):
                    if i != j:
                        m -= C[i][j] * x[j]
                m /= C[i][i]
                x[i] = m
            cont += 1
            if ErroRelativo(x,y) < erro:
                break
        return x, cont, ErroRelativo(x,y)
    else:
        return 'Matriz não converge pelo critério de Sassenfeld'

x = GaussSeidel(C, b, 0.001)

print(f'Mensagem decodificada: {[chr(int(np.round(v))) for v in x[0]]}')
print(f'Número de iterações: {x[1]}')
print(f'Erro relativo: {x[2]}')
