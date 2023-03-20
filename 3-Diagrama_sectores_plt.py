import matplotlib.pyplot as plt

# Define Data Coordinates
pet = ['Dog', 'Cat', 'Rabbit', 'Parrot', 'Fish']
owner = [50, 15, 8, 20, 12]

# Plot
plt.pie(owner, labels=pet,explode=(0.1,0,0,0,0),startangle=90, autopct='%1.1f%%') 

# Title fontsize
plt.title('Diagrama de sectores',fontsize=20)

# Display
plt.show() 