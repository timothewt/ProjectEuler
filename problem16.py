def sum_of_digits(n):
    num = []
    for i in range(0, len(str(n))):
        num.append(n % 10)
        n //= 10
    return sum(num)


N = 2 ** 1000
print("Sum of the digits of", N, ":", sum_of_digits(N))
