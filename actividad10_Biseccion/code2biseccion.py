import numpy as np
import matplotlib.pyplot as plt
def primera_derivada(x, f):
    delta = 0.0001
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def segunda_derivada(x, f):
    delta = 0.0001
    return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta ** 2)

# ---------------------------------------------------------
def f_lata(x):
    return ((2 * np.pi) * (x**2) + 500/x)
latax_a=0.5
latax_b=8.5

def f_caja(x):
    return -1* (( (20- 2*x) * (10- 2*x) ) * x) #minizar  
cajax_a= 2
cajax_b=3

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

def biseccionmethod(f_a, f_b, e, f):
    a = np.random.uniform(f_a, f_b)
    b = np.random.uniform(f_a, f_b)
    x1 = a
    x2 = b
    
    while True:
        z = (x1 + x2) / 2
        f_primaz = primera_derivada(z, f)
    
        if abs(x2 - x1) < e:  
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1, x2




n_valores= [0.5, 0.1, 0.001, 0.0001]
funciones = [(f_lata, 'lata', latax_a, latax_b), (f_caja, 'caja', cajax_a, cajax_b),
             (f3, 'f3', f3a, f3b), (f4, 'f4', f4a, f4b),
             (f5, 'f5', f5a, f5b), (f6, 'f6', f6a, f6b)]


fig, axs = plt.subplots(3, 2, figsize=(12, 12))
fig.tight_layout(pad=5.0)

#graficar
#graficar
for i, (f, title, a, b) in enumerate(funciones):
    row = i // 2
    col = i % 2

    x_values = np.linspace(a, b, 100)
    y_values = f(x_values)

    axs[row, col].plot(x_values, y_values, label='Función')
    axs[row, col].set_title(title)

    for n in n_valores:
        a, b = biseccionmethod(a, b, n, f)  # Obteniendo nuevos límites a y b
        axs[row, col].scatter(a, f(a), label=f'n={n}')  # Utilizando a como el punto para graficar

    axs[row, col].legend()

plt.show()


plt.show()
