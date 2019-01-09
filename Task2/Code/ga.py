import numpy as np


def ga(objfunc, lb, ub, startseeds):
    pass

def mutate_vector(x, vars, n0, ns):
    mutate_covariances(vars, n0, ns)
    mean = np.zeros(np.size(x,0))
    return x + np.random.multivariate_normal(mean, vars)

def mutate_covariances(vars, n0, ns):
    n = np.size(ns, 0)
    alphas = np.zeros((n,n))
    for j in range(0,n-1):
        for i in range(j+1,n):
            alphas[i,j] = np.nan_to_num(0.5*np.arctan((2*vars[i,j])/(vars[i][i]**2 - vars[j][j]**2)))
    tau = 1/(np.sqrt(2.*np.sqrt(n)))
    tau_dash = 1 / (np.sqrt(2. * n))
    for i in range(0,n):
        vars[i,i] = np.nan_to_num(vars[i, i] * np.exp(tau_dash*n0 + tau*ns[i,i]))
    beta = 0.0873
    for j in range(0, n-1):
        for i in range(j+1, n):
            alphas[i, j] = np.nan_to_num(alphas[i, j] + beta * ns[i, j])
            vars[i, j] = vars[j, i] = np.nan_to_num( 0.5 * (vars[i, i] ** 2 - vars[j, j] ** 2) * np.tan(2. * alphas[i, j]))
    assert vars.all() == (vars.T).all(), "Asymmetric covariance matrix generated!"


def breed():
    pass

if __name__ == "__main__":
    n = 5
    x = np.random.rand(n)
    x = x*1000 - 500
    nis = np.random.standard_normal((n,n))
    nis = (nis + nis.T)/2
    n0 = np.random.standard_normal()
    covars = nis
    for i in range(0,20):
        x = mutate_vector(x,covars, n0, nis)
        print("x after %d mutation:" % (i+1))
        print(x)