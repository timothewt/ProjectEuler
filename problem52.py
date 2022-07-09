def compare_digits(n1, n2):
    num1 = [int(x) for x in str(n1)]
    num1.sort()
    num2 = [int(x) for x in str(n2)]
    num2.sort()
    return num1 == num2


for i in range(1, 99):
    for j in range(10 ** (i - 1), (10 ** i) // 6 + 1):
        if compare_digits(j, 2 * j) and compare_digits(2 * j, 3 * j) and compare_digits(3 * j, 4 * j) and compare_digits(4 * j, 5 * j) and compare_digits(5 * j, 6 * j):
            print('Result:', j)
            break
    else:
        continue
    break
