# we can re-use the program of the problem 28 to know each number of the diagonals

with open("primes.txt") as f:  # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]
# we can re-use the program of the problem 28 to know each number of the diagonals
from sympy import isprime   # after 50 problems I discovered this wonderful function that reduces the time of
# execution by at least 10^4

primes_count = 0
count = 1
size = 1
reason = 2
current = 1

while primes_count / count > .1 or primes_count == 0:
    for i in range(0, 4):   # each corner of the square
        current += reason
        count += 1
        if isprime(current):
            primes_count += 1
    size += 2
    reason += 2

print("Result :", size)
