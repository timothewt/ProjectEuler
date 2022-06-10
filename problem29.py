def remove_duplicates(arr):
    arr.sort()
    index = 0
    max = len(arr) - 1
    while index < max:
        while arr[index] == arr[index + 1]:
            arr.pop(index + 1)
            max -= 1
        index += 1
    return arr


numbers = []

for i in range(2, 101):
    for j in range(2, 101):
        numbers.append(i ** j)

numbers = remove_duplicates(numbers)
print("Result :", len(numbers))
