def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_ways(size):
    return factorial(2 * size) // (factorial(size) ** 2)


print("Number of ways :", number_of_ways(20))
