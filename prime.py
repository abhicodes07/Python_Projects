
# This is a program about finding whether a number is prime or not
num = int(input("Enter the number: "))

flag = 0
if num == 0 or num == 1:
    flag = 1
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 0:
    print("Entered number is a prime number.")
else:
    print("Entered number is not a prime number.")



