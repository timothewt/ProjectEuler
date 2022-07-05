from math import sqrt


def generate_triangles():
    sides = [0, 0, 0]
    radius = 0
    for a in range(1, 1000):
        b = 1
        while radius < 100:
            c = sqrt(a ** 2 + b ** 2 - a * b)
            if c.is_integer():
                sides = [a, b, c]
                radius = (sqrt(3) / 2) * (b * c) / (a + b + c)
                print(sides, radius)
            b += 1

generate_triangles()
