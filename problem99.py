from math import log


def compare_exp(a, b, c, d):
    return b * log(a) > d * log(c)


data = []

with open("problem99/data.txt") as f:
    lines = f.readlines()

    for line in lines:
        base, exp = line.replace("\n", "").split(",")
        data.append((int(base), int(exp)))


highest_index = 0

for i in range(1, 1000):
    if not compare_exp(data[highest_index][0], data[highest_index][1], data[i][0], data[i][1]):
        highest_index = i


print("Line with the highest number :", highest_index + 1)
