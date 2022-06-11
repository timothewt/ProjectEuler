res = 0
remainder = 200

for i in range(0, remainder + 1, 200):
    remainder = 200 - i
    for j in range(0, remainder + 1, 100):
        remainder = 200 - i - j
        for k in range(0, remainder + 1, 50):
            remainder = 200 - i - j
            for l in range(0, remainder + 1, 20):
                remainder = 200 - i - j - k - l
                for m in range(0, remainder + 1, 10):
                    remainder = 200 - i - j - k - l - m
                    for n in range(0, remainder + 1, 5):
                        remainder = 200 - i - j - k - l - m - n
                        for o in range(0, remainder + 1, 2):
                            remainder = 200 - i - j - k - l - m - n - o
                            for p in range(0, remainder + 1):
                                remainder = 200 - i - j - k - l - m - n - o - p
                                if remainder == 0:
                                    res += 1

print(res)
