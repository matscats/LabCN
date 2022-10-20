import numpy as np
# Tamanho da matriz de criptografia
n = 12
# Matriz de criptografia
C = [[10.0,0.0,0.0,1.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
     [0.0,10.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0],
     [1.0,0.0,10.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
     [1.0,1.0,0.0,10.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0],
     [1.0,1.0,1.0,0.0,10.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0],
     [1.0,1.0,1.0,1.0,0.0,10.0,0.0,1.0,1.0,1.0,1.0,1.0],
     [1.0,1.0,1.0,1.0,1.0,0.0,10.0,0.0,1.0,1.0,1.0,1.0],
     [1.0,1.0,1.0,1.0,1.0,1.0,0.0,10.0,0.0,1.0,1.0,1.0],
     [1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,10.0,0.0,1.0,1.0],
     [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,10.0,0.0,1.0],
     [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,10.0,1.0],
     [0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,10.0]]
# Mensagem criptografada
b = [[1938.0],[1936.0],[2039.0],[1839.0],[2017.0],[2020.0],[1318.0],[2020.0],[1934.0],[2001.0],[2072.0],[2004.0]]

# Critérios de convergência
def ConvergeLinha(B : float) -> bool:
    for i in range(n):
        m = 0
        for j in range(0,n):
            m += np.abs(B[i][j])
            if m > 1:
                return False
            else:
                return True

def ConvergeColuna(B : float) -> bool:
    for j in range(0,n):
        m = 0
        for i in range(0,n):
            m += np.abs(B[i][j])
            if m > 1:
                return False
            else:
                return True

def Sassenfeld(M : float) -> bool:
    B = np.array(C)
    for i in range(0, n):
        for j in range(0, n):
            B[i][j] = -C[i][j]/C[i][i]
            B[i][i] = 0
    b = np.zeros(n)
    for i in range(0,n):
        for j in range(0,i-1):
            b[i] += b[j] * np.abs(B[i,j])
        for j in range(i,n):
            b[i] += np.abs(B[i,j])
        if b[i] > 1:
            return False
        else:
            return True

def ErroRelativo(X : float, Y : float) -> float:
    return np.abs(np.linalg.norm(X, np.inf) - np.linalg.norm(Y, np.inf))/np.linalg.norm(X, np.inf)