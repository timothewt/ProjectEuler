def dec_to_bin(n):  # decimal to binary
    res = ''
    while n > 0:
        new_digit = n % 2
        n //= 2
        res = str(new_digit) + res
    return res


def is_palindromic(str):
    for i in range(0, len(str) // 2):
        if str[i] != str[len(str) - 1 - i]:
            break
    else:
        return True
    return False

sum = 0

for i in range(1, 1_000_000, 2):  # only odd numbers because in binary there will be trailing zeros, so they are not palindromic as the description says it
    if is_palindromic(str(i)):
        if is_palindromic(dec_to_bin(i)):
            sum += i

print("The sum of all palindromic numbers in base 10 and 2 under one million is", sum)
