from concurrent.futures import process
from math import sqrt
from time import time
from multiprocessing import cpu_count, Pool

input = {
    "n": 1000,
    "m": 1000,
    "points": [(1,3), (3,2), (6,8), (9,6), (5,5)]
}

def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def matrix_gen():
    rows, cols = input["n"], input["m"]
    points = input["points"]

    for i in range(rows):
        for j in range(cols):
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


def matrix_calc():
    with Pool(processes=16) as pool:
        yield from pool.map(
            _worker,
            matrix_gen(),
        )

nearest_point = []

def matrix_store(matrix):
    for i in matrix:
        nearest_point.append(i)

if __name__ == "__main__":
    s = time()
    nums = matrix_calc()
    matrix_store(nums)
    delta = time() - s
    print("Measured time:", delta)
    print(nearest_point[:100])