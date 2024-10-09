# SPOJ | TRN - Transponowanie macierzy | https://pl.spoj.com/problems/TRN/
# Author: Pozorska Aleksandra
"""
This is the program that transposes a given matrix.
Input:
4 3
1 2 5
4 3 3
3 4 9
8 7 7
Output:
1 4 3 8
2 3 4 7
5 3 9 7
"""

m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = input().split()
    matrix.append(row)

transposed = list(zip(*matrix))
for i in range(n):
    print(' '.join(transposed[i]))
