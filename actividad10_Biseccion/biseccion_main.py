import numpy as np 
import matplotlib.pyplot as plt
#Este es el central difference method 
def primeraderivadanumerica(x_actual,f):
    delta=0.0001
    numerador= f(x_actual + delta) - f (x_actual - delta) 
    return numerador / (2 * delta)

def segundaderivadanumerica(x_actual,f):
    delta=0.0001
    numerado= f(x_actual + delta) - (2 * f (x_actual + f(x_actual- delta))) 
    return numerado / (delta**2)

def biseccionmethod(a_orginal,b_original,e,f):
    a = np.random.uniform(a_orginal, b_original)
    b = np.random.uniform(a_orginal, b_original)
    while(primeraderivadanumerica(a,f) > 0):
        a = np.random.uniform(a_orginal, b_original)
        print(primeraderivadanumerica(a,f))
    
    while (primeraderivadanumerica(b,f) < 0): 
        b = np.random.uniform(a_orginal, b_original)
    x1=a
    x2=b
    z = ((x2+x1)/2)
    #print(primeraderivadanumerica(x1,f))
    while(primeraderivadanumerica(z,f) > e):
        #print(z)
        if primeraderivadanumerica(z,f) < 0: 
            x1=z
            z=0
            z = int((x2+x1)/2)
        elif primeraderivadanumerica(z,f) > 0: 
            x2=z
            z=0
            z = ((x2+x1)/2)
    
    print("Listo!")
    x1 , x2

def funcion1(x):
    return (x**2) + (54/x)

def funcion2(x):
    return (x**3) + (2*x) - 3

def funcion3(x):
    return (x**4) + (x**2) - 33
def funcion4(x):
    return (3 * (x**4)) - (8 * (x**3)) - (6 * (x**2)) + 12 * x

def ecuacionsuperficie(radio):
    pi=3.1416
    if radio==0:
        radio==1
    return  2*pi * (radio**2)+500/radio
def formula_volumen_4demarzo(l):
    cajita=((20-(2*l))*(10-(2*l)))*l
    return  cajita *-1

#Funcion 1 
nv=0.5
nv2=0.1
nv3=0.01
nv4=0.0001
a1=0.1
b1=10
array_funcion10=np.linspace(a1,b1,100)
y_funcion10=[]
for x in array_funcion10: 
    y_funcion10.append(funcion1(x))

X1_F1,X3_F1=biseccionmethod(a1,b1,nv,funcion1)
X12_F1,X32_F1=biseccionmethod(a1,b1,nv2,funcion1)
X13_F1,X33_F1=biseccionmethod(a1,b1,nv3,funcion1)
X14_F12,X34_F1=biseccionmethod(a1,b1,nv4,funcion1)
print("Funcion 1 lista")

#Funcion 2 
a2=-5
b2=5
array_funcion2=np.linspace(a2,b2,100)
y_funcion2=[]
for x_2 in array_funcion2:
    y_funcion2.append(funcion2(x_2))

'''
X1_F2,X3_F2=biseccionmethod(a2,b2,nv,funcion2)
X12_F2,X32_F2=biseccionmethod(a2,b2,nv2,funcion2)
X13_F2,X33_F2=biseccionmethod(a2,b2,nv3,funcion2)
X14_F2,X34_F2=biseccionmethod(a2,b2,nv4,funcion2)
print("Funcion 2")
'''

#Funcion 3 
a3=-2.5
b3=2.5
array_funcion3=np.linspace(a3,b3,100)
y_3=[]
for x_3 in array_funcion3:
    y_3.append(funcion3(x_3))
X1_F3,X3_F3=biseccionmethod(a3,b3,nv,funcion3)
X12_F3,X32_F3=biseccionmethod(a3,b3,nv2,funcion3)
X13_F3,X33_F3=biseccionmethod(a3,b3,nv3,funcion3)
X14_F3,X34_F3=biseccionmethod(a3,b3,nv4,funcion3)
print("Funcion3")
#Funcion 4 
''' 
a4=-1.5
b4=3
array_funcion4=np.linspace(a4,b4,100)
y_4=[]
for x4 in array_funcion4:
    y_4.append(funcion4(x4))
X1_F4,X3_F4=biseccionmethod(a4,b4,nv,funcion4)
X12_F4,X32_F4=biseccionmethod(a4,b4,nv2,funcion4)
X13_F4,X33_F4=biseccionmethod(a4,b4,nv3,funcion4)
X14_F4,X34_F4=biseccionmethod(a4,b4,nv4,funcion4)
print("Funcion 4")
'''
#Funcion lata 
alata=0.5
blata=8
array_funcionlata=np.linspace(alata,blata,100)
y_lata=[]
for la in array_funcionlata:
    y_lata.append(ecuacionsuperficie(la))
X1_lata,X3_lata=biseccionmethod(alata,blata,nv,ecuacionsuperficie)
X12_lata,X32_lata=biseccionmethod(alata,blata,nv2,ecuacionsuperficie)
X13_lata,X33_lata=biseccionmethod(alata,blata,nv3,ecuacionsuperficie)
X14_lata,X34_lata=biseccionmethod(alata,blata,nv4,ecuacionsuperficie)
print("Funcion 1 lata")
#Funcion caja
acaja=2
bcaja=3
array_funcioncaja=np.linspace(acaja,bcaja,100)
y_caja=[]
for caja in array_funcioncaja:
    y_caja.append(formula_volumen_4demarzo(caja))
X1_caja,X3_caja=biseccionmethod(acaja,bcaja,nv,formula_volumen_4demarzo)
X12_caja,X32_caja=biseccionmethod(acaja,bcaja,nv2,formula_volumen_4demarzo)
X13_caja,X33_caja=biseccionmethod(acaja,bcaja,nv3,formula_volumen_4demarzo)
X14_caja,X34_caja=biseccionmethod(acaja,bcaja,nv4,formula_volumen_4demarzo)
print("Funcion 1 caja")
#Graficas 
fig, axs = plt.subplots(2, 3)
axs[0,0].plot(array_funcion10,y_funcion10)
axs[0, 0].scatter(X1_F1,funcion1(X1_F1), label='Limite = 0.5')
axs[0, 0].scatter(X3_F1,funcion1(X3_F1), label='Limite = 0.5')
axs[0, 0].scatter(X12_F1,funcion1(X12_F1), label = 'limite = 0.1 ')
axs[0, 0].scatter(X32_F1,funcion1(X32_F1), label = 'limite = 0.1 ')
axs[0, 0].scatter(X13_F1,funcion1(X13_F1), label='limite = 0.01')
axs[0, 0].scatter(X33_F1, funcion1(X33_F1),label='limite = 0.01')
axs[0, 0].scatter(X14_F12,funcion1(X14_F12),label = 'limite = 0.0001')
axs[0, 0].scatter(X34_F1,funcion1(X34_F1),label = 'limite = 0.0001')
axs[0,0].legend()
axs[0, 0].set_title('Funcion1')
axs[0,1].plot(array_funcion2,y_funcion2)
'''
axs[0, 1].scatter(X1_F2,funcion2(X1_F2), label='Limite = 0.5')
axs[0, 1].scatter(X3_F2,funcion2(X3_F2), label='Limite = 0.5')
axs[0, 1].scatter(X12_F2,funcion2(X12_F2), label = 'limite = 0.1 ')
axs[0, 1].scatter(X32_F2,funcion2(X32_F2), label = 'limite = 0.1 ')
axs[0, 1].scatter(X13_F2,funcion2(X13_F2), label='limite = 0.01')
axs[0, 1].scatter(X33_F2, funcion2(X33_F2),label='limite = 0.01')
axs[0, 1].scatter(X14_F2,funcion2(X14_F2),label = 'limite = 0.0001')
axs[0, 1].scatter(X34_F2,funcion2(X34_F2),label = 'limite = 0.0001')
axs[0,1].legend()
axs[0, 1].set_title('Funcion2')
'''
axs[1,0].plot(array_funcion3,y_3)
axs[1, 0].scatter(X1_F3,funcion3(X1_F3), label='Limite = 0.5')
axs[1, 0].scatter(X3_F3,funcion3(X3_F3), label='Limite = 0.5')
axs[1, 0].scatter(X12_F3,funcion3(X12_F3), label = 'limite = 0.1 ')
axs[1, 0].scatter(X32_F3,funcion3(X32_F3), label = 'limite = 0.1 ')
axs[1, 0].scatter(X13_F3,funcion3(X13_F3), label='limite = 0.01')
axs[1, 0].scatter(X33_F3, funcion3(X33_F3),label='limite = 0.01')
axs[1, 0].scatter(X14_F3,funcion3(X14_F3),label = 'limite = 0.0001')
axs[1, 0].scatter(X34_F3,funcion3(X34_F3),label = 'limite = 0.0001')
axs[1,0].legend()
axs[1, 0].set_title('Funcion3')
'''
axs[1,1].plot(array_funcion4,y_4)
axs[1, 1].scatter(X1_F4,funcion4(X1_F4), label='Limite = 0.5')
axs[1, 1].scatter(X3_F4,funcion4(X3_F4), label='Limite = 0.5')
axs[1, 1].scatter(X12_F4,funcion4(X12_F4), label = 'limite = 0.1 ')
axs[1, 1].scatter(X32_F4,funcion4(X32_F4), label = 'limite = 0.1 ')
axs[1, 1].scatter(X13_F4,funcion4(X13_F4), label='limite = 0.01')
axs[1, 1].scatter(X33_F4, funcion4(X33_F4),label='limite = 0.01')
axs[1, 1].scatter(X14_F4,funcion4(X14_F4),label = 'limite = 0.0001')
axs[1, 1].scatter(X34_F4,funcion4(X34_F4),label = 'limite = 0.0001')
axs[1,1].legend()
axs[1, 1].set_title('Funcion4')
'''
axs[0,2].plot(array_funcionlata,y_lata)
axs[0, 2].scatter(X1_lata,ecuacionsuperficie(X1_lata), label='Limite = 0.5')
axs[0, 2].scatter(X3_lata,ecuacionsuperficie(X3_lata), label='Limite = 0.5')
axs[0, 2].scatter(X12_lata,ecuacionsuperficie(X12_lata), label = 'limite = 0.1 ')
axs[0, 2].scatter(X32_lata,ecuacionsuperficie(X32_lata), label = 'limite = 0.1 ')
axs[0, 2].scatter(X13_lata,ecuacionsuperficie(X13_lata), label='limite = 0.01')
axs[0, 2].scatter(X33_lata, ecuacionsuperficie(X33_lata),label='limite = 0.01')
axs[0, 2].scatter(X14_lata,ecuacionsuperficie(X14_lata),label = 'limite = 0.0001')
axs[0, 2].scatter(X34_lata,ecuacionsuperficie(X34_lata),label = 'limite = 0.0001')
axs[0,2].legend()
axs[0, 2].set_title('Funcion lata')
axs[1,2].plot(array_funcioncaja,y_caja)
axs[1, 2].scatter(X1_caja ,formula_volumen_4demarzo(X1_caja), label='Limite = 0.5')
axs[1, 2].scatter(X3_caja,formula_volumen_4demarzo(X3_caja), label='Limite = 0.5')
axs[1, 2].scatter(X12_caja,formula_volumen_4demarzo(X12_caja), label = 'limite = 0.1 ')
axs[1, 2].scatter(X32_caja,formula_volumen_4demarzo(X32_caja), label = 'limite = 0.1 ')
axs[1, 2].scatter(X13_caja,formula_volumen_4demarzo(X13_caja), label='limite = 0.01')
axs[1, 2].scatter(X33_caja, formula_volumen_4demarzo(X33_caja),label='limite = 0.01')
axs[1, 2].scatter(X14_caja,formula_volumen_4demarzo(X14_caja),label = 'limite = 0.0001')
axs[1, 2].scatter(X34_caja,formula_volumen_4demarzo(X34_caja),label = 'limite = 0.0001')
axs[1,2].legend()
axs[1, 2].set_title('Funcion caja')
plt.title('Metodo Biseccion ')
plt.show()