import numpy as np
import matplotlib.pyplot as plt

def delta(a, b, n):
    delta = (b - a) / n
    return delta

def f_lata(x):
    return  ((2 * np.pi) * (x**2) + 500/x)

def f_caja(x):
    return -1 * (((20 - 2*x) * (10 - 2*x)) * x)  # minimizar

def f3(x):
    return (x**2) + 54/x

def f4(x):
    return (x**3) + 2 * x - 3

def f5(x):
    return (x**4) + (x**2) - 33

def f6(x):
    return 3 * (x**4) - 8 * (x**3) - 6 * (x**2) + 12 * x

# Función para realizar la búsqueda exhaustiva y devolver los valores encontrados
def exhausive_search(a, b, n, f):
    precision = (2 * (b - a)) / n
    delt = delta(a, b, precision)

    x1 = a
    x2 = x1 + delt
    x3 = x2 + delt

    fx1 = f(x1)
    fx2 = f(x2)
    fx3 = f(x3)

    while x3 <= b:
        if (fx1 > fx2) and (fx2 < fx3):
            return x1, x3
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + delt
            fx1 = f(x1)
            fx2 = f(x2)
            fx3 = f(x3)
    return x1, x3

#parametros
n_values = [0.5, 0.1, 0.001, 0.0001]
functions = [(f_lata, 'lata', 0.5, 8.5), (f_caja, 'caja', 2, 3),
             (f3, 'f3', 0.1, 10), (f4, 'f4', 0.1, 5),
             (f5, 'f5', -2.5, 2.5), (f6, 'f6', -1.5, 3)]


fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.tight_layout(pad=5.0)


for i, (f, title, a, b) in enumerate(functions):
    row = i // 2
    col = i % 2

    x_values = np.linspace(a, b, 100)
    y_values = f(x_values)

    axs[row, col].plot(x_values, y_values, label='Función')
    axs[row, col].set_title(title)

    for n in n_values:
        a, b = exhausive_search(a, b, n, f)  
        axs[row, col].scatter(a, f(a), label=f'n={n}') 

    axs[row, col].legend()
plt.show()
