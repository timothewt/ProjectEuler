with open("primes.txt") as f:  # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]


def prime_factors(n):
    if n in primes:
        return [n]
    res = []
    while n != 1:
        for p in primes:
            x = n % p
            if x == 0:
                n = n // p
                res.append(p)
                break
    return res


def euler_totient(pf):  # up to which numbers, prime factors
    res = 1
    for i in set(pf):
        res *= i ** (pf.count(i) - 1) * (i - 1)
    return res

# The result n/phi(n) will be the largest if n is a product of primes
N = 10 ** 7
res = 1
i = 0

while res * primes[i + 1] < N:
    res *= primes[i]
    i += 1

print("Optimal n :", res)
