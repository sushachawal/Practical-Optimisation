import numpy as np
from functionplt import schwefel
from time import time
import numba


def ga(objfunc, n, lb, ub, startseeds = None):
    pop_size = 100
    pop = np.random.rand(n, pop_size)
    pop = pop * (ub - lb) + lb
    funcs = objfunc(pop)
    order = funcs.argsort()
    nis = np.random.standard_normal((n, n))
    nis = (nis + nis.T) / 2
    n0 = np.random.standard_normal()
    covars = nis
    iter = 0
    tol = 1e-3
    p = 0.5
    mu = max(pop.shape[1]//7, 2)
    results = []
    populations = []
    functions = []
    while(abs(funcs[order[-1]] - funcs[order[0]]) > tol):
        pop = breed(pop[:, order[0:mu]], pop_size)
        mask = np.random.choice(a=[False, True], size=pop_size, p=[p, 1-p])
        mutate_pop(pop, mask, covars, n0, nis, ub, lb)
        pop = pop[:, np.logical_and(pop >= lb, pop <= ub).all(axis=0)]
        funcs = objfunc(pop)
        order = funcs.argsort()
        if (iter % 10 == 0):
            populations.append(pop)
            functions.append(funcs)
        iter += 1
        if(iter > 10000):
            print("Max Iterations reached!")
            break
    populations.append(pop)
    functions.append(funcs)
    results.append(populations)
    results.append(results)
    results.append(iter)
    return results


def mutate_pop(population, mask, varmat, nzero, ns, ub, lb):
    mutate_covariances(varmat, nzero, ns, ub, lb)
    mean = np.zeros(np.shape(varmat)[1])
    for i in (i for i in range(np.size(population, 1)) if mask[i] == True):
        population[:, i] += np.random.multivariate_normal(mean, varmat)


def mutate_covariances(vars, n0, ns, ub, lb):
    n = ns.shape[0]
    alphas = np.zeros((n, n))
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            alphas[i, j] = 0.5 * np.arctan2(2 * vars[i, j] , vars[i][i] ** 2 - vars[j][j] ** 2)
    tau = 1 / (np.sqrt(2. * np.sqrt(n)))
    tau_dash = 1 / (np.sqrt(2. * n))
    for i in range(0, n):
        vars[i, i] = np.clip(vars[i, i] * np.exp(tau_dash * n0 + tau * ns[i, i]),lb[i], ub[j])
    beta = 0.0873
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            alphas[i, j] = alphas[i, j] + beta * ns[i, j]
            vars[i, j] = vars[j, i] = \
                0.5 * (vars[i, i] ** 2 - vars[j, j] ** 2) * np.tan(2. * alphas[i, j])
    assert np.allclose(vars, vars.T, atol=1e-8), "Asymmetric covariance matrix generated!"

@numba.njit
def breed(parents, num_child):
    size = parents.shape[1]
    n = parents.shape[0]
    children = np.zeros((n,num_child))
    for j in range(0, num_child):
        for i in range(0,n):
            children[i,j] = parents[i, np.random.randint(size)]
    return children

if __name__ == "__main__":
    n = 2
    ub = np.full((n,1), 500)
    lb = np.full((n,1), -500)
    times = []
    for i in range(50):
        start = time()
        results = ga(schwefel, n, lb, ub)
        end = time()
        times.append(end-start)
        np.save('results%d.npy' % i, results)
        print("Time elapsed is: ", end-start)
    np.save(times)
