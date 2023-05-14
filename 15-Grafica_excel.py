import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
width=0.25
workbook="Notas.xlsx"
df = pd.read_excel(workbook)
print(df.head())

datos=df[{"name","Algebra","Quimica"}]
x=np.arange(len(datos))
algebra=df[{"Algebra"}]
quimica=df[{"Quimica"}]
df['name'] = df['name'].astype("string") # Let them be strings!
print(algebra)
fig, ax = plt.subplots()
#datos.plot.bar(x=["name"], y=["Algebra"],width=width,rot=0)
df.plot(x=['name'], y=['Algebra','Quimica'],kind="bar",rot=0,ax=ax)


plt.show()