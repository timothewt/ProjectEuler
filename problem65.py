from math import gcd


def reduce_e_continued_rep(iteration):  # values of the continue fraction
    val = generate_expansions_values(iteration)
    n = val[1]
    size = len(n)
    num = 1
    den = n[size - 1]
    for j in range(size - 2, -1, -1):
        temp = num
        num = den
        den = den * n[j] + temp
    num += val[0] * den
    hcf = gcd(num, den)
    num //= hcf
    den //= hcf
    return [num, den]


def generate_expansions_values(n):
    expansion = [2, []]
    for i in range(0, n - 1):
        if (i - 1) % 3 == 0:
            expansion[1].append(((i - 1) // 3 + 1) * 2)
            continue
        expansion[1].append(1)
    return expansion


def digits_sum(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res


N = 100
e = reduce_e_continued_rep(N)

print("The ", N, "th iteration of the continued fraction of e is :\n", e[0], "/", e[1],
      "\nThe sum of the digits of the numerator is ", digits_sum(e[0]), sep='')
