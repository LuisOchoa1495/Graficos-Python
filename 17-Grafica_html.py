import pandas as pd
import matplotlib.pyplot as plt

# Leer las tablas en pandas
tables = pd.read_html('https://www.nbamaniacs.com/palmares-nba/')
# Imprimir el número total de tablas
print(f'Número total de tablas: {len(tables)}')
# Imprimir las primeras filas de todas las tablas en la página
datos=(tables[0].head())
dataframe=pd.DataFrame(datos[{'Franquicia','Títulos'}])
print(dataframe)
dataframe.plot(x="Franquicia",kind="bar",rot=10)
plt.title("Top 5 - Ganadores NBA")
plt.grid()
plt.show()

"""
# Imprimir las primeras filas de todas las tablas en la página
for i in range(len(tables)):
  print(tables[i].head())
"""

