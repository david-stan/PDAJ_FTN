from asyncio.trsock import TransportSocket
from math import sqrt
from time import time
import tracemalloc

input = {
    "n": 1000,
    "m": 1000,
    "points": [(1,3), (3,2), (6,8), (9,6), (5,5)]
}

def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def matrix_gen():
    rows, cols = input["n"], input["m"]

    for i in range(rows):
        for j in range(cols):
            yield i, j

def matrix_calc(matrix_gen, points):
    for i, j in matrix_gen:
        dist_min = float('inf')
        p_index = 0
        for idx, p in enumerate(points):
            dist_curr = dist((i, j), p)
            if dist_curr < dist_min:
                dist_min = dist_curr
                p_index = idx
        yield p_index

nearest_point = []
def matrix_store(idx_gen):
    for i in idx_gen:
        nearest_point.append(i)


if __name__ == "__main__":
    time_start = time()
    tracemalloc.start()
    matrix = matrix_gen()
    points = input["points"]
    ids = matrix_calc(matrix, points)
    
    
    
    current, peak = tracemalloc.get_traced_memory()
    matrix_store(ids)
    time_delta = time() - time_start
    print(time_delta)
    print(current / 10**6, peak / 10**6)
    # print(nearest_point)