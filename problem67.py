from math import sqrt   # dynamic programming and optimal sub-structure


def build_pyramid(num):
    res = []
    num = [int(i) for i in num.split(",")]
    depth = int(sqrt(8 * len(num) + 1) - 1) // 2
    start_pos = 0
    for i in range(1, depth + 1):
        new_elem = []
        for j in range(start_pos, start_pos + i):
            new_elem.append(num[j])
        res.append(new_elem)
        start_pos += i
    return res


with open("problem67/data.txt") as f:
    data = f.read()

data = build_pyramid(data)
size = len(data)

for i in range(size - 2, -1, -1):
    for j in range(0, len(data[i])):
        data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])

print("Max path in the pyramid :", data[0][0])
