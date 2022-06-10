from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = list(permutations(digits))
perm.sort()

millionth = perm[999_999]
res = 0
for i in range(0, len(digits)):
    res += millionth[i] * (10 ** (len(digits) - i - 1))

print("Millionth lexicographic permutation :", res)
