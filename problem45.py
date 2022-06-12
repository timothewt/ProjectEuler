triangular = []
pentagonal = []
hexagonal = []


def is_pentagonal(x):
    j = 0
    while pentagonal[j] <= x:
        if pentagonal[j] == x:
            return True
        j += 1
    return False


def is_triangular(x):
    j = 0
    while triangular[j] <= x:
        if triangular[j] == x:
            return True
        j += 1
    return False


for i in range(1, 100_000):
    triangular.append((i * (i + 1)) // 2)
for i in range(1, 100_000):
    pentagonal.append((i * (3 * i - 1)) // 2)
for i in range(1, 100_000):
    hexagonal.append(i * (2 * i - 1))

n = 0
res = 0

for i in hexagonal:
    if is_pentagonal(i):
        if is_triangular(i):
            n += 1
            if n == 3:  # the 2 first are 1 and 40755
                res = i
                break

print("Result :", res)
