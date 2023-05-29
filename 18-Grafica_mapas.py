import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

direccion = 'tu directorio //mexican-states-master'
direccion2 = 'tu directorio\\carpeta\\'
shapefile = gpd.read_file(direccion+'\mexican-states.shp')
shapefile.head(5)
estados = pd.read_csv(direccion2+'UniMex.csv',encoding='UTF-8',low_memory=False)
estados.head(5)
shapefile = shapefile.merge(
                     right = estados,
                     left_on = 'name',
                     right_on = 'Estado',
                     how = 'left'
                     )
shapefile.plot(column = 'Numero_Universidades',
               legend = True, 
            legend_kwds = {
              'label': "Número de Universidades",
              'orientation': "horizontal"
              },
            cmap = 'Greens')