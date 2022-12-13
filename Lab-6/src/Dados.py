import numpy as np

l = 1 # Comprimento da corda em metros
fps = 30.011340
h = 1 / fps
(x0, y0) = (166, 360 - 13)
(xr, yr) = (61, 360 - 284)
(x1, y1) = (65, 360 - 286)
n1 = np.sqrt((xr - x0)**2 + (yr - y0)**2)
n2 = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
# theta_0 = np.arccos(((xr - x0) * (x1 - x0) + (yr - y0) * (y1 - y0))/(n1 * n2)) # Ângulo inicial
theta_0 = -0.35
d = np.sqrt((x1-x0)**2 + (y1-y0)**2) # Tamanho da corda em pixels
g = 9.81 # Aceleração da gravidade em m/s²
num = 16
v = 50

def df1(omega : float, theta : float, t : float) -> float : return omega
def df2(omega : float, theta : float, t : float) -> float : return - g/l * np.sin(theta)