from math import ceil, sqrt

prime_sum = 0

for i in range(2, 2000001):
    print(i)
    is_prime = True
    for j in range(2, ceil(sqrt(i)) + 1):
        if i % j == 0 and i != j:
            is_prime = False
            break
    if is_prime:
        prime_sum += i

print("Sum of primes below two millions :", prime_sum)