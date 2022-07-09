from tqdm import tqdm


def shuffle(d):         # useless
    top = d[:len(d) // 2]
    bottom = d[len(d) // 2:]
    new_deck = []
    for j in range(0, len(d)):
        if j % 2 == 0:
            new_deck.append(top[j // 2])
        else:
            new_deck.append(bottom[j // 2])
    return new_deck


n = 60
sizes = [2 * i for i in tqdm(range(1, 2 ** n + 1)) if (2 ** n) % (2 * i - 1) == 1]
s = sum(sizes)
print(sizes)
print(s)
