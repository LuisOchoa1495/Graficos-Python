import pandas as pd
import re
desired_width = 320
pd.set_option('display.width', desired_width)


# Leer las tablas en pandas
inflation_tables = pd.read_html('https://en.wikipedia.org/wiki/List_of_countries_by_inflation_rate')

# Imprimir el número total de tablas
print(f'Número total de tablas: {len(inflation_tables)}')

# Imprimir las primeras filas de todas las tablas en la página
for i in range(len(inflation_tables)):
  print(inflation_tables[i].head())