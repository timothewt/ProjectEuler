sum = 0

for i in range(1, 1001):
    sum += i ** i

str_sum = str(sum)

print("Last ten digits of the series 1^1+2^2+3^3+...+1000^1000 :", str_sum[len(str_sum) - 10:])
print(sum)