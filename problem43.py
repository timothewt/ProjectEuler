from itertools import permutations


def get_digit(n, i):
    return (n // (10 ** (10 - i))) % 10


def is_valid(n):    # input is an integer
    digits = [get_digit(n, i) for i in range(1, 10 + 1)]
    if (digits[7] * 100 + digits[8] * 10 + digits[9]) % 17 != 0:
        return False
    if (digits[6] * 100 + digits[7] * 10 + digits[8]) % 13 != 0:
        return False
    if (digits[5] * 100 + digits[6] * 10 + digits[7]) % 11 != 0:
        return False
    if (digits[4] * 100 + digits[5] * 10 + digits[6]) % 7 != 0:
        return False
    if (digits[3] * 100 + digits[4] * 10 + digits[5]) % 5 != 0:
        return False
    if (digits[2] * 100 + digits[3] * 10 + digits[4]) % 3 != 0:
        return False
    if (digits[1] * 100 + digits[2] * 10 + digits[3]) % 2 != 0:
        return False
    return True


numbers = [int(''.join(i)) for i in permutations('0123456789') if i[0] != '0']
sum = 0

for num in numbers:
    if is_valid(num):
        sum += num

print('Result:', sum)
