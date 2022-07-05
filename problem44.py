# Recursive formula : P(n+1) = P(n) + 3n + 1
from math import sqrt


def gen_pentagonals(n):
    res = [1]
    for i in range(1, n):
        res.append(res[i - 1] + 3 * i + 1)
    return res


def is_pentagonal(n):
    if n < 0:
        return False
    return ((1 + sqrt(1 + 24 * n)) / 6).is_integer()


def is_pair_valid(a, b):
    return is_pentagonal(a + b) and is_pentagonal(a - b)


N = 3000
pentagonals = gen_pentagonals(N)
i = 0

while True:
    for j in range(0, i):
        if is_pair_valid(pentagonals[i], pentagonals[j]):
            print("j =", i + 1, "| k =", j + 1)
            print("D =", pentagonals[i] - pentagonals[j])
            break
    else:
        i += 1
        continue
    break
