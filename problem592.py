def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def clean_16_factorial(n):  # clean <=> removes the 0 at the end of the hex
    res = 1
    for i in range(1, n + 1):
        res *= i
        while res % 16 == 0:
            res //= 16
    return res


def shift_str_right(string, n):  # n being the number of times the string is shifted to the right
    res = string
    for i in range(0, n):
        string_list = list(res)
        for i in range(len(string_list) - 1, 0, -1):
            string_list[i] = string_list[i - 1]
        string_list[0] = ''
        res = ''.join(string_list)
    return res


def clear_end_zeros(n):
    while n[len(n) - 1] == '0' and not len(n) == 0:
        n = shift_str_right(n, 1)
    return n


def to_base_n(number, n):  # up to base 16
    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    res = ""
    current = number
    while current > 0:
        new_digit = current % n
        res = numerals[new_digit] + res
        current //= n
    return res


def f(N):
    fact_N = clean_16_factorial(N)
    f_N_hex = to_base_n(fact_N, 16)
    f_N_hex_clean = f_N_hex

    f_N_hex_clean = clear_end_zeros(f_N_hex_clean)

    return f_N_hex_clean[-12:]


N = 20
print("Last twelve digits of f("+str(N)+") without trailing zeros :", f(factorial(8)))  # can't go above 8, too much calculations
