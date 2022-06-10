from math import floor, sqrt, ceil


def get_divisors(n):
    divisors = []
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            if i == sqrt(n) or i == 1:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n / i))
    return divisors


def get_number_type(n):
    divisors = get_divisors(n)
    divisors_sum = sum(divisors)
    if divisors_sum == n:
        return 'perfect'
    elif divisors_sum < n:
        return 'deficient'
    else:
        return 'abundant'


abundant_numbers = []

for i in range(1, 28124):
    if get_number_type(i) == 'abundant':
        abundant_numbers.append(i)

res = (28124 * 28123) // 2  # we start with the sum of all the integers in |[1,28123]| and subtract every sum of 2 abundant numbers from it

for i in range(1, 28124):
    possible_abundant_top = ([n for n in abundant_numbers if i > n >= ceil(i/2)])   # we only need to take the abundant numbers below the current number and
    possible_abundant_bottom = ([n for n in abundant_numbers if n <= ceil(i/2)])
    for j in possible_abundant_bottom:
        for k in possible_abundant_top:
            if j + k == i:
                res -= i
                break
        else:
            continue
        break

# this is the worst way to solve this problem, the best one is to generate all the possible sums of two abundant numbers and subtract the sum of them to the sum 'res' above

print("Result:", res)
