import matplotlib.pyplot as plt

#Funcion cuadratica
def funcion1(x):
    return(x**2)

#Funcion lineal
def funcion2(x):
    return(4*x+5)

# Valores del eje x que toma el grafico
x= range(-15,15)

#Grafica de funciones
plt.plot(x,[funcion1(i) for i in x],color="blue",label="Funcion Cuadratica")
plt.plot(x,[funcion2(i) for i in x],color="red",label="Funcion Lineal")

#Estableces el color de los ejes
plt.axhline(0,color="black")
plt.axvline(0,color="black")

#limitar valores de los ejes
plt.xlim(-15,15)
plt.ylim(-15,15)

#Title
plt.title("Grafica de funciones")
plt.legend(loc="lower right")

plt.grid()
plt.show()
