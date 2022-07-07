from math import tan, atan, sqrt, degrees, radians


def atandeg(x):
    return degrees(atan(x))


def tandeg(x):
    return tan(radians(x))


def next_step(last_beam_slope: float, hit_point: list):    # last_beam_slope : y_beam = this*x + a | hit_point : [x,y]
    x1 = hit_point[0]
    y1 = hit_point[1]
    mt = -4 * (x1 / y1)
    m1 = last_beam_slope
    t = 180 - atandeg((m1 - mt) / (1 + mt * m1))
    m2 = (tandeg(t) + mt) / (1 - tandeg(t) * mt)    # new beam : y = m2 * x + b
    b = y1 - m2 * x1
    x2_1 = (-2 * m2 * b + sqrt((2 * m2 * b) ** 2 - 4 * (4 + m2 ** 2) * (b ** 2 - 100))) / (2 * (4 + m2 ** 2))
    x2_2 = (-2 * m2 * b - sqrt((2 * m2 * b) ** 2 - 4 * (4 + m2 ** 2) * (b ** 2 - 100))) / (2 * (4 + m2 ** 2))
    y2_1 = (8 * b + sqrt((8 * b) ** 2 - 4 * (m2 ** 2 + 4) * (4 * b ** 2 - 100 * m2 ** 2))) / (2 * (4 + m2 ** 2))
    y2_2 = (8 * b - sqrt((8 * b) ** 2 - 4 * (m2 ** 2 + 4) * (4 * b ** 2 - 100 * m2 ** 2))) / (2 * (4 + m2 ** 2))
    x2 = x2_1 if abs(x2_1 - x1) > abs(x2_2 - x1) else x2_2  # Takes the other intersection point than the point just hit by the beam
    y2 = y2_1 if abs(y2_1 - y1) > abs(y2_2 - y1) else y2_2
    return m2, [x2, y2]


count = 0
launch_pt = [0, 10.1]
hit_pt = [1.4, -9.6]
slope = (hit_pt[1] - launch_pt[1]) / (hit_pt[0] - launch_pt[0])
while not (-.01 <= hit_pt[0] <= .01 and hit_pt[1] >= 0):
    slope, hit_pt = next_step(slope, hit_pt)
    count += 1

print("The laser will reflect", count, "times before exiting the white cell.")
