from tqdm import tqdm


def is_pan_prod(a, b):   # checks if a * b = n is a pandigital number
    n = a * b
    string = str(a) + str(b) + str(n)
    return len(set(string)) == 9 and len(string) == 9 and '0' not in string


valid_products = set()

for i in range(1, 10):
    for j in range(1_000, 10_000):
        if is_pan_prod(i, j):
            print(i, j, i * j)
            valid_products.add(i * j)

for i in range(10, 100):
    for j in range(100, 1_000):
        if is_pan_prod(i, j):
            print(i, j, i * j)
            valid_products.add(i * j)

print("Result : ", sum(valid_products))
