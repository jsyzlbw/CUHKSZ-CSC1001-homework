#get an input
num = input("Enter an positive number")

#get each digit and calculate the sum
sum_digits = 0
for digit in num:
    sum_digits += int(digit)

print(f"The sum of the digits of {num} is: {sum_digits}")