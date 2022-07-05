with open("primes1.txt") as f:   # the primes in the file are all the primes below 1 million
    primes = f.read()

primes = primes.split()
primes = [int(i) for i in primes]


def count_distinct_factors(n):
    decomp = prime_decomposition(n)
    return len(list(set(decomp)))


def prime_decomposition(n):
    decomposition = []
    i = 0
    while n != 1:
        while True:
            if n % primes[i] == 0:
                n = n / primes[i]
                decomposition.append(primes[i])
                break
            i += 1
    return decomposition


n = 2
consecutive = 0

while consecutive != 4:
    if count_distinct_factors(n) == 4:
        consecutive += 1
    else:
        consecutive = 0
    n += 1

print("Result :", n - 4)
