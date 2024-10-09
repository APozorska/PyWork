# SPOJ | FR_03_20 - T9 | https://pl.spoj.com/problems/FR_03_20/
# Author: Pozorska Aleksandra
"""
This is a program that checks whether a given word could have been created from a given combination of digits using the T9 dictionary.
Input:
3

FraKtal 3725825

BlednaKomBinacjA123 2533625662462252122

NIE 643



Output:
TAK – FraKtal

NIE

TAK - NIE
"""

table_mapping = {
    'a': '2', 'b': '2', 'c': '2',
    'd': '3', 'e': '3', 'f': '3',
    'g': '4', 'h': '4', 'i': '4',
    'j': '5', 'k': '5', 'l': '5',
    'm': '6', 'n': '6', 'o': '6',
    'p': '7', 'q': '7', 'r': '7', 's': '7',
    't': '8', 'u': '8', 'v': '8',
    'w': '9', 'x': '9', 'y': '9', 'z': '9',
    '1': '1', '2': '2', '3': '3',
    '4': '4', '5': '5', '6': '6',
    '7': '7', '8': '8', '9': '9',
    '0': '0', "#": "#", "*": "*"
}


def check_word_letters_combination(word, numbers):
    word_lower = word.lower()
    generated_numbers = ""
    for char in word_lower:
        generated_numbers += table_mapping[char]
    if generated_numbers != numbers:
        return f"NIE \n"
    else:
        return f"TAK - {word} \n"


n = int(input())
for j in range(n):
    line = input()
    while not line:
        line = input()
    word, numbers = line.split()
    print(check_word_letters_combination(word, numbers))

