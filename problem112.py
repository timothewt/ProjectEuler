from collections import Counter


def is_bouncy(n):
    num = str(n)
    if len(Counter(set(num))) == 1:
        return False
    i = 0
    while num[i] == num[i + 1]:
        i += 1
    sign = 1 if int(num[i + 1]) - int(num[i]) > 0 else -1
    for k in range(i, len(num) - 1):
        if num[k] == num[k + 1]:
            continue
        if sign < 0 and int(num[k]) - int(num[k + 1]) < 0:
            return True
        if sign > 0 and int(num[k]) - int(num[k + 1]) > 0:
            return True
    return False


count = 0
i = 100     # no bouncy numbers under 100

while count/i < .99:
    i += 1
    if is_bouncy(i):
        count += 1

print("There are ", int(count / i * 100),"% of bouncy numbers under ", i, ".",sep='')
