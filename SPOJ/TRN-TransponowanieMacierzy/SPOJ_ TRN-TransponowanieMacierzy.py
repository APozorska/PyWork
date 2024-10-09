# SPOJ | TRN - Transponowanie macierzy | https://pl.spoj.com/problems/TRN/
# Author: Pozorska Aleksandra

m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = input().split()
    matrix.append(row)

transposed = list(zip(*matrix))
for i in range(n):
    print(' '.join(transposed[i]))
