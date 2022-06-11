# Almost same problem as the 72, but the program has to be optimised a lot in order to solve the 72

def hcf(a, b):      # Euclidean algorithm ; a > b > 0
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def is_rpf(num, den):   # is_reduced_proper_fraction
    return hcf(num, den) == 1


def is_even(x):
    return x % 2 == 0

count = 0
incr = 1

for d in range(1, 12000 + 1):
    if is_even(d):
        incr = 2
    for n in range(1, d, incr):
        if is_rpf(n, d):
            if 1/3 < n/d < 1/2:
                count += 1
    incr = 1

print("Number of reduced proper fraction in ]1/3;1/2[ for d <= 12000 :", count)
