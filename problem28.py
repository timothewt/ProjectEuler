sum = 1
size = 1
reason = 2
current = 1

while size < 1001:
    for i in range(0, 4):   # each corner of the square
        current += reason
        print(current)
        sum += current
    size += 2
    reason += 2

print(sum)
