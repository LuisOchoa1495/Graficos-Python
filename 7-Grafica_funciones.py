import matplotlib.pyplot as plt

# Función cuadrática.
def funcion1(x):
    return (x**2) 

# Función lineal.
def funcion2(x):
    return 4*x + 5

# Valores del eje X que toma el gráfico.
x = range(-15, 15)

# Graficar ambas funciones.
plt.plot(x, [funcion1(i) for i in x],color="blue")
plt.plot(x, [funcion2(i) for i in x],color="red")

# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")


# Limitar los valores de los ejes.
plt.xlim(-15, 15)
plt.ylim(-15, 15)

#Titulo
plt.title("GRAFICA DE FUNCIONES")

# Mostrarlo.
plt.grid()
plt.show()
