from concurrent.futures import process
from math import sqrt
from time import time
from multiprocessing import cpu_count, Pool
import tracemalloc


def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def matrix_gen(nrows, ncols, points):
    for i in range(nrows):
        for j in range(ncols):
            yield i, j, points

def _worker(args):
    i, j, points = args
    dist_min = float('inf')
    p_index = 0
    for idx, p in enumerate(points):
        dist_curr = dist((i, j), p)
        if dist_curr < dist_min:
            dist_min = dist_curr
            p_index = idx
    return p_index


def matrix_calc(nrows, ncols, points):
    with Pool(processes=8) as pool:
        yield from pool.map(
            _worker,
            matrix_gen(nrows, ncols, points),
        )

nearest_points = []

def matrix_store(matrix):
    for i in matrix:
        nearest_points.append(i)

def calculate(parameters):
    nrows, ncols, points = parameters["n"], parameters["m"], parameters["points"]

    tracemalloc.start()
    s = time()
    nums = matrix_calc(nrows, ncols, points)
    matrix_store(nums)
    delta = time() - s
    
    current, peak = tracemalloc.get_traced_memory()
    
    

    ret = {
        # "result": nearest_points,
        "time_in_s": delta,
        "max_memory_in_MB": peak / 10**6
    }
    return ret