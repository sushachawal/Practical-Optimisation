import numpy as np
from functionplt import schwefel
from collections import deque
from time import time

class grid:
    def __init__(self, ub, lb, K):
        assert(ub.shape == lb.shape), "Upper Bound and Lower Bound shapes " \
                                      "are not compatible!"
        assert((ub > lb).any()), "ub value smaller than lb value"
        self.n = ub.shape[0]
        self.ub = ub
        self.lb = lb
        self.count = np.zeros([K]*self.n)
        self.grid_step = (ub-lb)/K


    def inc(self, x):
        temp = np.floor_divide((x - self.lb), self.grid_step)
        idx = tuple(temp.flatten().astype(int))
        self.count[idx] += 1


    def gen_rand_n_min_sampled(self, n):
        i = np.random.randint(n)
        idx = np.unravel_index(self.count.flatten().argpartition(i)[i],
                               self.count.shape)
        lower = self.lb + \
                np.asarray(idx).reshape(self.n, 1) * self.grid_step
        upper = self.lb + \
                (np.asarray(idx) + 1).reshape(self.n , 1) * self.grid_step
        return gen_sample(self.n, upper, lower)


def tabu(objfunc, n, lb, ub, least_sampled=5, tolerance = 1e-8, SI=10, SD=15, SSR=25, N = 5, M = 10, K = 5):
    assert((ub>lb).any()), "ub value smaller than lb value!"
    results = []
    base_point = shotgun(objfunc, n, lb, ub, 10)
    prev_func = objfunc(base_point)
    delta = 10
    sample_grid = grid(ub,lb, K)
    assert(least_sampled < ((K*K) - 1) ), "Lower least_sampled value!"
    tabu_locs = deque([base_point])
    best_locs = base_point
    best_funcs = np.array([prev_func])
    counter = 0
    tol = np.full((n,1), tolerance)
    func_tol = 1e-8
    points = base_point
    iter = 0
    while((delta > tol).all()):
        if(counter < SSR):
            if(counter > SI):
                base_point = np.mean(best_locs, axis=1).reshape(n, 1)
            if(counter > SD):
                base_point = sample_grid.gen_rand_n_min_sampled(least_sampled)
            base_point = local_search(objfunc,base_point, delta, tabu_locs, N)
            sample_grid.inc(base_point)
            func = objfunc(base_point)
            if(len(best_funcs) >= M):
                if(True in (func < f for f in best_funcs)):
                    best_funcs = np.append(best_funcs[0:-1], func)
                    best_locs = np.hstack((best_locs[:, 0:-1], base_point))
            else:
                best_funcs = np.append(best_funcs, func)
                best_locs = np.hstack((best_locs, base_point))
            order = best_funcs.argsort()
            best_locs = best_locs[:,order]
            best_funcs = np.sort(best_funcs)
            if(abs(func - prev_func)/prev_func < func_tol):
                counter += 1
            else:
                counter = 0
            prev_func = func
        else:
            delta *= 0.9
            counter = 0
            base_point = best_locs[:, 0].reshape(n, 1)
        iter += 1
        points = np.hstack((points,base_point))
        if(iter> 10000):
            print("Max iterations reached!")
            break
    results.append(points)
    results.append(best_locs[:,0].reshape(n,1))
    results.append(best_funcs[0])
    results.append(iter)
    return results


def local_search(objfunc, base_point, delta, tabu_locs, N):
    n = base_point.shape[0]
    prev_func = objfunc(base_point)
    best = np.inf
    best_p = base_point
    for i in range(n):
        step = np.zeros(base_point.shape)
        step[i] = delta
        point = base_point + step
        if (point >= lb).all() and (point <= ub).all():
            temp = objfunc(point)
            if temp < best and (False in ((point == tab).all()
                                          for tab in tabu_locs)):
                best = temp
                best_p = point
        step = np.zeros(base_point.shape)
        step[i] = -delta
        point = base_point + step
        if (point >= lb).all() and (point <= ub).all():
            temp = objfunc(point)
            if temp < best and (False in ((point == tab).all()
                                          for tab in tabu_locs)):
                best = temp
                best_p = point

    append_tabu(best_p, tabu_locs, N)
    if(best < prev_func):
        best_p += (best_p - base_point)
        append_tabu(best_p, tabu_locs, N)
    return best_p


def append_tabu(point, tabu_locs, N):
    if (len(tabu_locs) < N):
        tabu_locs.append(point)
    else:
        tabu_locs.popleft()
        tabu_locs.append(point)


def shotgun(objfunc, n, lb, ub, ntrials):
    func = np.inf
    for i in range(ntrials):
        temp = gen_sample(n, ub, lb)
        if(objfunc(temp) < func):
            sample = temp
    return sample


def gen_sample(n, ub, lb):
    return np.random.rand(n, 1) * (ub - lb) + lb


if __name__ == "__main__":
    n = 5
    ub = np.full((n, 1), 500)
    lb = np.full((n, 1), -500)

    times = []
    best_funcs = []
    for i in range(100):
        start = time()
        results = tabu(schwefel, n, lb, ub, 5, SI=10, SD=15, SSR=25, K=5)
        end = time()
        times.append(end-start)
        best_funcs.append(results[2])
    np.save('TabuTimes.npy', times)
    np.save('TabuBestFuncs.npy', best_funcs)
    print(np.mean(np.asarray(times)))
    print(np.std(np.asarray(times)))
    print(np.mean(np.asarray(best_funcs)))
    print(np.std(np.asarray(best_funcs)))
