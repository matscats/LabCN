import numpy as np

Tx = 1600 # Tamanho da imagem em x
Ty = 1200 # Tamanho da imagem em y
Lc = 1.22 # Tamanho da corda em metros
Lm = 0.615 # Tamanho da madeira em metros
Tm = np.sqrt((10 - 1564)**2 + (1038 - 1006)**2) # Tamanho da madeira em pixels
Pontos = ((24,836),(134,788),(168,724),(358,382),(420,424),(566,710),(800,686),(1046,332),(1190,480),(1346,780),(1466,624),(1548,282))
X = [Pontos[i][0] for i in range(len(Pontos))]
Y = [Pontos[i][1] for i in range(len(Pontos))]
k = Lm / Tm # Proporção pixel-metro
Xm = [Pontos[i][0] * k for i in range(len(Pontos))]
Ym = [Pontos[i][1] * k for i in range(len(Pontos))]
