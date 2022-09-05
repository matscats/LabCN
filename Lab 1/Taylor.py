import numpy as np
import matplotlib.pyplot as plt
from math import factorial

r = 1 #px

# Função X(t)
def X(t: float) -> float: return r*(t-np.sin(t))
# Função Y(t)
def Y(t: float) -> float: return r*(1-np.cos(t))

def TaylorX(t0: float, n: int, t: float) -> float:
    a = X(t0) + r*(1-np.cos(t))*(t-t0) # Termo inicial    
    for i in range(2,n+1):
        if i%4==0:
            a -= r*np.sin(t0)*(t-t0)**i/factorial(i)
        if i%4==1:
            a -= r*np.cos(t0)*(t-t0)**i/factorial(i)
        if i%4==2:
            a += r*np.sin(t0)*(t-t0)**i/factorial(i)
        if i%4==3:
            a += r*np.cos(t0)*(t-t0)**i/factorial(i)       
    return a

def TaylorY(t0: float, n: int, t: float) -> float:
    a = Y(t0) # Termo inicial
    for i in range(1,n+1):
        if i%4==0:
            a += -r*np.cos(t0)*(t-t0)**i/factorial(i)
        if i%4==1:
            a += r*np.sin(t0)*(t-t0)**i/factorial(i)
        if i%4==2:
            a += r*np.cos(t0)*(t-t0)**i/factorial(i)
        if i%4==3:
            a += -r*np.sin(t0)*(t-t0)**i/factorial(i)
    return a

def Plot(t0: float, n: int, t: float):
    t_ = np.linspace(t0, t, n+1) # Domínio
    x = X(t_)
    y = Y(t_)
    plt.scatter(t_, x, label='x(t)')
    plt.scatter(t_, y, label='y(t)')
    plt.legend()
    plt.show()
