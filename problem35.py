def contains_even(n):
    for i in n:
        if int(i) % 2 == 0:
            break
    else:
        return False
    return True


def is_valid(n):
    num = [i for i in str(n)]
    length = len(num)
    if contains_even(num) or '5' in num:    # if any of the numbers are even it can be at some point divided by 2, same for 5
        if num == ['2'] or num == ['5']:
            return True
        return False
    for i in range(0, length):
        temp = num[length - 1]
        for j in range(length - 1, 0, -1):
            num[j] = num[j - 1]
        num[0] = temp
        if not int(''.join(num)) in primes:
            break
    else:
        return True
    return False


with open("primes.txt") as f:   # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]


count = 0
for i in primes:
    if is_valid(i):
        count += 1

print("There are", count, "circular primes under one million.")