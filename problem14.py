res = 0
max_chain_length = 0

for i in range(2, 1000000):
    chain_length = 0
    current = i
    while current > 1:
        if current % 2 == 0:
            current /= 2
        else:
            current = 3 * current + 1
        chain_length += 1
    if chain_length > max_chain_length:
        res = i
        max_chain_length = chain_length

print("Max chain length :", max_chain_length, "with n =", res)
