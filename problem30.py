def sum_fifth_digits(n):
    num = str(n)
    s = 0
    for k in range(0, len(num)):
        s += int(num[k]) ** 5
    return s


sum = 0

for i in range(2, 10000000):
    if i == sum_fifth_digits(i):
        sum += i

print(sum)  # Sum at 10^7 same as 10^6, so it's probably the result at 10^6
