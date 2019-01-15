import numpy as np
import matplotlib.pyplot as plt

iters = []
pop_sizes = [5, 10, 25, 50, 100]
means = np.array([])
std_devs = np.array([])

for pop_size in pop_sizes:
    for i in range(50):
        results = np.load('popis%d/results%d.npy' % (pop_size, i))
        iters.append(results[2])
    np.append(means, np.mean(iters))
    np.append(std_devs,np.std(iters))

fig1 = plt.figure()
ax = fig1.addsubplot(111)
ax.plot(pop_sizes, means)
ax.plot(pop_sizes, means+std_devs, 'rx')
ax.plot(pop_sizes, means-std_devs, 'rx')

# fig = plt.figure()
# plt.plot(iters)
# plt.show()
