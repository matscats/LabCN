import numpy as np
import matplotlib.pyplot as plt
from Dados1 import *

def LU(M):
    L = np.identity(n)
    U = np.array(M)
    for k in range(0, n-1):
        for i in range(k+1, n):
            m = U[i][k]/U[k][k]
            L[i][k] = m
            for j in range(k+1, n):
                U[i][j] = U[i][j] - m * U[k][j]
            U[i][k] = 0
    return L,U

x = LU(imgruido)

#plt.imshow(np.uint8(x[0]), cmap="gray")
#plt.imshow(np.uint8(x[1]), cmap="gray")
plt.imshow(np.uint8(np.dot(x[0],x[1])), cmap="gray")
plt.show()