from time import time


def factorial(n):
    res = 1
    for k in range(1, n + 1):
        res *= k
    return res


def is_valid(n):
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    if sum == n:
        return True
    else:
        return False


res = 0

for i in range(3, 1000000):     # same result for 10^6 than 10^5, so I assume it's the good one ; start at 3 because 1 and 2 are invalid
    if is_valid(i):
        res += i

print("Result :", res)