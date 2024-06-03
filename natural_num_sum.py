# This is a program on demonstrating sum of all natural numbers

num = int(input("Enter the number: "))

add = 0
flag = 0


while flag != num+1:
    add += flag
    flag += 1
print("sum : {}". format(add))


