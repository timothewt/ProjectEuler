from decimal import Decimal
from math import floor, sqrt

from tqdm import tqdm


def continued_fraction(N):
    if sqrt(N).is_integer():
        return None

    N_rt = sqrt(N)
    a0 = floor(N_rt)
    m = 0
    d = 1
    a = a0
    sqrt_expansion = [a, []]

    while 2 * a0 != a:
        m = d * a - m
        d = (N - m ** 2) / d
        a = floor((a0 + m) / d)
        sqrt_expansion[1].append(a)

    return sqrt_expansion


res = 0

for i in range(1, 10_000):
    j = continued_fraction(i)
    if j is not None:
        res += len(j[1]) % 2 == 1

print("Result :", res)
