from random import randint
import time

X = []
Y = []
Z = []

N = 500


def init_matrix():
    """
    Initialize matrix from here, we do initialize three matrix from here
        1. mtrx1 - input matrix
        2. mtrx2 - input matrix
        3. mtrx3 - output matrix
    """
    global X
    X = [[randint(0, 9) for i in range(N)] for j in range(N)]

    global Y
    Y = [[randint(0, 9) for i in range(N)] for j in range(N)]


def multiply_matrix(X, Y):
    """
    Generate new matrix by multiplying incoming matrix data. Following is the
    algorithm for matrix multiplication

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
    global Z
    Z = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)]
            for X_row in X]


def multiply():
    """
    Multiply matrix via my own algorithm, Following is the algorithm to matrix
    multiplication

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
    Z = [[0] * len(Y[0]) for i in range(len(X))]

    i = 0
    for a in X:
        j = 0
        for b in a:
            k = 0
            for c in Y[j]:
                Z[i][k] = Z[i][k] + (b * c)
                k = k + 1
            j = j + 1
        i = i + 1


if __name__ == '__main__':
    """
    Main method here, we have to do
        1. initialize matrix
        2. Multiply matrix
    """
    init_matrix()

    # start time
    t1 = time.time()

    multiply_matrix(X, Y)

    # end time
    t2 = time.time()

    print('------------------------------------------------------------------')
    print X
    print('------------------------------------------------------------------')
    print('\n')

    print('------------------------------------------------------------------')
    print Y
    print('------------------------------------------------------------------')
    print('\n')

    print('------------------------------------------------------------------')
    print Z
    print('------------------------------------------------------------------')
    print('\n')

    print('------------------------------------------------------------------')
    print('Start time', t1)
    print('------------------------------------------------------------------')
    print('\n')

    print('------------------------------------------------------------------')
    print('End time', t2)
    print('------------------------------------------------------------------')
    print('\n')

    print('------------------------------------------------------------------')
    print('Time taken in seconds', int(t2 - t1))
    print('------------------------------------------------------------------')
    print('\n')
