from math import ceil, sqrt

n = 0
prime_count = 0

while prime_count < 10001:
    n += 1
    is_prime = n != 1
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0 and n != i:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print("10001st prime :", n)