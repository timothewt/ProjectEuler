def find_pattern_length(den):  # one issue with this function : if there are some digits before the pattern, like 1/6 = 0.1(6), it does not detect it
    reminders = [1 % den]
    for i in range(0, den - 1):
        reminder = (reminders[i] * 10) % den
        if reminder in reminders:
            break
        reminders.append(reminder)
    return len(reminders)


max_length = 0
value = 0

for j in range(2, 1000):
    length = find_pattern_length(j)
    if length > max_length:
        value = j
        max_length = length

print("The longest cycle is 1/", value, ", with a length of ", max_length, sep="")
