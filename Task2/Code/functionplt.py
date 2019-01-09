import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def schwefel(x):
    return np.sum(np.multiply(-x,np.sin(np.sqrt(np.abs(x)))))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
X, Y = np.mgrid[-500:500:50j, -500:500:50j]
Z = -np.multiply(X, np.sin(np.sqrt(np.abs(X)))) - np.multiply(Y, np.sin(np.sqrt(np.abs(Y))))
surf = ax.plot_surface(X, Y, Z, cmap="autumn_r", linewidth=0.3, edgecolors = 'k')
ax.contour(X, Y, Z, 10, cmap="autumn_r", linestyles="solid", offset=-850)
fig.colorbar(surf)
plt.show()
