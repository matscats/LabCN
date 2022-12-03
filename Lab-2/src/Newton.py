from Dados import *

def deriv_f(v0 : float) -> float:
    return g * dx**2/(np.cos(t)**2 * v0**3)

def newton(v0 : float, erro : float) -> float:
    i = 0
    while True:
        v1 = v0 - f(v0)/deriv_f(v0)
        if  np.abs(v1-v0)/v1 < erro or i > max_int:
            break
        else:
            v0 = v1
        i += 1
    return v1, i

z = newton(v0, 0.000001)
print(z)