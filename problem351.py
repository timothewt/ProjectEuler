# diagonals : 6 * (n-1)
# "secondary diagonals" : 6 * floor(1/2 * (n-3))
from math import floor


def count(n):
    return 6 * (floor(n / 2 - 1) + (n - 1))


print(count(10))
print(floor((5 - 3) / 2))

for i in range(0, 10):
    string = ''
    for j in range(0, i):
        string += '  '
    for j in range(0, 10 - i):
        string += 'o   '
    print(string)
print('')
string = ''
for j in range(0, 9):
    string += '  '
string += 'o'
print(string)
