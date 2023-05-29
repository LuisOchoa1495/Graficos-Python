import mysql.connector
import pandas as pd 
import matplotlib.pyplot as plt
#conexion
conexion = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="prueba"
    )
#Prueba conexion
my_data1 = pd.read_sql("SELECT * FROM productos",conexion)
my_data2 = pd.read_sql(
    "SELECT c.categoria,sum(p.cantidad) as total FROM productos as p INNER JOIN categorias as c ON c.idcategoria=p.categoria GROUP BY c.categoria",
    conexion)
labels=my_data2['categoria']
print(labels)
my_data2.plot(y="total", kind="pie", autopct='%1.01f%%',labels=labels,legend=False)
plt.title("Porcentaje de Categorias")
plt.show()


"""
#CONSULTAS 
SELECT * FROM productos;
#GRAFICO
SELECT c.categoria,sum(p.cantidad) FROM productos as p INNER JOIN categorias as c ON c.idcategoria=p.categoria GROUP BY c.categoria
"""