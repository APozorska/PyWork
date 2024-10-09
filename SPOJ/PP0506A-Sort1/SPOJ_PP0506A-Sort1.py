# SPOJ | PP0506A - Sort 1 | https://pl.spoj.com/problems/PP0506A/
# Author: Pozorska Aleksandra
"""
This is a program that sorts a given list of points in a plane by distance from the origin in the Euclidean metric.
Input:
2
3
A 0 0
C 5 5
B 1 -1

1
X 1 1

Output:
A 0 0
B 1 -1
C 5 5

X 1 1
"""

import math
import sys

data = sys.stdin.read().split()
t = int(data[0])
i = 1
result = []
for j in range(t):
    n = int(data[i])
    points = []
    for k in range(n):
        name = data[i+1]
        x = int(data[i+2])
        y = int(data[i+3])
        d = math.sqrt(x ** 2 + y ** 2)
        points.append((name, x, y, d))
        i += 3
    points_sorted = sorted(points, key=lambda x: x[3])
    for name, x, y, d in points_sorted:
        print(name, x, y)
    print()
    i += 1
