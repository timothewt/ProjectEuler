"""import sys

sys.setrecursionlimit(3000000)


### Stern-Brocot Tree


class Node:
    def __init__(self, val, l_son, r_son, l_neighbour, r_neighbour):
        self.val = val  # [num, den]
        self.l_son = l_son
        self.r_son = r_son
        self.l_neighbour = l_neighbour  # [num, den]
        self.r_neighbour = r_neighbour  # [num, den]

    def count_nodes(self):
        if self.l_son is None or self.r_son is None:
            return 1
        else:
            return 1 + self.l_son.count_nodes() + self.r_son.count_nodes()

    def display(self):
        print(self.val)
        if self.l_son is not None:
            self.l_son.display()
        if self.r_son is not None:
            self.r_son.display()


def build_tree(val, l_neighbour, r_neighbour):
    if val[1] > 1_000_000:
        return None
    else:
        l_s = build_tree([l_neighbour[0] + val[0], l_neighbour[1] + val[1]], l_neighbour, val)
        r_s = build_tree([val[0] + r_neighbour[0], val[1] + r_neighbour[1]], val, r_neighbour)
        return Node(val, l_s, r_s, l_neighbour, r_neighbour)
# Recursive method is too long and my computer doesn't go to the end


tree = build_tree([1, 2], [0, 1], [1, 1])
print(tree.count_nodes())"""

N = 1_000_000
phi = []
for i in range(0, N + 1):
    phi.append(i)
for i in range(2, N + 1):
    if phi[i] == i:
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i

print(sum(phi) - 1)

# not my solution
