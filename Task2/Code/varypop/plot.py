import numpy as np
import matplotlib.pyplot as plt

mean_funcs = np.array([])
std_funcs = np.array([])
pop_sizes = [5, 10, 25, 50, 100]
means = np.array([])
std_devs = np.array([])
mean_times = []
std_times = []

for pop_size in pop_sizes:
    iters = []
    fs = []
    for i in range(50):
        results = np.load('popis%d/results%d.npy' % (pop_size, i))
        fs.append(results[1][-1][0])
        iters.append(results[2])
    mean_funcs = np.append(mean_funcs, np.mean(fs))
    std_funcs = np.append(std_funcs, np.std(fs))
    means = np.append(means, np.mean(iters))
    std_devs = np.append(std_devs,np.std(iters))
    time = np.load('popis%d/Times.npy' % pop_size)
    mean_times.append(np.mean(time))
    std_times.append(np.std(time))

print(means)
print(std_devs)
print(mean_funcs)
print(std_funcs)
print(mean_times)
print(std_times)
fig1 = plt.figure()
ax = fig1.add_subplot(211)
ax.set_xlabel('Population Size')
ax.set_ylabel('Iterations')
l1 = ax.errorbar(pop_sizes, means, yerr = std_devs,fmt='-o', ms = 3,\
    ecolor = 'r', elinewidth = 1, label = 'Iterations',  solid_capstyle='projecting', capsize=5)
ax2 = ax.twinx()
l2 = ax2.errorbar(pop_sizes, mean_funcs, yerr = std_funcs, fmt = 'g-o', ms = 3, \
    ecolor = 'c', elinewidth = 1, label = 'Objective Values',  solid_capstyle='projecting', capsize=5)
ax2.set_ylabel('Best objective values')
lines,labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.grid(True, which  = 'both', axis = 'both', linewidth = 0.1)
ax2.legend(lines + lines2, labels + labels2, loc = 'upper right')
axt = fig1.add_subplot(212)
axt.errorbar(pop_sizes, mean_times, yerr = std_times, \
             ecolor = 'r', elinewidth = 1,  solid_capstyle='projecting', capsize=5)
axt.set_xlabel('Population Size')
axt.set_ylabel('Time/s')
axt.grid(True)
plt.tight_layout()
# fig = plt.figure()
# plt.plot(iters)
plt.show()
