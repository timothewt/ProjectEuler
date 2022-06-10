def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sum_of_digits(n):  # function of problem 16
    num = []
    for i in range(0, len(str(n))):
        num.append(n % 10)
        n //= 10
    return sum(num)


print("Sum of the digits of 10! :", sum_of_digits(factorial(100)))
