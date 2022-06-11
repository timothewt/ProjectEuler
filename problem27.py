def compute_polynomial(coeff, x):    # coeff = [a,b] are the coefficient such as P(n) = n^2 + a*n + b
    res = x ** 2 + coeff[0] * x + coeff[1]
    return res


def is_prime(n):
    return n in primes


def consecutive_primes(coeff):
    i = 0
    while compute_polynomial(coeff, i) in primes:
        i += 1
    return i


with open('primes.txt', 'r') as f:
    primes = f.read().split(',')
primes = list(map(int, primes))


max_length = 0
max_coeff = [0, 0]

possible_b = []     # b has to be prime otherwise P(0) = b is not prime
flag = False
i = 0
while not flag:
    if primes[i] <= 1000:
        possible_b.append(primes[i])
        possible_b.append(primes[i] * -1)
        i += 1
    else:
        flag = True

for a in range(-999, 1000, 2):  # a has to be odd otherwise P(1) = 1 + a + b is even so not prime, as b is prime therefore odd
    for b in possible_b:
        x = consecutive_primes([a, b])
        if x > max_length:
            max_length = x
            max_coeff = [a, b]

print("The polynomial has the longest chain for P(n)=n^2" + str(max_coeff[0]) + "n" + "+" + str(max_coeff[1]))
print("The product of the coefficients is", max_coeff[0] * max_coeff[1])
