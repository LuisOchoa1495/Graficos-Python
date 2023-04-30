from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Coordendas de Tenerife, en grados
lat, lon = 28.2419, -16.5937

# Mapa en alta resolución (h) con proyección mercator
map = Basemap(projection='merc', lat_0 = lat, lon_0 = lon,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=lon-0.5, llcrnrlat=lat-0.5,
    urcrnrlon=lon+0.5, urcrnrlat=lat+0.5)

# Líneas de costas y paises, aunque en este ejemplo no se ven
map.drawcoastlines()
map.drawcountries()

map.fillcontinents(color = '#cc9966')
map.drawmapboundary()

# Coordenadas para dibujar en el map
lats = [28.5068, 28.2617, 28.3310]
lons = [-16.2531, -16.5526, -16.8353]

x,y = map(lons, lats)
map.plot(x, y, '*r', markersize=6)

plt.show()