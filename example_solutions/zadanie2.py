# Napisz funkcję, która jako argument przyjmuje ciąg znaków. Jako output, zwróci liczbę liter występujących w ciągu więcej niż raz. Kod nie powinien być wrażliwy na wielkość liter. 
# Przykład:
# funkcja(“ABBA”) -> 2 (a i b występują po 2 razy)
# funkcja(“aBcbA”) -> 2 (a i b się powtarza; wielkość liter jest ignorowana)
# funkcja(“RabarbArka”) -> 3 (a,b i r)

from collections import Counter

test1 = 'ABBA'
test2 = 'rabarbarka'

def funkcja(seq):
    return len([letter for letter, occurences in Counter(seq).items() if occurences > 1])


print(funkcja(test1))
print(funkcja(test2))