alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def t(n):
    return n * (n + 1) // 2


def is_triangle(str):
    s = 0
    for c in str:
        s += alphabet.index(c) + 1
    return s in triangles


with open('problem42/data.txt') as f:
    words = f.read()

words = words.split(",")

max_length = max([len(s) for s in words])

triangles = []

for i in range(1, 1_000):
    triangles.append(t(i))
    if triangles[i - 1] > max_length * 26:  # the maximum value of the word is the max_length times the value of Z
        break

res = 0

for word in words:
    if is_triangle(word):
        res += 1

print("There are", res, "triangle words in the list.")
