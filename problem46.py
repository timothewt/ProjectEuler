from sympy import isprime

with open("primes1.txt") as f:   # the primes in the file are all the primes below 1 million
    primes = f.read()

primes = [int(i) for i in primes.split()]


def is_valid(num):
    if isprime(num) or num % 2 == 0:
        return True
    p_i = 0
    sq = 1
    while primes[p_i] + 2 * (sq ** 2) <= num:
        while primes[p_i] + 2 * (sq ** 2) <= num:
            if primes[p_i] + 2 * (sq ** 2) == num:
                return True
            sq += 1
        p_i += 1
        sq = 1
    return False


n = 4

while True:
    if not is_valid(n):
        print("Result :", n)
        break
    n += 1
