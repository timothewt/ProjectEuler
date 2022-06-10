units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_twenty = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def count_letters(n):
    unit = n % 10
    ten = (n // 10) % 10
    hundred = (n // 100) % 10
    count = 0
    if unit == 0 and ten == 0 and hundred != 0:
        count += len(units[hundred] + "hundred")
    else:
        if hundred > 0:
            count += len(units[hundred] + "hundredand")
        if ten == 1:
            count += len(ten_to_twenty[unit])
        else :
            count += len(tens[ten] + units[unit])
    return count


count_1_to_1000 = 0
for i in range (1, 1000):
    count_1_to_1000 += count_letters(i)

count_1_to_1000 += len("onethousand")

print("Length of all numbers written in text from 1 to 1000:", count_1_to_1000)
