from math import sqrt

D = 1000

x = []


for d in range(2, D + 1):
    if not sqrt(d).is_integer():
        y = 1
        x_ = sqrt(1 + d * y ** 2)
        while not x_.is_integer():
            y += 1
            x_ = sqrt(1 + d * y ** 2)
        x.append([x_, y])

print(x)
