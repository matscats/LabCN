import numpy as np

# Método dos mínimos quadrados polinomial
def mmq_pol(x : float, y : float, k : int) -> float:
    n = len(x)
    V = np.zeros((n, k + 1))
    Y = np.array(y).reshape((n , 1))
    for i in range(0, n):
        for j in range(0, k + 1):
            V[i][j] = pow(x[i] , j)
    Vt = V.transpose()
    return np.linalg.solve(np.dot(Vt, V) , np.dot(Vt, y))

# Método dos mínimos quadrados genérico
def g(x : float, j : int) -> float:
    if j == 0:
        return 1
    if j == 1:
        return x**2
    if j == 2:
        return x**4

# Método dos mínimos quadrados genérico
def mmq_gen(x, y, k):
    n = len(x)
    V = np.zeros((n , k))
    Y = np.array(y).reshape((n , 1))
    for i in range(0, n):
        for j in range(0, k):
            V[i][j] = g(x[i], j)
    Vt = V.transpose()
    return np.linalg.solve(np.dot(Vt, V) , np.dot(Vt, y))
