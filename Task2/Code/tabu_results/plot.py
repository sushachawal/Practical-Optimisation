import numpy as np
import matplotlib.pyplot as plt

mean_funcs = np.array([])
std_funcs = np.array([])
K_sizes = [10, 20]
means = np.array([])
std_devs = np.array([])
mean_times = []
std_times = []
for K_size in K_sizes:
    iters = []
    fs = []
    for i in range(50):
        results = np.load('Kis%d/results%d.npy' % (K_size, i))
        fs.append(results[2])
        iters.append(results[3])
    t = np.load('Kis%d/time.npy' % K_size)
    mean_times.append(np.mean(t))
    std_times.append(np.std(t))
    mean_funcs = np.append(mean_funcs, np.mean(fs))
    std_funcs = np.append(std_funcs, np.std(fs))
    means = np.append(means, np.mean(iters))
    std_devs = np.append(std_devs,np.std(iters))

print(means)
print(std_devs)
print(mean_funcs)
print(std_funcs)
print(mean_times)
print(std_times)
fig1 = plt.figure()
ax = fig1.add_subplot(211)
ax.set_xlabel('K values')
ax.set_ylabel('Iterations')
l1 = ax.errorbar(K_sizes, means, yerr = std_devs,fmt='-o', ms = 3,\
    ecolor = 'r', elinewidth = 1, label = 'Iterations')
ax2 = ax.twinx()
l2 = ax2.errorbar(K_sizes, mean_funcs, yerr = std_funcs, fmt = 'g-o', ms = 3, \
    ecolor = 'c', elinewidth = 1, label = 'Objective Values')
ax2.set_ylabel('Best objective values')
lines,labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.grid(True, which  = 'both', axis = 'both', linewidth = 0.1)
ax2.legend(lines + lines2, labels + labels2, loc = 'upper right')
plt.tight_layout()

axt = fig1.add_subplot(212)
axt.set_xlabel('K values')
axt.set_ylabel('time/s')
axt.errorbar(K_sizes, mean_times, yerr = std_times, \
                  ecolor = 'c', elinewidth = 1, label = 'Objective Values')
axt.grid(True)


mean_funcs = np.array([])
std_funcs = np.array([])
means = np.array([])
std_devs = np.array([])
mean_times = []
std_times = []
tols = [1, 0.5, 0.25, 1e-1, 1e-2, 1e-3]

for tol in range(len(tols)):
    iters = []
    fs = []
    for i in range(50):
        results = np.load('tolis%d/results%d.npy' % (tol, i))
        fs.append(results[2])
        iters.append(results[3])
    t = np.load('tolis%d/time.npy' % tol)
    mean_times.append(np.mean(t))
    std_times.append(np.std(t))
    mean_funcs = np.append(mean_funcs, np.mean(fs))
    std_funcs = np.append(std_funcs, np.std(fs))
    means = np.append(means, np.mean(iters))
    std_devs = np.append(std_devs,np.std(iters))

print(means)
print(std_devs)
print(mean_funcs)
print(std_funcs)
print(mean_times)
print(std_times)
fig2 = plt.figure()
ax = fig2.add_subplot(211)
ax.set_xlabel('Tolerance values')
ax.set_ylabel('Iterations')
l1 = ax.errorbar(tols, means, yerr = std_devs,fmt='-o', ms = 3,\
                 ecolor = 'r', elinewidth = 1, label = 'Iterations')
ax2 = ax.twinx()
l2 = ax2.errorbar(tols, mean_funcs, yerr = std_funcs, fmt = 'g-o', ms = 3, \
                  ecolor = 'c', elinewidth = 1, label = 'Objective Values')
ax2.set_ylabel('Best objective values')
lines,labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
plt.grid(True, which  = 'both', axis = 'both', linewidth = 0.1)
ax2.legend(lines + lines2, labels + labels2, loc = 'upper right')
plt.tight_layout()

axt = fig2.add_subplot(212)
axt.set_xlabel('Tolerance values')
axt.set_ylabel('time/s')
axt.errorbar(tols, mean_times, yerr = std_times, \
             ecolor = 'c', elinewidth = 1, label = 'Objective Values')
axt.grid(True)

# fig = plt.figure()
# plt.plot(iters)
plt.show()
