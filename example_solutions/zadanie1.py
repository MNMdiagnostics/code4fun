# Mając ciąg znaków x, napisz funkcję, która zwróci dwuelementową listę w której element pierwszy będzie ciąg znaków x z literami na parzystych miejscach zamienionymi na wielkie litery. Drugi element listy będzie miał wielkie litery na miejscach nieparzystych. 
# Przykład:
# fun(“abcdef”) -> [‘aBcDeF’, ‘AbCdEf’]
# Przyjmij, że input do funkcji zawiera tylko litery.


test_chr_1 = 'asalskjh'


def capitalize_even(seq):
    return [''.join([x.upper() if not i%2 else x for i, x in enumerate(seq.lower())]), ''.join([x.upper() if i%2 else x for i, x in enumerate(seq.lower())])]


print(capitalize_even(test_chr_1))