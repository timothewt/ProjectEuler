a = 0
b = 1

i = 1

min_length = 1000

while len(str(b)) < min_length:
    i += 1
    new_elem = a + b
    a = b
    b = new_elem

print("Index of the first number in Fibonacci which length is above", min_length, ":", i)
