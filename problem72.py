### Using a Stern-Brocot tree
# However this solution is not optimal and would take hours even days to compute
"""def count_nodes_recursive(limit, l_d, r_d):
    den = l_d + r_d
    if den > limit:
        return 0
    else:
        return 1 + count_nodes_recursive(limit, l_d, den) + count_nodes_recursive(limit, den, r_d)


def count_nodes_iteraive(limit):
    count = 0
    left = 1
    right = 1
    stack = []
    while True:
        med = left + right
        if med > limit:
            if len(stack) == 0:
                break
            else:
                left = right
                right = stack.pop()
        else:
            count += 1
            stack.append(right)
            right = med
    return count

res = count_nodes_iteraive(12000)

print("Result : ", res)"""

# using Euler's totient formula (executes in few seconds) :
# phi(n) = n * product of (1 - 1 / p) with p being all the distinct prime numbers that divide n

N = 1_000_000
phi = []

for i in range(0, N + 1):  # we generate the list of |[0; N]|
    phi.append(i)

for k in range(2, N + 1):
    if phi[k] == k:  # if the index is equal to the current number it is prime, otherwise it would have been
        # multiplied by a prime number below him
        for m in range(k, N + 1, k):    # we multiply every multiple of this prime number p by 1-1/p as in the formula
            phi[m] -= phi[m] // k
# we then have a list representing the result of the Euler's totient for every integer in |[0; N]|
# an interesting fact is that every number whose index is him + 1 is a prime number
# (because phi(p) = p-p/p = p-1, he's the only prime that can divide him)

res = sum(phi) - 1  # -1 because 1 is in the list but doesn't count in this case
print("Number of reduced proper fraction with a denominator below or equal to", N, ":", res)
