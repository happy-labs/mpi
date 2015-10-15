from random import randint

X = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

N = 500

mtrx1 = [[randint(0, 9) for i in range(N)] for j in range(N)]
mtrx2 = [[randint(0, 9) for i in range(N)] for j in range(N)]

Z = [[0] * N for i in range(N)]

i = 0
for a in mtrx1:
    j = 0
    for b in a:
        k = 0
        for c in mtrx2[j]:
            Z[i][k] = Z[i][k] + (b * c)
            k = k + 1
        j = j + 1
    i = i + 1

print(Z)
