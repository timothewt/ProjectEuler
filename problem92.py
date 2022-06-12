def next_node(n):
    res = 0
    for i in str(n):
        res += int(i) ** 2
    return res


def chain_until_stuck(n):
    start = n
    while n != 89 and n != 1:
        n = next_node(n)
        if n in known_nodes:
            n = ending[known_nodes.index(n)]
            return n
    known_nodes.append(start)
    ending.append(n)
    return n


known_nodes = []
ending = []

res = 0

for i in range(1, 10_000_000):
    if chain_until_stuck(i) == 89:
        res += 1

print(res, "numbers below 10,000,000 will at the end of the chain arrive at 89.")