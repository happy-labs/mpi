X = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]


Y = [
    [1, 2, 3],
    [5, 6, 7],
    [2, 2, 7],
    [5, 6, 9],
]

Z = [[0] * len(Y[0]) for i in range(len(X))]

print(Z)

i = 0
for a in X:
    j = 0
    for b in a:
        k = 0
        for c in Y[j]:
            Z[i][k] = Z[i][k] + (b * c)
            print(b, c, i, k)
            k = k + 1
        j = j + 1
    i = i + 1

print(Z)
