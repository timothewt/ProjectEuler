# diagonals : 6 * (n-1)
# "secondary diagonals" : 6 * floor(1/2 * (n-3))
from math import floor


def count(n):
    return 6 * (floor(n / 2 - 1) + (n - 1))


print(count(10))
print(floor((5 - 3) / 2))
