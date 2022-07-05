from itertools import permutations


def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def is_correct(primes_list):
    gaps = []
    indexes = []
    for i in range(0, len(primes_list)):
        for j in range(i + 1, len(primes_list)):
            gap = primes_list[j] - primes_list[i]
            indexes.append([i, j])
            gaps.append(gap)
    for gap in gaps:
        if len(indices(gaps, gap)) == 2:
            if indexes[indices(gaps, gap)[0]][1] == indexes[indices(gaps, gap)[1]][0]:
                str1 = str(primes_list[indexes[indices(gaps, gap)[0]][0]])
                str2 = str(primes_list[indexes[indices(gaps, gap)[0]][1]])
                str3 = str(primes_list[indexes[indices(gaps, gap)[1]][1]])
                return [True, str1 + str2 + str3]
    return False


with open("primes1.txt") as f:   # the primes in the file are all the primes below 1 million
    primes = f.read()

primes = primes.split()

primes = [i for i in primes if len(i) == 4]

res = ''

for prime in primes:
    perms = [''.join(p) for p in permutations(prime)]
    correct_perms = list(dict.fromkeys([int(perm) for perm in perms if perm in primes]))
    correct_perms.sort()
    if is_correct(correct_perms) is not False:
        if is_correct(correct_perms)[1] != '148748178147':
            res = is_correct(correct_perms)[1]
            break

print("Result:", res)
