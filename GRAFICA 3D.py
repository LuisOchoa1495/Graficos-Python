import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

vector1 = np.array([[4,4,9,4]])
vector2 = np.array([[2,2,2,2]])
vector3 = np.array([[7,5,7,7]])

figura=plt.figure()
plano=figura.add_subplot(111,projection='3d')

plano.plot_wireframe(vector1,vector2,vector3)
plano.scatter(4,5,6,color='green',marker='o')

plano.set_xlim([0,10])
plano.set_ylim([0,10])
plano.set_zlim([0,10])

plano.set_xlabel('EJE X')
plano.set_ylabel('EJE Y')
plano.set_zlabel('EJE Z')

plt.title("GRAFICAS 3D")
plt.show()