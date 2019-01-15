import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import sys

def schwefel(x):
    return np.sum(np.multiply(-x,np.sin(np.sqrt(np.abs(x)))), axis=0)


def load_points_to_plot(run, generation):
    results = np.load('results%d.npy' % run)
    zs = results[1][min(generation, len(results[0])-1)]
    xs = results[0][min(generation, len(results[0])-1)]
    ys = xs
    xs = xs[0, :]
    ys = ys[1, :]
    return (xs, ys, zs)


def generate_obj_funcs_plot(run):
    results = np.load('results%d.npy' % run)
    results = results[1]
    minvals = []
    maxvals = []
    average = []
    for arr in results:
        minvals.append(np.min(arr))
        average.append(np.mean(arr))
        maxvals.append(np.max(arr))
    return (minvals, average, maxvals)


def generate_iteration_vector(numruns):
    iters = []
    for i in range(numruns):
        results = np.load('results%d.npy' % i)
        iters.append(results[2])
    return iters

if __name__ == "__main__":
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection="3d")
    X, Y = np.mgrid[-600:600:50j, -600:600:50j]
    Z = -np.multiply(X, np.sin(np.sqrt(np.abs(X)))) - np.multiply(Y, np.sin(np.sqrt(np.abs(Y))))
    # surf = ax.plot_surface(X, Y, Z, cmap="autumn_r", linewidth=0.3, edgecolors = 'k')
    # ax.contour(X, Y, Z, 10, cmap="autumn_r", linestyles="solid", offset=-850)
    # fig.colorbar(surf)

    runnum = int(sys.argv[1])


    points = load_points_to_plot(runnum, 0)
    fig2 = plt.figure()
    ax11 = fig2.add_subplot(221)
    contour = ax11.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
    ax11.scatter(points[0], points[1], c='b', marker = 'o')
    ax11.set_title('Population points after 0 iterations')
    points = load_points_to_plot(runnum, 10)
    ax12 = fig2.add_subplot(222)
    contour = ax12.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
    ax12.scatter(points[0], points[1], c='b', marker='o')
    ax12.set_title('Population points after 100 iterations')
    points = load_points_to_plot(runnum, 100)
    ax21 = fig2.add_subplot(223)
    ax21.set_title('Population points after 1000 iterations')
    contour = ax21.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
    ax21.scatter(points[0], points[1], c='b', marker='o')
    points = load_points_to_plot(runnum, -1)
    ax22 = fig2.add_subplot(224)
    ax22.set_title('Final population points')
    contour = ax22.contour(X, Y, Z, cmap="autumn_r", linestyles="solid")
    ax22.scatter(points[0], points[1], c='b', marker='o')



    fig3 = plt.figure()
    axfuncs = fig3.add_subplot(111)
    obj_funcs = generate_obj_funcs_plot(runnum)
    axfuncs.plot(obj_funcs[0], '-r', label='Minimum function values')
    axfuncs.plot(obj_funcs[1], '--g', label='Average function values')
    axfuncs.plot(obj_funcs[2], '-b', label='Maximum function values')
    axfuncs.legend(loc='upper right')
    axfuncs.set_xlabel('Number of iterations')
    axfuncs.grid(True, linewidth = 0.1)
    fig4 = plt.figure()
    axnew = fig4.add_subplot(111)
    axnew.plot(generate_iteration_vector(50), '.-')
    axnew.set_xlabel('Run number')
    axnew.set_ylabel('Number of iterations')
    axnew.grid(True, linewidth=0.1)
    plt.show()
