from Dados import *

def secante(v0 : float, erro : float) -> float:
    v1 = v0 + 1
    i = 0
    while True:
        v2 = v1 - f(v1) * (v1-v0)/(f(v1)-f(v0))
        _erro = np.abs(v2-v1)/v2
        if _erro < erro or i > max_int:
            break
        else:
            v0 = v1
            v1 = v2
        i += 1
    return v2, i

z = secante(v0, 0.000001)
print(z)