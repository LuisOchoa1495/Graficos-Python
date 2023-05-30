import pandas as pd
import matplotlib.pyplot as plt

tables=pd.read_html('https://www.nbamaniacs.com/palmares-nba/')
print(f'Número total de tablas: {len(tables)}')

datos=(tables[0].head())
dataframe=pd.DataFrame(datos[{'Franquicia','Títulos'}])
print(dataframe)
dataframe.plot(x="Franquicia",kind="bar",rot=10)
plt.title("Top 5 - Ganadores NBA")
plt.show()
