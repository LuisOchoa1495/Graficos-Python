import numpy as np
import matplotlib.pyplot as plt
import animatplot as amp

x= np.linespace(0,1,50)
t=np.linespace(0,1,20)

x,t=np.meshgrid(x,t)
y=np.sin(2*np.pi*(x+t))

block=amp.blocks.Line(x,y)
anim=amp.Animation([block])

plt.show()