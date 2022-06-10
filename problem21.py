from math import floor, sqrt


def get_divisors(n):
    divisors = []
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            if i == sqrt(n) or i == 1:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n // i)
    return divisors


def d(n):
    return sum(get_divisors(n))


def are_amicable(a, b):
    return d(a) == b and d(b) == a and a != b  # therefore we can find two amicable number is we find one that gives d(d(n)) == n


def sum_amicable():
    sum = 0
    for i in range(1, 10001):
        if d(d(i)) == i:
            if d(i) != i and d(i) < 10000:
                sum += d(i) + i
    return sum // 2     # divided by two because we got each pair of amicable numbers 2 times


print("Sum of all amicable numbers under 10000 :", sum_amicable())
