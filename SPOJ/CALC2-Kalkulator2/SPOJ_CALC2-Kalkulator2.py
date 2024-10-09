# SPOJ | CALC2 - Kalkulator2 | https://pl.spoj.com/problems/CALC2/
# Author: Pozorska Aleksandra
"""
This is a program that acts as a simple calculator with memory that supports five operations:
addition, subtraction, multiplication, division, and integer division.
The calculator has 10 registers in memory, numbered 0 - 9. All registers contain leading zeros.
Input:
z 3 6
z 1 89
z 2 60
z 0 11
+ 0 1
- 1 2
* 2 3
/ 3 0
% 3 1
Output:
100
29
360
0
6
"""

result = ['0'] * 10


def calculate(symbol, a, b):
    if symbol == "z":
        result[int(a)] = b
    else:
        print(int(eval(result[int(a)] + symbol + result[int(b)])))


while True:
    try:
        symbol, a, b = input().split()
        calculate(symbol, a, b)
    except EOFError:
        break
