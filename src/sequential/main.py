from math import sqrt
from time import time

input = {
    "n": 2000,
    "m": 2000,
    "points": [(1,3), (3,2), (6,8), (9,6), (5,5)]
}

def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def f():
    rows, cols = input["n"], input["m"]
    points = input["points"]

    nearest_point = []

    time_start = time()
    for i in range(rows):
        for j in range(cols):
            dist_min = float('inf')
            p_index = 0
            for idx, p in enumerate(points):
                dist_curr = dist((i, j), p)
                if dist_curr < dist_min:
                    dist_min = dist_curr
                    p_index = idx
            nearest_point.append(p_index)
    time_delta = time() - time_start

    # print(nearest_point)
    print(time_delta)


if __name__ == "__main__":
    f()