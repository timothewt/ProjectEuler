sum = 0
for i in range(0, 1000):
    if (i % 5 == 0) | (i % 3 == 0):
        sum += i
print(sum)