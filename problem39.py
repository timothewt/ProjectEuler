from math import sqrt
from tqdm import tqdm


def compute_c(a, b):
    return sqrt(a ** 2 + b ** 2)


def gen_right_int_tri(a, b):    # returns None if the triangle is not integer or the perimeter is over 1000
    if 1000*a + 1000*b - a * b > 5 * 10 ** 5:
        return None
    c = compute_c(a, b)
    if int(c) == c:
        return (a, b, c)
    return None


triangles = set()

for i in tqdm(range(0, 1000)):
    for j in range(0, 1000):
        triangles.add(gen_right_int_tri(i, j))

triangles.remove(None)
triangles = list(triangles)
perimeters = []
max_perimeter = 0
max_count = 0

for tri in triangles:
    perimeters.append(sum(tri))

for i in range(1, 1000):
    if perimeters.count(i) > max_count:
        max_perimeter = i
        max_count = perimeters.count(i)

print("The maximum of triangles is reached for p = ", max_perimeter,", indeed there are ", max_count, " integers triangles for which p = ", max_perimeter, ".", sep='')
