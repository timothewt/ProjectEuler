string = ''
i = 1
while len(string) < 10 ** 7:
    string = string + str(i)
    i += 1

res = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])

print("Result :", res)

# great solution however, i have to do it again without brute forcing
