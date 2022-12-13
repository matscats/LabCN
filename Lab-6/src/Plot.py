import numpy as np
import matplotlib.pyplot as plt
from Dados import *

def plot(theta : list[float], t : list[float]):
    for i in range(0, num - 1):
        nome = 'imagens/f' + str(i + 1) + '.jpg'
        img = plt.imread(nome)
        tm = img.shape
        fig , ax = plt.subplots(figsize=(15,15))
        ax.imshow(img, extent=[0, tm[1], 0, tm[0]])
        dy = np.cos(theta[v * i]) * d
        dx = np.sin(theta[v * i]) * d
        px = x0 + dx
        py = y0 - dy
        ax.plot(x0, y0, '.', linewidth=5, markersize=20,color='b')
        ax.plot(px, py, '.', linewidth=5, markersize=20,color='r')
        ax.plot([x0,px], [y0,py], '--', linewidth=2,markersize=20, color='r')
    plt.figure()
    plt.plot(t, theta)
    plt.show()