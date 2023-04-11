import math
import matplotlib.pyplot as plt
import numpy as np

fn_1 = np.sin
fn_2 = np.cos
fn_3 = np.tan

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
points = [i * np.pi/2 for i in range(-4, 5)]
labels = ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "3π/2", "2π"]

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.plot(x, fn_1(x),label="Seno")
ax.plot(x, fn_2(x),label="Coseno")
ax.plot(x, fn_3(x),label="Tangente")
ax.set_xticks(points)
ax.set_xticklabels(labels)

plt.ylim(-1, 1)
ax.hlines(0, -7,7, "k")
ax.vlines(0, -5, 5, "k")
plt.title("Graficas Trigonometricas")
plt.grid()
plt.legend()
plt.show()