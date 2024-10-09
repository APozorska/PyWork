# SPOJ | FR_05_14 - Miasta | https://pl.spoj.com/problems/FR_05_14/
# Author: Pozorska Aleksandra
"""
This is a program that returns the city that is nth-largest in order.
If there are several such cities, the program returns them in alphabetical order
(cities with the same name are treated as two different cities).
If there are no such positions of the cities, the program returns "BRAK".
Input:
5
DZIALDOWO 21000
TORUN 210000
WARSZAWA 1700000
OLSZTYN 170000
BAJTOCJA 21000
3
1
4
5
Output:
WARSZAWA
BAJTOCJA DZIALDOWO
BRAK
"""


import sys

data = sys.stdin.read().split()
n = int(data[0])

dict_cities = {}
i = 1
while i < 2 * n:
    city = data[i]
    population = int(data[i + 1])
    if population in dict_cities:
        dict_cities[population] += [city]
    else:
        dict_cities[population] = [city]
    i += 2

dict_cities = sorted(dict_cities.items(), key=lambda x: x[0], reverse=True)

q = int(data[i])
i += 1
for j in range(1, q + 1):
    position = int(data[i])
    i += 1
    if position > len(dict_cities):
        print("BRAK")
    else:
        result = sorted(dict_cities[position - 1][1])
        print(' '.join(result))
