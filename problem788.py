from math import factorial


def nCk(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def d(N):
    same_digits = N // 2 + 1
    representations = nCk(N, same_digits)   # * 9 for every dominant digit in |[1, 9]|
    start_by_0 = nCk(N - 1, N - same_digits - 1)
    a = 10 ** (N - same_digits) - 1
    result = (representations * a - start_by_0) * 9
    result += start_by_0 * a
    result += 1     # only the same digit each time
    print(N, a, result)
    return result


def D(N):
    if N == 2:
        return 19   # 0 - 9 and 11, 22, ..., 99
    else:
        return d(N) + D(N - 1)


print(D(4))
