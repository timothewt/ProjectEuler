# Let Se(d) be the sum of all near power sums of exactly d digits. We see that S(d) = Se(d) + S(d)
from tqdm import tqdm


def sum_digits(n, k):
    s = 0
    for i in str(n):
        s += int(i) ** k
    return s

def is_valid(n):
    s = 0
    if max([int(i) for i in str(n - 1)]) != 1:
        k = 1
        while s < n:
            s = sum_digits(n - 1, k)
            k += 1
        if n == s:
            return True
    s = 0
    if max([int(i) for i in str(n + 1)]) != 1:
        k = 1
        while s < n:
            s = sum_digits(n + 1, k)
            k += 1
        if n == s:
            return True
    return False

sum = 0
d = 6
for i in tqdm(range(2, 10 ** d)):
    if is_valid(i):
        sum += i

print(sum)
