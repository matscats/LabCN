import numpy as np
from Dados2 import *

def Jacobi(C, b, erro):
    # Cria as matrizes B e g
    B = np.array(C)
    g = np.array(b)
    x = np.zeros((n, 1))
    for i in range(0, n):
        g[i] = g[i]/C[i][i]
        for j in range(0, n):
            B[i][j] = -C[i][j]/C[i][i]
            B[i][i] = 0
    # Iterações
    if ConvergeLinha(B) or ConvergeColuna(B):
        cont = 0
        while True:
            y = x.copy()
            x = np.dot(B, x) + g
            cont += 1
            if ErroRelativo(x,y) < erro:
                break          
        return x, cont, ErroRelativo(x,y)
    else:
        return 'Teste inconclusivo' 

x = Jacobi(C, b, 0.001)

print(f'Mensagem decodificada: {[chr(int(np.round(v))) for v in x[0]]}')
print(f'Número de iterações: {x[1]}')
print(f'Erro relativo: {x[2]}')