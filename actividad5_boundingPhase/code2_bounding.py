import numpy as np
import matplotlib.pyplot as plt

def f_lata(x):
    return 2 * np.pi * (x**2)
latax_a=0.5
latax_b=8.5

def f_caja(x):
    return (20- 2*x) * (10- 2*x) * x
cajax_a= 2
cajax_b=3.1

#----------------------------------------------------------
def f3(x):
    return (x**2) + 54/x
f3a=0.1
f3b=10

def f4(x):
    return (x**3) + 2 * x - 3
f4a=0.1
f4b=5

def f5(x):
    return (x**4) + (x**2) - 33
f5a=-2.5
f5b=2.5

def f6(x):
    return 3 * (x**4) - 8 * (x**3) - 6 * (x**2) + 12 * x
f6a=-1.5
f6b=3


def bounding_phase(delta, f):
    x_0 = 0.6

    if f(x_0 - abs(delta)) > f(x_0) > f(x_0 + abs(delta)):
        delta = abs(delta)
    else:
        if delta < 0:
            delta = delta
        else:
            delta = -1 * delta

    k = 0
    condicion = True

    while condicion:
        x_anterior = x_0 
        x_actual = x_0 + (2**k * delta)  
        k += 1

        if f(x_actual) < f(x_0):
            x_0 = x_actual
        else:
            condicion = False

    return x_anterior, x_actual  

#NOTA: la funcion 4 no es posible graficar ya que aparece error de Overflow

#delta
delta_valores = [0.5, 0.1, 0.001, 0.0001]

funciones = [(f_lata, 'lata', latax_a, latax_b), (f_caja, 'caja', cajax_a, cajax_b),
             (f3, 'f3', f3a, f3b), #(f4, 'f4', f4a, f4b),
             (f5, 'f5', f5a, f5b), (f6, 'f6', f6a, f6b)]


fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.tight_layout(pad=5.0)


for i, (f, title, a, b) in enumerate(funciones):
    row = i // 2
    col = i % 2

    x_values = np.linspace(a, b, 100)
    y_values = f(x_values)

    axs[row, col].plot(x_values, y_values, label='Función')
    axs[row, col].set_title(title)

    for d in delta_valores:
        a, b = bounding_phase( d, f)  
        axs[row, col].scatter(a, f(a), label=f'n={d}') 

    axs[row, col].legend()


plt.show()
