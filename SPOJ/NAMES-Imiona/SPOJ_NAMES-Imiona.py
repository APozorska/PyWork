# SPOJ | NAMES - Imiona | https://pl.spoj.com/problems/NAMES/
# Author: Pozorska Aleksandra
"""
This is a program that examines the frequency of names among students.
Input:
1. KowalSki JaCEk
2. mazurkiewicz pIoTR
3. prokoP ANna
4. MisioL annA
5. BerezOwSki jaCEK
6. pietraS ANNA
7. WILkowsKA aneta

Output:
ANNA 3
JACEK 2
ANETA 1
PIOTR 1
"""

dict_names = {}
try:
    while True:
        data = input().split()
        name = data[2].upper()
        if name in dict_names:
            dict_names[name] += 1
        else:
            dict_names[name] = 1
except EOFError:
    pass

names_sorted = sorted(dict_names.items(), key=lambda x: (-x[1], x[0]))

for name, number in names_sorted:
    print(name, number)
