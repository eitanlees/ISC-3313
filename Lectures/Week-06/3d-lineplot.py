import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')


# Data for a three-dimensional line
t = np.linspace(0, 10*np.pi, 1000)

x = np.sin(t)
y = np.cos(t)
z = t

ax.plot3D(x, y, z)

plt.show()
