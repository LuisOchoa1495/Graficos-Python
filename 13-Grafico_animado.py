import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

fig=plt.figure()

ax1=fig.add_subplot(2, 1, 1)
x= np.linspace(0,1,50)
t= np.linspace(0,1,20)
x,t=np.meshgrid(x,t)
y=np.cos(2*np.pi*(x+t))
block=amp.blocks.Line(x,y)
anim_1=amp.Animation([block])
anim_1.controls()

ax2=fig.add_subplot(2, 1, 2)
a=np.sin(2*np.pi*(x+t))
block_2=amp.blocks.Line(x,a)
anim_2=amp.Animation([block_2])
anim_2.controls()

"----------------------------------------------------------------"
plt.suptitle("GRAFICOS ANIMADOS",fontsize=18)
plt.show()

