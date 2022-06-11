from math import sqrt


# 1_2_3_4_5_6_7_8_9_0 ends with 0 and is a square, so it ends in 00. We can now search for 1_2_3_4_5_6_7_8_9 and
# multiply the result root by 10. It ends by 9 so the root has to end with 3 or 7. Also, the last _ has to be different
# from 9. The minimum possible root is sqrt(10203040506070809) and the max is sqrt(19293949596979899)

def is_valid(n):
    n = str(n)
    for j in range(0, 9):
        if n[2 * j] != str(j + 1):
            break
    else:
        return True
    return False

res = 0

for i in range(int(sqrt(10203040506070809)) // 10, int(sqrt(19293949596979899)) // 10 + 1):
    if is_valid((10 * i + 3) ** 2):
        res = (10 * i + 3) * 10
        break
    if is_valid((10 * i + 7) ** 2):
        res = (10 * i + 7) * 10
        break

print("Unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0 :", res)
print(res, "^2 = ", res ** 2, sep='')
