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
        z= x2- ( (primera_derivada(x2, f))  / (    ( (primera_derivada(x2, f)) - (primera_derivada(x1,f)) ) /   (x2-x1)   )     )
        f_primaz = primera_derivada(z, f)
    
        if abs(x2 - x1) < e:  # Condición de terminación basada en la longitud del intervalo
            break
        elif f_primaz < 0:
            x1 = z
        elif f_primaz > 0:
            x2 = z

    return x1, x2

# Parámetros iniciales

e1=0.5
e2=0.1
e3=0.01
e4=0.0001
# Llamada al método de bisección
print('lata')
print(biseccionmethod(latax_a, latax_b, e1, f_lata))
print(biseccionmethod(latax_a, latax_b, e2, f_lata))
print(biseccionmethod(latax_a, latax_b, e3, f_lata))
print(biseccionmethod(latax_a, latax_b, e4, f_lata))

print('caja')
print(biseccionmethod(cajax_a, cajax_b, e1, f_caja))
print(biseccionmethod(cajax_a, cajax_b, e2, f_caja))
print(biseccionmethod(cajax_a, cajax_b, e3, f_caja))
print(biseccionmethod(cajax_a, cajax_b, e4, f_caja))

print('f3')
print(biseccionmethod(f3a, f3b, e1, f3))
print(biseccionmethod(f3a, f3b, e2, f3))
print(biseccionmethod(f3a, f3b, e3, f3))
print(biseccionmethod(f3a, f3b, e4, f3))

print('f4')
print(biseccionmethod(f4a, f4b, e1, f4))
print(biseccionmethod(f4a, f4b, e2, f4))
print(biseccionmethod(f4a, f4b, e3, f4))
print(biseccionmethod(f4a, f4b, e4, f4))

print('f5')
print(biseccionmethod(f5a, f5b, e1, f5))
print(biseccionmethod(f5a, f5b, e2, f5))
print(biseccionmethod(f5a, f5b, e3, f5))
print(biseccionmethod(f5a, f5b, e4, f5))

print('f6')
print(biseccionmethod(f6a, f6b, e1, f6))
print(biseccionmethod(f6a, f6b, e2, f6))
print(biseccionmethod(f6a, f6b, e3, f6))
print(biseccionmethod(f6a, f6b, e4, f6))