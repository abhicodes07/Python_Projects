
# Finding factorial of a number using while loop

num = int(input("Enter the numbers: "))
factorial = 1
i = num
while i != 0:
    factorial *= i
    i -= 1

print("Factorial: ", factorial)



