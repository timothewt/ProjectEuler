N = 1_000_000
phi = []
for i in range(0, N + 1):
    phi.append(i)
for i in range(2, N + 1):
    if phi[i] == i:
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i

print(sum(phi))

#not my solution