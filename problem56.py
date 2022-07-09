def digit_sum(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s


maxi = 0

for i in range(1, 100):
    for j in range(1, 100):
        if digit_sum(i ** j) > maxi:
            maxi = digit_sum(i ** j)

print("Result:", maxi)
