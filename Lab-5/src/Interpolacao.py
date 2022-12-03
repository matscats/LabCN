import numpy as np

def lagrange(X : list[int], Y : list[int], p : float) -> float:
    n = len(X)
    s = 0
    for i in range(0, n):
        L = 1
        for j in range(0, n):
            if i != j:
                L *= (p - X[j])/(X[i] - X[j])
        s += L * Y[i]
    return s

def dif_div(X : list[int], Y : list[int]) -> list[float]:
    n = len(X)
    T = np.zeros((n,n))
    for i in range(0, n):
        T[i][0] = Y[i]
    for j in range(0, n-1):
        for i in range(0, (n-1) - j):
            T[i][j+1] = (T[i+1][j] - T[i][j])/(X[i+j+1] - X[i])
    return T

def newton(X : list[int], Y : list[int], p : float) -> float:
    n = len(X)
    s = Y[0]
    Tab = dif_div(X, Y)
    for i in range(1, n):
        M = 1
        for j in range(0, i):
            M *= p - X[j]
        s += M * Tab[0][i]
    return s
