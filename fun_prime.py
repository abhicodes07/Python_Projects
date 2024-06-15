# a program to demonstrate prime numbers using function

def prime(num):
    flag = 0
    if num == 0 or num == 1:
        flag = 1
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
    if flag == 1:
        print("Number is not prime.")
    else:
        print("Number is prime.")

num = int(input("Enter the number: "))
prime(num)
