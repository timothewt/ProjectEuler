from math import factorial


def next_node(n):
    return sum([factorial(int(i)) for i in str(n)])


count = 0
for i in range(1, 1_000_000):
    nodes = [i]
    i = next_node(i)
    while i not in nodes:
        nodes.append(i)
        i = next_node(i)
        if len(nodes) > 60:
            break
    if len(nodes) == 60:
        count += 1

print("Result:", count)
