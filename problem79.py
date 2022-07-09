import collections

with open("problem79/data.txt") as f:   # the primes in the file are all the primes below 1 million
    data = f.read()

digits = [int(item) for item, cnt in collections.Counter([code for code in data]).items() if item != '\n']
codes = [item for item, count in collections.Counter([code for code in data.split()]).items()]


def previous_digits(n):
    n = str(n)
    res = set()
    for code in codes:
        if code[0] == n:
            continue
        elif code[1] == n:
            res.add(code[0])
        elif code[2] == n:
            res.add(code[0])
            res.add(code[1])
        else:
            continue
    return list(res)


result = [None] * len(digits)
for digit in digits:
    pos = len(previous_digits(digit))
    result[pos] = digit
result = ''.join(map(str, result))

print('Result:', result)
