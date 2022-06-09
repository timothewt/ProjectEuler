sum_squares = 0
square_sum = 0
for i in range(0, 101):
    sum_squares += i**2
print("Sum of the squares in [0,100] :", sum_squares)
for i in range(0, 101):
    square_sum += i
square_sum **= 2
print("Square of the sum of all integers in [0,100] :", square_sum)
print("Sum square difference :", square_sum - sum_squares)
