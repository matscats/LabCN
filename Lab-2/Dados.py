import numpy as np

ponto = ((0,0.743), (0.061,0.861), (0.455,1.187), (0.988,0.540)) #m
tempo = (3.043, 3.077, 3.377, 3.744) # s

g = 9.81 # m/s²
y_alvo = ponto[3][1]
y0 = ponto[0][1] # m
x0 = 1.158 #m
t = np.arctan((ponto[1][1] - ponto[0][1])/(ponto[1][0] - ponto[0][0])) # rad
v0x = (ponto[1][0]-ponto[0][0])/(tempo[1]-tempo[0]) #m/s
v0y = g * (tempo[2]-tempo[0]) #m/s
v0 = np.sqrt(v0x**2 + v0y**2) #m/s
dx = ponto[3][0] - ponto[0][0]
max_int = 1000

def f(v0 : float) -> float : 
    return np.tan(t) * dx - g/(2 * v0**2 * np.cos(t)**2) * dx**2 + y0 - y_alvo


