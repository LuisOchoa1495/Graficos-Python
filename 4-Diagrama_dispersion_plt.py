import matplotlib.pyplot as plt

tiempo_algebra = [1, 3, 5, 7]
notas_algebra = [10, 12, 14, 16]
tiempo_quimica = [2, 4 , 6 , 8]
notas_quimica = [8, 10, 11.5, 13]

#Configurar las características del gráfico
plt.scatter(tiempo_algebra, notas_algebra, label = 'Algebra',color = 'red')
plt.scatter(tiempo_quimica, notas_quimica,label = 'Quimica', color = 'purple')

#Definir título y nombres de ejes
plt.title('Diagrama de dispersión')
plt.ylabel('Tiempo de estudio')
plt.xlabel('Horas de estudio')

#Mostrar leyenda y figura
plt.legend()
plt.grid()
plt.show()