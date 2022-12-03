from Dados import xo, yo, trata_pontos, reverte_pontos_x, reverte_pontos_y
from Metodos import mmq_pol, mmq_gen
import numpy as np
import matplotlib.pyplot as plt

# Pontos transformados
x, y, V, y_central = trata_pontos(xo, yo)
# Coeficientes MMQ Polinominal com pontos transformados
b0, b1, b2 = mmq_pol(x, y, 2)
# Coeficientes MMQ Genérico com pontos transformados
a0, a1, a2 = mmq_gen(x, y, 3)

img = plt.imread("Arquivos/imagem.jpeg")
fig, ax = plt.subplots()
ax.imshow(img)
xd = np.linspace(-1, 1, 100)
yd = b0 * 1 + b1 * xd + b2 * xd**2
yd2 = a0 * 1 + a1 * xd**2 + a2 * xd**4
reverte_pontos_x(xd, V)
reverte_pontos_y(yd, V, y_central)
reverte_pontos_y(yd2, V, y_central)
plt.plot(xd, yd2, color='black', label="Taylor")
plt.plot(xd, yd, color='y', label="Parábola", ls='dotted')
plt.scatter(xo, yo)
plt.show()
plt.legend()
