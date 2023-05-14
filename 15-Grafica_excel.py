import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
width=0.25
workbook="Notas.xlsx"
df = pd.read_excel(workbook)
print(df.head())

datos=df[{"name","Algebra","Quimica"}]

datos.plot.bar(x="name", y="Algebra",width=width,rot=0)
datos.plot(x="name",kind="bar",rot=0)
plt.title("Puntajes")
plt.xlabel("Nombres")
plt.ylabel("Puntajes")
plt.grid()
plt.show()