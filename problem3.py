from math import ceil, sqrt

n = 600851475143
maxPrimeFactor = n

for i in range(2, n):
    if n % i == 0:
        isPrime = True
        for j in range(2, ceil(sqrt(i)) + 1):
            if i % j == 0 and i != j:
                isPrime = False
                print(i, "is a non-prime factor of", n)
                break
        if isPrime:
            print(i, "is a prime factor of", n)
            maxPrimeFactor = i
print("Largest prime factor of", n, ":", maxPrimeFactor)
