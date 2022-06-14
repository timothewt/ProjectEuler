from math import floor, sqrt, gcd


def is_valid(d, x, y):
    return x ** 2 - d * (y ** 2) == 1


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


def get_expansion_iterations(N, k):  # N being the number under the square root and k>=1 the number of iterations
    expansion = continued_fraction(N)
    period = len(expansion[1])
    result = [expansion[0], []]
    for i in range(0, k - 1):
        result[1].append(expansion[1][i % period])
    return result


def reduce_fraction(val):  # values of the continue fraction
    n = val[1]
    if not n:
        return [val[0], 1]
    size = len(n)
    num = 1
    den = n[size - 1]
    for i in range(size - 2, -1, -1):
        temp = num
        num = den
        den = den * n[i] + temp
    num += val[0] * den
    hcf = gcd(num, den)
    num //= hcf
    den //= hcf
    return [num, den]


continued_fractions = []

for D in range(1, 1000 + 1):
    continued_fractions.append(continued_fraction(D))

max_sol = [0, 0]
max_d = 0

for D in range(1, 1000 + 1):
    s = [0, 0]
    if continued_fractions[D - 1] is not None:
        iteration = 1
        while not is_valid(D, s[0], s[1]):
            s = reduce_fraction(get_expansion_iterations(D, iteration))
            iteration += 1
        print("Solution for x²-", D, "y²=1 : (x,y)=(", s[0], ",", s[1], ")", sep='')
    if s[0] > max_sol[0]:
        max_sol = s
        max_d = D

print("The highest solution for x is found for D = ", max_d, ", and ", max_sol[0], "²-", max_d, "*", max_sol[1], "² = 1"
      , sep='')
