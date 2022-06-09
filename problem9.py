from math import sqrt, floor

a = 0
b = 0
c = 0

for i in range(1, 1000):
    is_pyth_triplet = True
    for j in range(1, 1000):
        if sqrt(i ** 2 + j ** 2).is_integer():
            a = i
            b = j
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == 1000:
                print("Triplet (a,b,c) as a+b+c = 1000 : ", "(", a, ",", b, ",", c, ")", sep="")
                print("a*b*c =", a * b * c)
                break
    else:
        continue
    break
