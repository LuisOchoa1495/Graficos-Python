import numpy as np
import matplotlib.pyplot as plt


# Semilla para reproducibilidad
np.random.seed(2)

# Datos
data = np.random.random((8, 12))

# Etiquetas
xlabs = ["ENERO", "FEBRERO", "MARZO", "ABRIL",
         "MAYO", "JUNIO", "JULIO", "AGOSTO","SEPTIEMBRE",
         "OCTUBRE","NOVIEMBRE", "DICIEMBRE"]
ylabs = ["LIMA", "PIURA", "AYACUCHO", "CUSCO",
         "AREQUIPA", "CAJAMARCA", "PUNO", "ICA"]
         
# Mapa de calor
fig, ax = plt.subplots()
im=ax.imshow(data)

# Agregar las etiquetas
ax.set_xticks(np.arange(len(xlabs)), labels = xlabs)
ax.set_yticks(np.arange(len(ylabs)), labels = ylabs)

# Agregar la leyenda
cbar = ax.figure.colorbar(im, ax = ax)
cbar.ax.set_ylabel("Leyenda", rotation = -90, va = "bottom")

# Loop over data dimensions and create text annotations.
for i in range(len(ylabs)):
    for j in range(len(xlabs)):
        text = ax.text(j, i, round(data[i, j],1),ha="center", va="center", color="white")



plt.setp(ax.get_xticklabels(), rotation = 40,
         ha = "right", rotation_mode = "anchor")


plt.title("Grafica de calor")
plt.show()

