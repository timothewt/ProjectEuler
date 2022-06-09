from dataclasses import dataclass


@dataclass
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def contains_point(m, tr):         # m being the point we want to know if it's in the triangle
    A = Coord(tri[0][0], tri[0][1])
    B = Coord(tri[1][0], tri[1][1])
    C = Coord(tri[2][0], tri[2][1])
    M = Coord(m[0], m[1])
    s = ((M.x - A.x) * (B.y - A.y) - (M.y - A.y) * (B.x - A.x)) / ((C.x - A.x) * (B.y - A.y) - (C.y - A.y) * (B.x - A.x))
    t = ((M.y - A.y) * (C.x - A.x) - (M.x - A.x) * (C.y - A.y)) / ((B.y - A.y) * (C.x - A.x) - (B.x - A.x) * (C.y - A.y))
    return 0 <= s <= 1 and 0 <= t <= 1 and s + t <= 1


triangles = []
valid_count = 0

with open('problem102/triangles.txt') as f:
    lines = f.readlines()

for line in lines:
    temp = list(map(int, line.split(",")))
    tri = [[temp[0], temp[1]],
           [temp[2], temp[3]],
           [temp[4], temp[5]]]
    triangles.append(tri)

f.close()

for triangle in triangles:
    if contains_point([0,0], triangle):
        valid_count += 1

print("Number of triangle containing the point (0,0) :", valid_count)