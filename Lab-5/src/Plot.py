import numpy as np
import matplotlib.pyplot as plt
from Dados import X, Y, Xm, Lc
from Interpolacao import lagrange, newton
from Integraçao import *

dom = np.linspace(X[0], X[len(X) - 1], 101)
y = np.zeros(101)

# for i in range(101):
#     y[i] = lagrange(X, Y, dom[i])

# img = plt.imread('Imagens/Corda.jpeg')
# fig, ax = plt.subplots()
# ax.imshow(img)
# plt.plot(dom, y, color='black', linewidth=2)
# plt.show()

S = trapezio(Xm[0], Xm[len(X) - 1], 1000)
print(f'Resultado pela regra do trapézio composta: {S}')

S = simpson_1(Xm[0], Xm[len(X) - 1], 1000)
print(f'Resultado pela primeira regra de simpson: {S}')

S = simpson_1(Xm[0], Xm[len(X) - 1], 1000)
print(f'Resultado pela segunda regra de simpson: {S}')

print(f'Tamanho original: {Lc}')