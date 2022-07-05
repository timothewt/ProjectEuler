from math import floor, ceil, gcd
from tqdm import tqdm


max_frac = [2, 5]
max_frac_dec = 2/5

for d in tqdm(range(9, 1_000_000 + 1)):
    for n in range(ceil(3 * d / 7), floor(2 * d / 5) - 1, -1):
        if max_frac_dec < n / d:
            if gcd(n, d) == 1:
                max_frac = [n, d]
                max_frac_dec = n / d
                break

print(max_frac)
