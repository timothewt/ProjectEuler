from itertools import permutations
from sympy import isprime


def gen_pandigitals(n):
    return [int(''.join(i)) for i in permutations(''.join([str(i) for i in range(1, n + 1)]))]


for i in range(9, 0, -1):
    pans = gen_pandigitals(i)
    pans.sort(reverse=True)
    for n in pans:
        if isprime(n):
            print('Largest n-digit prime: ', n, ' which is ', i, '-digit pandigital.', sep='')
            break
    else:
        continue
    break
