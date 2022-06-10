def compute_polynomial(coeff, x):    # coeff = [a,b,c] are the coefficient such as P(n) = a*n^2 + b*n + c
    res = coeff[0] * x ** 2 + coeff[1] * x + coeff[2]
    return res


def is_prime(n):
    return n in primes


def consecutive_primes(coeff):
    i = 0
    while compute_polynomial(coeff, i) in primes:
        i += 1
    return i


with open('primes.txt', 'r') as f:
    primes = f.read().split(',')
primes = list(map(int, primes))

print(primes)
print(is_prime(31))
print(consecutive_primes([1, -79, 1601]))
