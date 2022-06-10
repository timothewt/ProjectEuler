hex_numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def decimal_to_hex(n):  # up to base 16
    res = ""
    current = n
    while current > 0:
        new_digit = current % 16
        res = hex_numerals[new_digit] + res
        current //= 16
    return res


def hex_to_decimal(n):
    res = 0
    for i in range(0, len(n)):
        res += hex_numerals.index(n[i]) * (16 ** (len(n) - i - 1))
    return res


def decimal_factorial(n):
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


def f(N):
    fact_N = clean_16_factorial(N)
    f_N_hex = decimal_to_hex(fact_N)
    f_N_hex_clean = f_N_hex

    f_N_hex_clean = clear_end_zeros(f_N_hex_clean)

    return f_N_hex_clean[-12:]


N = 20
print("Last twelve digits of f("+str(N)+") without trailing zeros :", f(decimal_factorial(N)))  # can't go above 8, too much calculations
