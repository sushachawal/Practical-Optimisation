import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import sys

X, Y = np.mgrid[-600:600:50j, -600:600:50j]
Z = -np.multiply(X, np.sin(np.sqrt(np.abs(X)))) - np.multiply(Y, np.sin(np.sqrt(np.abs(Y))))

fig = plt.figure()
idx = int(sys.argv[1])

results = np.load('Kis10/results%d.npy' % idx)
ax11 = fig.add_subplot(221)
ax11.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
ax11.scatter(results[0][0, :], results[0][1, :], c='b', marker='.')
ax11.set_title('Points evaluated for K is 10')

results = np.load('Kis20/results%d.npy' % idx)
ax12 = fig.add_subplot(222)
ax12.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
ax12.scatter(results[0][0, :], results[0][1, :], c='b', marker='.')
ax12.set_title('Points evaluated for K is 20')

results = np.load('Kis50/results%d.npy' % idx)
ax21 = fig.add_subplot(223)
ax21.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
ax21.scatter(results[0][0, :], results[0][1, :], c='b', marker='.')
ax21.set_title('Points evaluated for K is 50')

results = np.load('Kis500/results%d.npy' % idx)
ax22 = fig.add_subplot(224)
ax22.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
ax22.scatter(results[0][0, :], results[0][1, :], c='b', marker='.')
ax22.set_title('Points evaluated for K is 500')

plt.show()
