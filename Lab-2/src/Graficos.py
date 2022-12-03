from cProfile import label
from Dados import *
import matplotlib.pyplot as plt

def Grafico():
    x = np.linspace(ponto[0][0], ponto[3][0], 101)
    y_exp = np.tan(t) * x - g/(2 * v0**2 * np.cos(t)**2) * x**2 + y0
    y_calc = np.tan(t) * x - g/(2 * 3.27705**2 * np.cos(t)**2) * x**2 + y0
    plt.plot(x,y_exp, "r--", label='v0 experimental')
    plt.plot(x,y_calc,label='v0 métodos', color = 'blue')
    plt.legend()
    plt.ylim(0.48,1.8)
    for ponto_ in ponto:
        plt.scatter(ponto_[0], ponto_[1])
    plt.show()

Grafico()