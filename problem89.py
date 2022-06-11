""" Algorithm with most extreme example :
MMMMDCCCCLXXXXVIIII     1) if we have IIII => IV
=> MMMMDCCCCLXXXXVIV    2) if we have VIV => IX
=> MMMMDCCCCLXXXXIX     3) if we have XXXX => XL
=> MMMMDCCCCLXLIX       4) if we have LXL => XC
=> MMMMDCCCCXCIX        5) if we have CCCC => CD
=> MMMMDCDXCIX          6) if we have DCD => CM
=> MMMMCMXCIX           7) fin
"""

def optimise_roman(n):
    n = n.replace("IIII", "IV")     # this only replaces if the string is in the word therefore if it's not, does nothing
    n = n.replace("VIV", "IX")
    n = n.replace("XXXX", "XL")
    n = n.replace("LXL", "XC")
    n = n.replace("CCCC", "CD")
    n = n.replace("DCD", "CM")
    return n


def count_char(list):
    res = 0
    for string in list:
        res += len(string)
    return res


with open('problem89/data.txt') as f:
    numbers = f.readlines()

for i in range(0, len(numbers)):
    numbers[i] = numbers[i].replace('\n', '')

start_char = count_char(numbers)

for i in range(0, len(numbers)):
    numbers[i] = optimise_roman(numbers[i])

end_char = count_char(numbers)

print("By optimising the writing we used", start_char - end_char, "less characters.")