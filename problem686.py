from math import log10, ceil, log


def num_length(num):
    return ceil(log10(num))


def first_digits(n, num):    # n number of digits
    length = num_length(num)
    return (num - (num % 10 ** (length - n))) // 10 ** (length - n)


def is_valid(n, p):
    return l123 <= p * l2 - num_length(n) - 1 < l124


l2 = log(2)
l123 = log(1.23)
l124 = log(1.24)
count = 0
power = 1
x = 2

while count < 678910:
    x *= 2
    power += 1
    if is_valid(x, power):
        count += 1

print("Result :", power)
