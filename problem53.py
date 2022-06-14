from math import factorial


def c(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


count = 0

for i in range(23, 100 + 1):  # the first value is at 23
    for j in range(2, i):  # c(n,1) = c(n,n) = 1 so we don't have to compute them
        count += c(i, j) > 1_000_000

print("Result :", count)
