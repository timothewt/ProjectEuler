def generate_primes(n):  # generates a list of n primes
    primes = []
    i = 2
    while len(primes) < n:
        for j in range(2, i):
            if i % j == 0:
                break
            continue
        else:
            primes.append(str(i))
        i += 1
    return primes


primes_list = ','.join(generate_primes(20000))


with open('primes.txt', 'w') as f:
    f.write(primes_list)
