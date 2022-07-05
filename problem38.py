def is_pan(n: str):
    return len(set(n)) == 9 and len(n) == 9 and '0' not in n


for i in range(9876, 9123, -1):
    if is_pan(str(i) + str(2 * i)):
        print("Result :", str(i) + str(2 * i))
        break
