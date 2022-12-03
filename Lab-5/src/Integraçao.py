import numpy as np
from Interpolacao import lagrange
from Dados import *

def deriv_f(x1, x2, h): return (lagrange(Xm, Ym, x1) - lagrange(Xm, Ym, x2))/h 

def f(x) : return np.sqrt(1 + deriv_f(x + 0.0001, x, 0.0001)**2)

def trapezio(a : float, b : float, n : int) -> float:
    h = (b-a)/n
    x = np.arange(a, b + h, h)
    s = 0
    for i in range(0, len(x) - 1):
        s += f(x[i]) + f(x[i+1])
    return h/2 * s

def simpson_1(a : float, b : float, n : int) -> float:
    if n % 2 != 0:
        return 'A regra de simpson exige um número par de subintervalos'
    else:
        h = (b-a)/n
        x = np.arange(a, b + h, h)
        s = 0
        for i in range(0, len(x) - 2, 2):
            s += f(x[i]) + 4 * f(x[i+1]) + f(x[i+2])
        return h/3 * s

def simpson_2(a : float, b : float, n : int) -> float:
    if n % 2 != 0:
        return 'A regra de simpson exige um número par de subintervalos'
    else:
        h = (b-a)/n
        x = np.arange(a, b + h, h)
        s = 0
        for i in range(0, len(x) - 3, 3):
            s += f(x[i]) + 3 * f(x[i+1]) + 3 * f(x[i+2]) + f(x[i+3])
        return 3*h/8 * s
