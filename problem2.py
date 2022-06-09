a = 0
b = 1
c = 1
sum = 0

while c < 4000000:
    temp = b + c
    a = b
    b = c
    c = temp
    if c % 2 == 0:
        sum += c
print(sum)