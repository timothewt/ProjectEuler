def next_iteration(n):  # n = [num, den]
    return [2 * n[1] + n[0], n[0] + n[1]]


def is_valid(n):        # is valid if there are more digits in the numerator than the denominator
    return len(str(n[0])) > len(str(n[1]))


count = 0
x = [1, 1]

for i in range(0, 1000):
    x = next_iteration(x)
    count += is_valid(x)

print("Result :", count)
