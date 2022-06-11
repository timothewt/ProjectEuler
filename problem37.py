with open("primes.txt") as f:  # the primes in the file are all the primes below 1 million
    primes = f.read()
primes = primes.split(",")
primes = [int(i) for i in primes]

def contains_even_except_two(n):
    for i in n:
        if int(i) % 2 == 0 and i != '2':
            break
    else:
        return False
    return True


def is_truncatable(n):
    num = str(n)
    if contains_even_except_two(num) or num in ['2', '3', '5', '7']:    # 2 is prime so we have to let it in
        return False
    temp = num
    for i in range(0, len(num) - 1):
        temp = temp[:-1]
        num = num[1:]
        if not (int(temp) in primes) or not (int(num) in primes):
            break
    else:
        return True
    return False


count = 0
sum = 0
for i in primes:
    if count == 11:
        break
    if is_truncatable(i):
        count += 1
        print(count, i)
        sum += i

print("Sum of all the truncatable prime numbers :", sum)
