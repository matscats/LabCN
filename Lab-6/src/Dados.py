import numpy as np

g = 9.81 # Aceleração da gravidade em m/s²
l = 1 # Comprimento da corda em metros

def df1(omega : float, theta : float, t : float) -> float : return omega
def df2(omega : float, theta : float, t : float) -> float : return - g/l * np.sin(theta)