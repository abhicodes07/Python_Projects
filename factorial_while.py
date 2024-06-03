
# Program for finding factorial of number using for loop

num = int(input("Enter the number: "))

factorial = 1

for i in range(1, num+1):
    factorial *= i
    i -= 1

print("factorial = ", factorial)



