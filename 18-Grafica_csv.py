import pandas as pd 
import matplotlib.pyplot as plt

#https://www.datosabiertos.gob.pe/group/datos-abiertos-de-covid-19
#leer las tablas
csv=pd.read_csv('fallecidos_covid.csv',sep=';',decimal=',')
dataframe=pd.DataFrame(csv[{"FECHA_FALLECIMIENTO","SEXO","DEPARTAMENTO"}])
sexo=dataframe["SEXO"].value_counts()
departamento=dataframe["DEPARTAMENTO"].value_counts().head()
print(departamento)
"----------Grafica 1---------"
plt.subplot(1, 2, 1)
sexo.plot(kind='pie',autopct='%1.01f%%')
plt.title("SEXO")
"----------Grafica 2---------"
plt.subplot(1, 2, 2)
departamento.plot(kind='bar',rot=20)
plt.title("DEPARTAMENTOS")
plt.xticks(fontsize=9)

plt.suptitle("GRAFICA COVID-19 - FALLECIDOS")
plt.show()

