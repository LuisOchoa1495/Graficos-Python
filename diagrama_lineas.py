import matplotlib.pyplot as plt

years=[2019,2020,2021,2022]
sales_a=[17,18,23,32]
sales_b=[11,12,26,32]

plt.plot(years, sales_a,color='black',linewidth=3,label="EMPRESA A")
plt.plot(years, sales_b,color='blue',linewidth=3,label="EMPRESA B")

plt.title("Diagrama de linea")
plt.xlabel("Year")
plt.ylabel("Sale")
plt.xticks(years)

plt.legend(loc="upper left")
plt.grid()
plt.show()

