# Dados coletados
nx = 1600
ny = 720
xo = [311, 392, 471, 592, 705, 787, 857, 940, 1012, 1088]
yo = [352, 412, 461, 507, 521, 513, 496, 462, 420, 362]
x_central = 705

def trata_pontos(xo, yo):
    x = xo.copy()
    y = yo.copy()
    n = len(x)
    # Inverte
    for i in range(n):
        y[i] = ny - y[i]
    # Centraliza
    for i in range(n):
        x[i] = x[i] - x_central
    # Normaliza
    V = abs(min(x))
    for i in range(n):
        x[i] /= V
        y[i] /= V
    y_central = min(y)
    for i in range(n):
        y[i] = y[i] - y_central + 1
    return x, y, V, y_central

def reverte_pontos_x(x, V):
    n = len(x)
    for i in range(n):
        x[i] = x[i] * V + x_central

def reverte_pontos_y(y, V, y_central):
    n = len(y)
    for i in range(n):
        y[i] = (y[i] - 1 + y_central) * V
        y[i] = -y[i] + ny
