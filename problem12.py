from math import ceil, sqrt

res = 1
i = 0
tri_nb = 0

while res == 1:
    i += 1
    tri_nb += i
    divisors_nb = 0
    for j in range(1, ceil(sqrt(tri_nb + 1))):
        if tri_nb % j == 0:
            divisors_nb += 2
    if divisors_nb > 500:
        res = tri_nb
print("First triangle number to have over 500 divisors :", res)
