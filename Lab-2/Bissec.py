from Dados import * 

def bissec(a: float, b : float, erro : float) -> float:
    i = 0
    while True:
        if f(a)*f(b) < 0:
            x = (a+b)/2
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
            if np.abs(b-a)/b < erro or i > max_int:
                break
        i += 1
    return x, i

z = bissec(1, 10, 0.000001)
print(z)
