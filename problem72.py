from time import time


with open("primes.txt") as f:  # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]

def prime_factors(n):
    res = []
    while n != 1:
        for p in primes:
            x = n % p
            if x == 0:
                n = n // p
                res.append(p)
                break
    return res


def euler_totient(n, pf):   # up to which numbers, prime factors
    res = n
    for i in pf:
        n *= 1 - 1/i
    return res

count = 0

start = time()

for d in range(2, 1000 + 1):
    pf = list[set(prime_factors(d))]
    for i in range(1, d):
        count += euler_totient(d, pf)

print(time() - start)

print("Number of reduced proper fraction for d <= 10^7 :", count)
