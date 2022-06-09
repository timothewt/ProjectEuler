res = 21
is_found = False
while not is_found:
    is_found = True
    for i in range(1, 21):
        if res % i != 0:
            is_found = False
            res += 1
            break
print("Smallest number evenly divisible by all numbers from 1 to 20 :", res)