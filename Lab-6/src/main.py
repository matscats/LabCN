from Dados import h, theta_0, num, v
from Metodos import euler, rk2
from Plot import plot
import matplotlib.pyplot as plt

theta, t = rk2(0, (num-1) * h, h/v, 1.8, theta_0)
plot(theta, t)