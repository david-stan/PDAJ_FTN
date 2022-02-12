from math import sqrt
from time import time
import tracemalloc

def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def calculate(parameters):
    nrows, ncols, points = parameters["n"], parameters["m"], parameters["points"]

    nearest_points = []

    tracemalloc.start()
    time_start = time()
    for i in range(nrows):
        for j in range(ncols):
            dist_min = float('inf')
            p_index = 0
            for idx, p in enumerate(points):
                dist_curr = dist((i, j), p)
                if dist_curr < dist_min:
                    dist_min = dist_curr
                    p_index = idx
            nearest_points.append(p_index)
    time_delta = time() - time_start
    current, peak = tracemalloc.get_traced_memory()

    ret = {
        # "result": nearest_points,
        "time_in_s": time_delta,
        "max_memory_in_MB": peak / 10**6
    }
    return ret