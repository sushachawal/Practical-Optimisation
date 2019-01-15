import numpy as np
import matplotlib.pyplot as plt

ps = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
mean_funcs = np.array([])
std_funcs = np.array([])
means = np.array([])
std_devs = np.array([])
mean_times = []
std_times = []

for p in range(9):
    iters = []
    fs = []
    for i in range(50):
        results = np.load('pis%d/results%d.npy' % (p, i))
        fs.append(results[1][-1][0])
        iters.append(results[2])
    mean_funcs = np.append(mean_funcs, np.mean(fs))
    std_funcs = np.append(std_funcs, np.std(fs))
    means = np.append(means, np.mean(iters))
    std_devs = np.append(std_devs,np.std(iters))
    time = np.load('pis%d/Times.npy' % p)
    mean_times.append(np.mean(time))
    std_times.append(np.std(time))


print(means)
print(std_devs)
print(mean_funcs)
print(std_funcs)
print(mean_times)
print(std_times)
fig1 = plt.figure()
ax = fig1.add_subplot(311)
ax.set_xlabel('Probability of mutation')
ax.set_ylabel('Iterations')
l1 = ax.errorbar(ps, means, yerr = std_devs,fmt='-o', ms = 3,\
                 ecolor = 'r', elinewidth = 1, label = 'Iterations', solid_capstyle='projecting', capsize=5)
plt.grid(True, which  = 'both', axis = 'both', linewidth = 0.1)
ax2 = fig1.add_subplot(312)
l2 = ax2.errorbar(ps, mean_funcs, yerr = std_funcs, fmt = 'g-o', ms = 3, \
                  ecolor = 'c', elinewidth = 1, label = 'Objective Values',\
                  solid_capstyle='projecting', capsize=5)
ax2.set_xlabel('Probability of mutation')
ax2.set_ylabel('Best objective values')
plt.grid(True, which  = 'both', axis = 'both', linewidth = 0.1)
ax3 = fig1.add_subplot(313)
ax3.plot(ps, mean_times)
ax3.set_xlabel('Probability of mutation')
ax3.set_ylabel('Time/s')
ax3.grid(True, linewidth = 0.1)
plt.tight_layout()
# fig = plt.figure()
# plt.plot(iters)
plt.show()
