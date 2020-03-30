# Mając ciąg znaków x, napisz funkcję, która zwróci dwuelementową listę w której element pierwszy będzie ciąg znaków x z literami na parzystych miejscach zamienionymi na wielkie litery. Drugi element listy będzie miał wielkie litery na miejscach nieparzystych. 
# Przykład:
# fun(“abcdef”) -> [‘aBcDeF’, ‘AbCdEf’]
# Przyjmij, że input do funkcji zawiera tylko litery.

import argparse

test_sequence = 'asalskjh'


def funky_capitalize(seq):
    return [''.join([x.upper() if not i % 2 else x for i, x in enumerate(seq.lower())]), ''.join([x.upper() if i % 2 else x for i, x in enumerate(seq.lower())])]


print(funky_capitalize(test_sequence))