import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import csv

def pegarDados(caminho):
    '''Função para pegar os dados tabelados do experimento, caminho é o caminho
    (path) do .csv'''
    x, y = [], []
    with open(caminho,'rt', newline="") as tabela:
        leitor = csv.reader(tabela,)
        for linha in leitor:
            if linha[0] == 'Frame': continue
            x.append(int(linha[1]))
            y.append(int(linha[3]))
    r = 40.90282037
    return {'pos':np.array([x, y]), 'r':r}

r = 1 #px

#Xo e Yo servem caso se faça um imshow de um frame do vídeo no gráfico.
#Xo e Yo exp. são pegarDados(caminho)['x'][0] e pegarDados(caminho)['y'][6].
# Função X(t)
def X(t: float, Xo:int =0) -> float: return r*(t-np.sin(t)) + Xo
# Função Y(t)
def Y(t: float, Yo:int =0) -> float: return r*(1-np.cos(t)) + Yo

def altTaylorX(t0: float, n: int, t: float, opt:bool = False) -> float:
    if n <= 0: raise Exception("Número inválido de termos")
    if opt: 
        ciclo1 = altTaylorX(t0, n, (t - (np.floor((t)/(2*np.pi))*2*np.pi)))
        return ciclo1 + r*(np.floor((t)/(2*np.pi))*2*np.pi)
    a = 0  
    for j in range(2,n):
        i = n-j+1
        if i%4==0:
            a -= r*np.sin(t0)*(t-t0)**i/factorial(i)
        if i%4==1:
            a -= r*np.cos(t0)*(t-t0)**i/factorial(i)
        if i%4==2:
            a += r*np.sin(t0)*(t-t0)**i/factorial(i)
        if i%4==3:
            a += r*np.cos(t0)*(t-t0)**i/factorial(i)
    if n > 1: a += r*(1-np.cos(t0))*(t-t0)
    a += X(t0) #Termo inicial

    return a

def altTaylorY(t0: float, n: int, t: float, opt:bool = False) -> float:
    if n <= 0: raise Exception("Número inválido de termos")
    if opt: return altTaylorY(t0, n, (t - (np.floor((t)/(2*np.pi))*2*np.pi)) )
    a = 0
    for j in range(1,n):
        i = n-j
        if i%4==0:
            a += -r*np.cos(t0)*((t-t0)**i)/factorial(i)
        if i%4==1:
            a += r*np.sin(t0)*((t-t0)**i)/factorial(i)
        if i%4==2:
            a += r*np.cos(t0)*((t-t0)**i)/factorial(i)
        if i%4==3:
            a += -r*np.sin(t0)*((t-t0)**i)/factorial(i)
    a += Y(t0) #Termo inicial
    return a

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
    
def altPlot(t0: float, n: int, t: float, ideal:bool =True, 
            exp:np.ndarray =np.ndarray([]), **taylor):
    '''os kwargs de taylor são o booleano opt e o inteiro termos que servem
    para representar o n e o opt das func altTaylor eu troquei altTaylorX por
    altTaylorY no opt do x e fiquei 30 min tentando entender como a distância
    ficava zoada'''
    t_ = np.linspace(t0, t, n+1) # Domínio
    Xo, Yo = 0, 0

    if exp.ndim==2:
        plt.scatter(exp[0], exp[1], label='Dados experimentais')
        Xo = exp[0][0]
        Yo = exp[1][6]

    if ideal: plt.plot(X(t_,Xo),Y(t_,Yo), label='Cicloide ideal')

    if taylor:
        plt.plot(altTaylorX(0, taylor['termos'], t_, taylor['opt']) + Xo,
                 altTaylorY(0, taylor['termos'], t_, taylor['opt']) + Yo,
                 label='Aprox. por Taylor')
    plt.legend()
    plt.axis('equal')
    plt.show()
    
