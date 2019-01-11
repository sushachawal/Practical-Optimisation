import numpy as np


def ga(objfunc, n, lb, ub, startseeds):
    pop_size = 20
    pop = np.random.rand(n, pop_size)
    pop = np.dot((ub-lb), pop) + lb
    pass


def mutate_pop(population, varmat, nzero, ns, ub, lb):
    mutate_covariances(varmat, nzero, ns, ub, lb)
    mean = np.zeros(np.size(varmat, 1))
    for i in range(0, np.size(pop, 1)):
        population[:, i] += np.random.multivariate_normal(mean, varmat)


def mutate_covariances(vars, n0, ns, ub, lb):
    n = np.size(ns, 0)
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

def breed():
    pass


if __name__ == "__main__":
    ub = np.full((5,1), 500)
    lb = np.full((5,1), -500)
    n = 5
    pop = np.random.rand(n, 4)
    pop = pop*(ub-lb) + lb
    nis = np.random.standard_normal((n, n))
    nis = (nis + nis.T) / 2
    n0 = np.random.standard_normal()
    covars = nis
    for i in range(0, 20):
        mutate_pop(pop, covars, n0, nis, ub, lb)
        print("pop after %d mutation:" % (i + 1))
        print(pop)
