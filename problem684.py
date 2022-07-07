# PROBLEM 684
# pattern --> always X99...9 depending on the multiple of ten we're at
# starting number of the solution is the tens unit, and the number of 9 is tens times 9 + 1
from tqdm import tqdm


def fibonacci(n):  # n >= 2
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i - 2] + f[i - 1])
    return f


def s(n):
    power = n // 9          # deduced by random values, it works
    left_digit = n % 9
    return (left_digit + 1) * (10 ** power) - 1


def S(n):
    result = 0
    for i in range(1, n + 1):
        result += s(i)
    return result


fib = fibonacci(90)
res = 0

for j in tqdm(fib):
    res += S(j)
    res %= 1_000_000_007

print(res)
