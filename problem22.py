alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('problem22/names.txt') as f:
    names = f.readlines()[0]
f.close()
names = names.replace("\"", "").split(',')
names.sort()

total_score = 0
i = 1
for name in names:
    score = 0
    for letter in name:
        score += alphabet.index(letter) + 1
    total_score += score * i
    i += 1

print("Total score of the list :", total_score)
