from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
workers = comm.Get_size() - 1

mtrx1 = []
mtrx2 = []
mtrx3 = []

N = 500


def init_matrix():
    """
    Initialize matrxi from here, we do initialize three matrx from here
        1. mtrx1 - input matrix
        2. mtrx2 - input matrix
        3. mtrx3 - output matrix
    """
    global mtrx1
    mtrx1 = [
        [1, 2, 3, 4, 5, 6, 9],
        [5, 6, 7, 8, 4, 3, 5],
        [9, 10, 11, 12, 3, 2, 2],
    ]

    global mtrx2
    mtrx2 = [
        [1, 2, 3],
        [5, 6, 7],
        [2, 2, 7],
        [5, 6, 9],
        [5, 6, 9],
        [5, 6, 9],
        [5, 6, 9],
    ]

    global mtrx3
    mtrx3 = [0] * len(mtrx1)


def calculate_matrix_row(X, Y):
    """
    Generate single row of final matrix. This funcaiont will be called by
    each and every slave with their matrix data. For an example

    x = [
            [1, 2, 3, 4],
            [3, 2, 3, 7],
        ]

    y = [
            [1, 2, 3],
            [5, 6, 7],
            [2, 2, 7],
            [5, 6, 9],
        ]

    z = [
            [(1*1 + 2*5 + 3*2 + 4*5), (1*2 + 2*6 + 3*2 + 4*6), --, --],
            [(3*1 + 2*5 + 3*2 + 7*5), (3*2 + 2*6 + 3*2 + 7*6), --, --]
        ]

    Args:
        x: mtrx1
        y: mtrx2

    Returns:
        z: calculated matrix part
    """
    Z = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
            for X_row in X]

    return Z


def distribute_matrix_data():
    """
    Distribute row of first matrix and whole second matrix to salves, this done
    via master node. Then salves caculate single row of final matrix and send
    result back to master
    """
    # split matrix according to workers count
    n = max(1, workers)
    l = [mtrx1[i:i + n] for i in range(0, len(mtrx1), n)]

    print(l)

    pid = 1
    for row in l:
        comm.send(row, dest=pid, tag=1)
        comm.send(mtrx2, dest=pid, tag=2)
        pid = pid + 1


def assemble_matrix_data():
    """
    Assemble returing valus form salves and generate final matrix. Slaves
    calculate single row of final matrix
    """
    pid = 1
    l = []
    for n in range(workers):
        row = comm.recv(source=pid, tag=pid)
        l = l + row
        #mtrx3[pid - 1] = row
        print('master', rank, row)
        pid = pid + 1

    print(l)


def master_operation():
    """
    Do operation of master node, we have to do following this from here
        1. distribute matrix data to slaves
        2. assemble salves returing valus and generate final matrix
    """
    distribute_matrix_data()
    assemble_matrix_data()
    print(mtrx3)


def slave_operation():
    """
    Do operation of slave nodes, we have to do
        1. Gather the data sending from master
        2. Calculate the single fow of final matrix
        3. Send the calcuated row back to master
    """
    # receive data from master node
    x = comm.recv(source=0, tag=1)
    y = comm.recv(source=0, tag=2)

    # calculate single matrx row and send it back to master
    z = calculate_matrix_row(x, y)
    comm.send(z, dest=0, tag=rank)


if __name__ == '__main__':
    """
    Main method here, we have to do
        1. initilize matrxies
        2. Master/Salve operations
    """
    init_matrix()
    if rank == 0:
        master_operation()
    else:
        slave_operation()
