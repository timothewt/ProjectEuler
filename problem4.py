from math import ceil


def get_digit(n, i):
    return n // 10 ** i % 10


def is_palindrome(n):
    # Or :
    # return str(n) == str(n)[::-1]
    is_pal = True
    n_len = len(str(n))
    for i in range(0, ceil(n_len / 2)):
        if get_digit(n, i) != get_digit(n, n_len - i - 1):
            is_pal = False
    return is_pal


largest_pal = 1

for i in range(0, 1000):
    for j in range(0, 1000):
        if i * j > largest_pal:
            if is_palindrome(i * j):
                largest_pal = i * j

print(largest_pal)