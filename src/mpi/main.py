from math import sqrt
from time import time
import tracemalloc
from mpi4py import MPI

input = {
    "n": 1000,
    "m": 1000,
    "points": [(1,3), (3,2), (6,8), (9,6), (5,5)]
}

mpi_comm = MPI.COMM_WORLD
mpi_size = mpi_comm.Get_size()
mpi_rank = mpi_comm.Get_rank()

def dist(point_x, point_y):
    return sqrt((point_x[0] - point_y[0])**2 + (point_x[1] - point_y[1])**2)

def f():
    rows, cols = input["n"], input["m"]
    points = input["points"]

    nearest_point = []

    rowsLocal = int(rows / mpi_size)
    rowsReg = rowsLocal
    if (mpi_rank == mpi_size - 1):
        rowsLocal += int(rows % mpi_size)

    if (mpi_rank == 0):
        time_start = time()
        tracemalloc.start()

    start_index = mpi_rank * rowsReg
    print(start_index, start_index + rowsLocal)
    for i in range(start_index, start_index + rowsLocal):
        for j in range(cols):
            dist_min = float('inf')
            p_index = 0
            for idx, p in enumerate(points):
                dist_curr = dist((i, j), p)
                if dist_curr < dist_min:
                    dist_min = dist_curr
                    p_index = idx
            nearest_point.append(p_index)

    if (mpi_rank != 0):
        mpi_comm.send(nearest_point, dest=0)

    if (mpi_rank == 0):
        for rank in range(1, mpi_size):
            sub_array = mpi_comm.recv(source=rank)
            nearest_point.append(sub_array)

        time_delta = time() - time_start
        print("Measured time:", time_delta)
        current, peak = tracemalloc.get_traced_memory()
        print(current / 10**6, peak / 10**6)


if __name__ == "__main__":
    f()