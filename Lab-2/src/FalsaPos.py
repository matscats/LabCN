from Dados import * 

def falsapos(a: float, b : float, erro : float) -> float:
    i = 0
    while True:
        if f(a)*f(b) < 0:
            x= a - f(a) * (b-a)/(f(b)-f(a))
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
            if np.abs(b-a)/b < erro or i > max_int:
                break
        i += 1
    return x, i

z = falsapos(1, 10, 0.000001)
print(z)
