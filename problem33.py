def highest_common_divisor(a, b):
    res = 1
    for k in range(1, min(a, b) + 1):
        if a // k == a / k and b // k == b / k:
            res = k
    return res

frac = []  # each element is [numerator, denominator]

for i in range(10, 100):          #den
    for j in range(10, i):       #num, up to i because the fraction is less than one
        if str(j)[0] == str(i)[0] and int(str(i)[1]) != 0:
            if int(str(j)[1]) / int(str(i)[1]) == j/i:
                frac.append([j, i])
        if str(j)[1] == str(i)[0] and int(str(i)[1]) != 0:
            if int(str(j)[0]) / int(str(i)[1]) == j/i:
                frac.append([j, i])
        if str(j)[0] == str(i)[1]:
            if int(str(j)[1]) / int(str(i)[0]) == j/i:
                frac.append([j, i])

print("Fractions with this property :")
for i in range(0, 4):
    print(frac[i][0], "/", frac[i][1], sep='')
product = [frac[0][0] * frac[1][0] * frac[2][0] * frac[3][0], frac[0][1] * frac[1][1] * frac[2][1] * frac[3][1]]
div = highest_common_divisor(product[0], product[1])
print("Product of the fractions :")
print(product[0], "/", product[1], " = ", product[0] // div, "/", product[1] // div, sep='')
