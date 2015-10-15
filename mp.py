from mpi4py import MPI
from random import randint

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
workers = comm.Get_size() - 1

mtrx1 = []
mtrx2 = []
mtrx3 = []

N = 5


def init_matrix():
    """
    Initialize matrxi from here, we do initialize three matrx from here
        1. mtrx1 - input matrix
        2. mtrx2 - input matrix
        3. mtrx3 - output matrix
    """
    global mtrx1
    mtrx1 = [[randint(0, 9) for i in range(N)] for j in range(N)]

    global mtrx2
    mtrx2 = [[randint(0, 9) for i in range(N)] for j in range(N)]


def multiply_matrix(X, Y):
    """
    Generate new matrix by multiplying incoming matrix data.
    This funcaiont will be called by each and every slave with their matrix
    data. For an example

    X = [
            [1, 2, 3, 4],
            [3, 2, 3, 7],
        ]

    Y = [
            [1, 2, 3],
            [5, 6, 7],
            [2, 2, 7],
            [5, 6, 9],
        ]

    Z = [
            [(1*1 + 2*5 + 3*2 + 4*5), (1*2 + 2*6 + 3*2 + 4*6), --, --],
            [(3*1 + 2*5 + 3*2 + 7*5), (3*2 + 2*6 + 3*2 + 7*6), --, --]
        ]

    Args:
        X: rows of mtrx1
        Y: whole mtrx2

    Returns:
        Z: calculated matrix part
    """
    Z = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
            for X_row in X]

    return Z


def distribute_matrix_data():
    """
    Distribute rows of first matrix and whole second matrix to salves, this
    done via master node. Then salves caculate a sub matrix by multiplying
    incoming matrix and send result back to master
    """
    # split matrix according to workers count
    n = max(1, workers)
    rows = [mtrx1[i:i + n] for i in range(0, len(mtrx1), n)]

    # this means matrix devided to un equal parts
    # we have to deistribute unequl part to master node, master node will do
    # multiplicaiton on it
    if len(mtrx1) % workers != 0:
        comm.send(rows[-1], dest=0, tag=1)
        comm.send(mtrx2, dest=0, tag=2)
        del rows[-1]

    pid = 1
    for row in rows:
        comm.send(row, dest=pid, tag=11)
        comm.send(mtrx2, dest=pid, tag=22)
        pid = pid + 1


def assemble_matrix_data():
    """
    Assemble returing valus form salves and generate final matrix. Slaves
    calculate single rows of final matrix
    """
    global mtrx3

    pid = 1
    for n in range(workers):
        row = comm.recv(source=pid, tag=pid)
        mtrx3 = mtrx3 + row
        pid = pid + 1

    # this means matrix devided to un equal parts
    # master node also doing some operation here
    if len(mtrx1) % workers != 0:
        row = comm.recv(source=0, tag=0)
        mtrx3 = mtrx3 + row

    print(mtrx3)


init_matrix()
if rank == 0:
    distribute_matrix_data()

    # this means matrix devided to un equal parts
    # in here we have to do some calculation in master node as well
    if len(mtrx1) % workers != 0:
        x = comm.recv(source=0, tag=1)
        y = comm.recv(source=0, tag=2)

        # calculate matrx rows and send it back to master
        z = multiply_matrix(x, y)
        comm.send(z, dest=0, tag=0)

    assemble_matrix_data()
else:
    # receive data from master node
    x = comm.recv(source=0, tag=11)
    y = comm.recv(source=0, tag=21)

    # calculate matrx rows and send it back to master
    z = multiply_matrix(x, y)
    comm.send(z, dest=0, tag=rank)
