from sympy import isprime


with open("primes.txt") as f:  # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]

max_sum_length = 0
res = 2

for i in range(0, len(primes) - 1):
    sum = 0
    l = 0
    p = 0
    for j in range(i, len(primes) - 1):
        if sum > 1_000_000:
            break
        sum += primes[j]
        if isprime(sum):
            l = j - i + 1
            p = sum
    if l > max_sum_length:
        res = p
        max_sum_length = l

print("Prime below one-million that can be written as the sum of the most consecutive primes :", res, "\
        ,which is the sum of", max_sum_length, "primes.")
